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

	qry = "SELECT DISTINCT Scientific_name FROM PATHOGEN WHERE Scientific_name LIKE %s OR Other_names LIKE %s LIMIT 5"
	cursor.execute(qry, ('%' + term + '%', '%' + term + '%'))

	results = { 'suggestions': list() }
	for row in cursor:
		results['suggestions'].append(row[0])

	cursor.close()
	conn.close()

	print(json.dumps(results))


if __name__ == '__main__':
	main()
