#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')

    conn = mysql.connector.connect(user='ywang833', password='Bioinformatics!', host='localhost', database='biotest')
    cursor = conn.cursor()

    qry = "SELECT DISTINCT product FROM genes WHERE product LIKE %s LIMIT 5"
    cursor.execute(qry, ('%' + term + '%', ))

    results = { 'suggestions': list() }
    for product in cursor:
        results['suggestions'].append(product[0])

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()
