import os
import re

# This function extracts CDS information from the input GenBank file
def extraction(input_file) :
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
	
	print(CDS_list)
	print(accession_no)
	print(sequence)

if __name__ == "__main__":
	# Prompt user to enter path or file name for the extraction
	input_file = input("Enter the GenBank file to be extracted: ")
	# Check if the correct input is entered
	if not os.path.isfile(input_file):
		print("Error: No file found")
	else:
		extraction(input_file)
