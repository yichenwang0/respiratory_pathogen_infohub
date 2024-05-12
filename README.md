# Respiratory Pathogen Information Hub

## Overview
The Respiratory Pathogen Information Hub is a web application designed to provide comprehensive information about various respiratory pathogens.

## Features
- **Pathogen Search:** Users can search for specific respiratory pathogens by their scientific or common names with autocomplete support.
- **General Information:** Users can access inforamtion such as scientific names, common aliases, major subtypes, genome types, and associated symptoms for each pathogen.
- **Gene Annotation:** Detailed gene annotation data is provided for each pathogen.
- **NCBI Reference Sequence Access:** Direct links to NCBI reference sequences are available for further exploration.
- **Support for Multiple Segments:** The application has a specialized layout for pathogens with segmented genomes (influenza viruses).

## Usage
### 1. Enter a search term and hit submit. ###
<img src="https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/1b644d40-7ffc-48d7-8311-65ad2afe4911" alt="image" width="40%">

- **Option 1:** Search for a general term to view all respiratory pathogens with similar names.
  ![image](https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/a73e5041-c0f7-489c-a7dd-5e1861949137)

- **Option 2:** Search for the common name of a specific respiratory pathogen.
  ![image](https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/db4caa24-14b2-4670-92b5-92adde3c8a66)

- **Option 3:** Search for the scientific name of a specific respiratory pathogen. This example also demonstrates the autocomplete function. Note that autocomplete suggestions always display scientific names, even if a common name is entered.
  <img src="https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/5ac68f8c-f731-4963-a664-ecaec402f37b" alt="image" width="40%">
  <img src="https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/faf1250d-bc7f-4794-b279-5796de061595" alt="image" width="80%">

### 2. Select a pathogen to view its detailed gene annotation by clicking "View Gene Annotation". (Optional) ###

- **Example 1:** Human bocavirus 1
  ![image](https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/531317fb-1708-4fe1-b84d-4150a88554fd)

- **Example 2:** Influenza B
  ![image](https://github.com/yichenwang0/respiratory_disease_infohub/assets/59595330/5765704e-d739-4428-925e-9630ca8f583a)
  Please note that the screenshots only display the top portion of the gene annotation page.
   
### 3. Visit the corresponding NCBI GenBank reference sequence page by clicking the highlighted accession number. (Optional) ###

## Requirements
### Deployment Options ###
- **Online Access**: The Respiratory Pathogen Information Hub is currently deployed on the bfx3.aap.jhu.edu server. To access the application online, you need to be connected to the JHU Network or VPN. Once connected to the JHU network or VPN, you can access the application using the following link: [Respiratory Pathogen Information Hub](http://bfx3.aap.jhu.edu/ywang833/final/respiratory_pathogen_infohub.html) A stable internet connection is recommended for seamless usage.
- **Self-Deployment**: You can clone this GitHub repository to another web server that is capable of serving Python CGI files. Execute the `database_setup.sql` script in a MySQL server to set up the required database schema. Run the `extract.py` script with the path to each GenBank file and its corresponding `pathogen_id` to finish populating the tables. Make sure to modify the MySQL connector in the Python CGI scripts accordingly. 
### Hardware Recommendations ###
For optimal performance, the following hardware specifications are recommended:
- **Memory**: At least 2 GB of RAM.
- **CPU**: A clock speed of at least 2.5 GHz.

## File Descriptions

- `Project Proposal.pdf`: PDF document containing the original project proposal.
- `README.md`: You are here! Markdown file containing basic information about the application and instructions for usage.
- `gene_annotation.cgi`: Python CGI script that retrieves gene annotation information from the MySQL database based on the provided pathogen ID and generates a dynamic HTML page displaying the gene annotations.
- `pathogen_search.cgi`: Python CGI script responsible for handling the search functionality on the main page of the infohub. It retrieves pathogen information from the MySQL database based on the user's input and returns the results in JSON format to be processed by the JavaScript frontend.
- `pathogen_suggestion.cgi`: Python CGI script designed to provide autocomplete suggestions for pathogens as the user types into the search box. It interacts with the MySQL database to fetch distinct pathogen names that match the user's input. These suggestions are then returned to the client-side JavaScript for display in real-time.
- `respiratory_pathogen_infohub.html`: HTML file serving as the main webpage for the respiratory pathogen information hub.

- css:
  - `search_product.css`: CSS file for styling the pathogen search page.
  - `gene_annotation_result.css`: CSS file for styling the gene annotation page.

- js:
  - `search.js`: JavaScript file responsible for enabling autocomplete functionality in the search box and dynamically updating the result table on the pathogen search page.

- sources:
  - `.gb files`: GenBank files for all respiratory pathogens in the database.
  - `database_setup.sql`: SQL script for setting up the database schema and populating the PATHOGEN table.
  - `extract.py`: Python script for extracting information from GenBank files and populating the REFERENCE_SEQUENCE and CDS tables in the MySQL database.

- templates:
  - `gene_annotation.html`: HTML template for displaying gene annotation information. 
