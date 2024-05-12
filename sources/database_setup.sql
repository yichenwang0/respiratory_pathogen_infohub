CREATE SCHEMA IF NOT EXISTS ywang833_final;
USE ywang833_final;

CREATE TABLE IF NOT EXISTS PATHOGEN (
Pathogen_id INT NOT NULL,
Scientific_name VARCHAR(100) NOT NULL,
Genome VARCHAR(250) NOT NULL,
Symptoms VARCHAR(250) NOT NULL,
Other_names VARCHAR(250),
Major_subtypes VARCHAR(45),
CONSTRAINT PT_PK
	PRIMARY KEY (Pathogen_id)
);

CREATE TABLE IF NOT EXISTS REFERENCE_SEQUENCE (
Accession VARCHAR(20) NOT NULL,
Link VARCHAR(250) NOT NULL,
Sequence MEDIUMTEXT NOT NULL,
Pathogen_id INT,
Segment INT,
CONSTRAINT REF_PK
	PRIMARY KEY (Accession),
CONSTRAINT REF_PT_FK
	FOREIGN KEY (Pathogen_id) REFERENCES PATHOGEN (Pathogen_id)
	ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS CDS (
CDS_id INT AUTO_INCREMENT NOT NULL,
Accession VARCHAR(20) NOT NULL,
Gene_symbol VARCHAR(100),
Product VARCHAR(100),
5_coordinate INT NOT NULL,
3_coordinate INT NOT NULL,
Strand CHAR(1) NOT NULL,
CONSTRAINT CDS_PK
	PRIMARY KEY (CDS_id, Accession),
CONSTRAINT CDS_ACC_FK
	FOREIGN KEY (Accession) REFERENCES REFERENCE_SEQUENCE (Accession)
	ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO PATHOGEN (Pathogen_id, Scientific_name, Other_names, Major_subtypes, Genome, Symptoms) VALUES
(1, 'Human bocavirus 1', 'HBoV1', NULL, 'ssDNA (+/-) virus', 'Common cold symptoms, including fever, runny nose, and cough'),
(2, 'Human rhinovirus A', 'HRV-A, HRVA', NULL, 'ssRNA (+) virus', 'Common cold symptoms, including sore throat, runny nose, cough, and headache'),
(3, 'Human rhinovirus B', 'HRV-B, HRVB', NULL, 'ssRNA (+) virus', 'Common cold symptoms, including sore throat, runny nose, cough, and headache'),
(4, 'Human rhinovirus C', 'HRV-C, HRVC', NULL, 'ssRNA (+) virus', 'Causes common cold symptoms, including fever, sore throat, runny nose, cough, and headache, and is generally more severe than HRV-A and HRV-B'),
(5, 'Middle East respiratory syndrome-related coronavirus', 'MERS-CoV, MERS', NULL, 'ssRNA (+) virus', 'Fever, cough, and shortness of breath'),
(6, 'Human coronavirus NL63', 'HCoV-NL63', NULL, 'ssRNA (+) virus', 'Fever, nasal congestion, sore throat, and cough'),
(7, 'Human respirovirus 1', 'HPIV-1, PIV1, Parainfluenza virus type 1', NULL, 'ssRNA (-) virus', 'Causes common cold symptoms such as fever, runny nose, and cough, and is also a common cause of croup'),
(8, 'Human respirovirus 3', 'HPIV-3, PIV3, Parainfluenza virus type 3', NULL, 'ssRNA (-) virus', 'A major cause of bronchiolitis and pneumonia'),
(9, 'Severe acute respiratory syndrome coronavirus 2', 'SARS-CoV-2, COVID-19', 'Alpha, Beta, Gamma, Delta, Omicron', 'ssRNA (+) virus', 'Fever, cough, shortness of breath, body ache, loss of taste or smell, sore throat, nasal congestion, nausea, and diarrhea'),
(10, 'Human mastadenovirus B', 'HAdV-B, Human adenovirus B', '3, 7, 14, 21', 'dsDNA virus', 'Causes common cold symptoms such as fever, cough, sore throat, and nasal congestion, and may also lead to conjunctivitis'),
(11, 'Human mastadenovirus C', 'HAdV-C, Human adenovirus C', '1, 2, 5, 6', 'dsDNA virus', 'Common cold symptoms such as fever, cough, sore throat, and nasal congestion'),
(12, 'Bordetella pertussis', 'Whooping cough', NULL, 'ssDNA bacterium', 'Common cold symptoms with violent and rapid cough that sounds like "woop"'),
(13, 'Bordetella parapertussis', NULL, NULL, 'ssDNA bacterium', 'Common cold symptoms with cough similar to but milder than pertussis'),
(14, 'Chlamydia pneumoniae', 'Taiwan acute respiratory agent, TWAR', NULL, 'dsDNA bacterium', 'Runny nose, fatigue, low-grade fever, sore throat, and a persistent, slowly worsening cough'),
(15, 'Influenza A virus', 'Flu A', 'H1N1, H3N2', 'ssRNA (-) virus', 'Fever (often high-grade), cough, sore throat, runny nose, muscle ache, and sometimes vomiting and diarrhea'),
(16, 'Influenza B virus', 'Flu B', 'Victoria, Yamagata', 'ssRNA (-) virus', 'Fever, cough, sore throat, runny nose, and muscle ache'),
(17, 'Human coronavirus HKU1', 'HCoV-HKU1', NULL, 'ssRNA(+) virus', 'Fever, nasal congestion, sore throat, and cough'),
(18, 'Legionella pneumophila', 'Legionnaires'' disease, Pontiac fever, Legionellosis', NULL, 'dsDNA bacterium', 'fever, headache, muscle ache, shortness of breath, and severe pneumonia'),
(19, 'Mycoplasma pneumoniae', 'Walking pneumonia, Mycoplasmoides pneumoniae', NULL, 'dsDNA bacterium', 'Causes common cold symptoms like fever, sore throat, fatigue, and a slowly worsening cough, sometimes leading to mild pneumonia'),
(20, 'Human coronavirus OC43', 'HCoV-OC43', NULL, 'ssRNA (+) virus', 'Fever, nasal congestion, sore throat, and cough'),
(21, 'Human orthorubulavirus 2', 'HPIV-2, PIV2, Parainfluenza virus type 2', NULL, 'ssRNA (-) virus', 'Causes fever, runny nose, cough and croup like PIV-1, but is usually associated with milder symptoms'),
(22, 'Human orthorubulavirus 4', 'HPIV-4, PIV4, Parainfluenza virus type 4', '4a, 4b', 'ssRNA (-) virus', 'Causes mild symptoms like low-grade fever, runny nose, and cough, usually less severe than PIV-1, PIV-2, and PIV-3'),
(23, 'Human metapneumovirus', 'HMPV', 'A1, A2, B1, B2', 'ssRNA (-) virus', 'Cough, fever, nasal congestion, and shortness of breath'),
(24, 'Human coronavirus 229E', 'HCoV-229E', NULL, 'ssRNA (+) virus', 'Fever, nasal congestion, sore throat, and cough'),
(25, 'Human respiratory syncytial virus A', 'HRSV-A, RSVA, Human orthopneumovirus A', NULL, 'ssRNA(-) virus', 'Runny nose, decrease in appetite, cough, and fever'),
(26, 'Human respiratory syncytial virus B', 'HRSV-B, RSVB, Human orthopneumovirus B', NULL, 'ssRNA(-) virus', 'Runny nose, decrease in appetite, cough, and fever');