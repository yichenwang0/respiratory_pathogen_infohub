import os
import re
import mysql.connector

# This function generates insert statements for REFERENCE_SEQUENCE table
def generate_ref(accession, link, sequence, pathogen_id, segment):
	if segment == '0':
		insert_str = f'INSERT INTO REFERENCE_SEQUENCE (Accession, Link, Sequence, Pathogen_id, Segment) VALUES ("{accession}", "{link}", "{sequence}", {pathogen_id}, NULL);'
	else:
		insert_str = f'INSERT INTO REFERENCE_SEQUENCE (Accession, Link, Sequence, Pathogen_id, Segment) VALUES ("{accession}", "{link}", "{sequence}", {pathogen_id}, {segment});'
	return insert_str

# This function generates insert statements for CDS table
def generate_cds(accession, five_coord, three_coord, strand, gene_symbol, product):
	if gene_symbol is None and product is None:
		insert_str = f'INSERT INTO CDS (Accession, 5_coordinate, 3_coordinate, Strand, Gene_symbol, Product) VALUES ("{accession}", {five_coord}, {three_coord}, "{strand}", NULL, NULL);'
	elif gene_symbol is None:
		insert_str = f'INSERT INTO CDS (Accession, 5_coordinate, 3_coordinate, Strand, Gene_symbol, Product) VALUES ("{accession}", {five_coord}, {three_coord}, "{strand}", NULL, "{product}");'
	elif product is None:
		insert_str = f'INSERT INTO CDS (Accession, 5_coordinate, 3_coordinate, Strand, Gene_symbol, Product) VALUES ("{accession}", {five_coord}, {three_coord}, "{strand}", "{gene_symbol}", NULL);'
	else:
		insert_str = f'INSERT INTO CDS (Accession, 5_coordinate, 3_coordinate, Strand, Gene_symbol, Product) VALUES ("{accession}", {five_coord}, {three_coord}, "{strand}", "{gene_symbol}", "{product}");'
	return insert_str

# This function extracts reference sequence and CDS information from the input GenBank file
# and populate ywang833_final database
def extraction(input_file, pathogen_id, segment):

	# Establish connection to MySQL database
	conn = mysql.connector.connect(user='ywang833', password='Bioinformatics!', host='localhost', database='ywang833_final')
	curs = conn.cursor()

	# Variables to store accesion, sequence, and annotations
	accession_no = ''
	sequence = ''
	CDS_list = []

	# Parse out information from GenBank file
	accession_exist = False
	annotation_start = False
	sequence_start = False
	five_coord = 0
	three_coord = 0
	strand = '+'
	gene_symbol = None
	product_name =None
	CDS_gene = False
	CDS_product = False
	product_accumulator = ''
	product_continue = False
	for line in open(input_file, 'r'):
		# Extract accession
		if line.strip().startswith('VERSION') and not accession_exist:
			accession = re.search(r'VERSION\s+(\S+)', line)
			if accession:
				accession_no = accession.group(1)
				accession_exist = True
		# Extract CDS annotation
		elif line.strip().startswith('FEATURES'):
			annotation_start = True
		elif line.strip().startswith('CDS') and annotation_start:
			if five_coord != 0 and three_coord != 0:
				CDS_list.append((five_coord, three_coord, strand, gene_symbol, product_name))
				five_coord = 0
				three_coord = 0
				strand = '+'
				gene_symbol = None
				product_name = None
			numbers = re.findall(r'\d+', line)
			if numbers:
				five_coord = int(numbers[0])
				three_coord = int(numbers[-1])
				CDS_gene = True
				CDS_product = True
			if 'complement' in line:
				strand = '-'
		elif 'gene=' in line and CDS_gene:
			gene = re.search(r'/gene="([^"]+)"', line)
			if gene:
				gene_symbol = gene.group(1)
				CDS_gene = False
		elif product_continue:
                        product_accumulator += ' '
                        product_accumulator += line.strip().strip('"')
                        if '"' in line.strip():
                                product_name = product_accumulator
                                CDS_product = False
                                product_continue = False
                                product_accumulator = ''
		elif 'product=' in line and CDS_product:
			product = re.search(r'/product="([^"]+)"', line)
			if product:
				product_name = product.group(1)
				CDS_product = False
			else:
				product_accumulator += line.strip().split('=')[1].strip('"')
				product_continue = True
		# Extract sequence
		elif line.strip().startswith('ORIGIN'):
			annotation_start = False
			sequence_start = True
		elif line.strip().startswith('//') and sequence_start:
			break
		elif sequence_start:
			sequence += re.sub(r'[\d\s]', '', line.strip()).upper()

	CDS_list.append((five_coord, three_coord, strand, gene_symbol, product_name))
	
	# Insert statement for REFERENCE_SEQUENCE table
	link = f"https://www.ncbi.nlm.nih.gov/nuccore/{accession_no}?report=genbank"
	ref_insert = generate_ref(accession_no, link, sequence, pathogen_id, segment)
	print(ref_insert)
	curs.execute(ref_insert)

	# Insert statements for CDS table
	for cds in CDS_list:
		cds_insert = generate_cds(accession_no, *cds)
		print(cds_insert)
		curs.execute(cds_insert)

	# Commit changes and close connection
	conn.commit()
	curs.close()
	conn.close()

if __name__ == "__main__":
	# Prompt user to enter path or file name for the extraction
	input_file = input("Enter the GenBank file to be extracted: ")
	# Check if the correct input is entered
	if not os.path.isfile(input_file):
		print("Error: No file found")
	else:
		pathogen_id = input("Enter pathogen ID: ")
		segment = input("Enter segment (0 if not applicable): ")
		extraction(input_file, pathogen_id, segment)
