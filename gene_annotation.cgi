#!/usr/local/bin/python3

import cgi
import os
import mysql.connector
import jinja2

def main():
	# Parse the query parameter from the URL
	form = cgi.FieldStorage()
	p_id = form.getvalue('pathogen_id')
	pathogen = form.getvalue('pathogen')

	# Query the databae to fetch the gene annotation based on the pathogen id
	conn = mysql.connector.connect(user='ywang833', password='Bioinformatics!', host='localhost', database='ywang833_final')
	cursor = conn.cursor()
	qry_seq = """
		SELECT R.Accession, R.Link, R.Segment, R.Sequence
		FROM REFERENCE_SEQUENCE R
		WHERE R.Pathogen_id = %s
	"""
	cursor.execute(qry_seq, (p_id,))
	qry_seq_results = cursor.fetchall()
	if len(qry_seq_results) > 1:
		multiple_segment = True
	else:
		multiple_segment = False
	entries = list()
	qry_cds = """
		SELECT C.5_coordinate, C.3_coordinate, C.Strand, C.Gene_symbol, C.Product
		FROM CDS C
		WHERE C.Accession = %s
	"""
	if multiple_segment:
		accession = list()
		link = list()
		for (acc, lk, segment, sequence) in qry_seq_results:
			accession.append(acc)
			link.append(lk)
			cursor.execute(qry_cds, (acc,))
			for (five_coord, three_coord, strand, gene, product) in cursor:
				if gene is None:
					gene = 'N/A'
				if product is None:
					product = 'N/A'
				if strand == '+':
					gene_sequence = sequence[five_coord - 1:three_coord]
				else:
					gene_sequence = reverse_complement(sequence[five_coord - 1:three_coord])
				entries.append((five_coord, three_coord, strand, gene, product, gene_sequence, segment))
	else:
		accession, link, segment, sequence = qry_seq_results[0]
		cursor.execute(qry_cds, (accession,))
		for (five_coord, three_coord, strand, gene, product) in cursor:
			if gene is None:
				gene = 'N/A'
			if product is None:
				product = 'N/A'
			if strand == '+':
				gene_sequence = sequence[five_coord - 1:three_coord]
			else:
				gene_sequence = reverse_complement(sequence[five_coord - 1:three_coord])
			entries.append((five_coord, three_coord, strand, gene, product, gene_sequence))
	
	# Load template
	templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
	env = jinja2.Environment(loader=templateLoader)
	template = env.get_template('gene_annotation.html')
	rendered_template = template.render(pathogen=pathogen, multiple_segment=multiple_segment, link=link, accession=accession, entries=entries)
	print("Content-Type: text/html\n\n")
	print(rendered_template)

	cursor.close()
	conn.close()
	
def reverse_complement(seq):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	rev_seq = ''
	for base in reversed(seq):
		rev_seq += complement[base]
	return rev_seq

if __name__ == '__main__':
	main()
