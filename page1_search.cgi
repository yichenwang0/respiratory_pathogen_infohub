#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
	print("Content-Type: application/json\n\n")
	form = cgi.FieldStorage()
	term = form.getvalue('search_term')

	conn = mysql.connector.connect(user='ywang833', password='Bioinformatics!', host='localhost', database='ywang833_final')
	cursor = conn.cursor()

	qry = """
		SELECT Scientific_name, Other_names, Major_subtypes, Genome, Symptoms
		FROM PATHOGEN
		WHERE Scientific_name LIKE %s OR Other_names LIKE %s
	"""
	cursor.execute(qry, ('%' + term + '%', '%' + term + '%'))

	results = { 'match_count': 0, 'matches': list() }
	for (scientific_name, other_names, major_subtypes, genome, symptoms) in cursor:
		results['matches'].append({
			'scientific_name': scientific_name,
			'other_names': other_names,
			'major_subtypes': major_subtypes,
			'genome': genome,
			'symptoms': symptoms
		})
		results['match_count'] += 1

	conn.close()
	
	print(json.dumps(results))


if __name__ == '__main__':
	main()
