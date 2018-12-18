#Manifest File

##raw_data_README.md:

Readme file that describes how to access my raw data.

##Requirements.txt: 

All of the needed modules to create my final data file.

##final_institution_doi_reproducible_JupyterNotebook.ipynb:

Reproducible notebook that walks through joining my intermediate data files.

##final_institution_doi_assessment_report.pdf:

An assment of the value of my final dataset. 

##DataCite.md:

Markdown file that descirbes my DataCite data file.

##GRID.md:

Markdown file that describes my GRID data file.

##Harvard_DataVerse.md: 

Markdown file that describes my GRID data file.

##OpenAire.md:

Markdown file that desicirbres my OpenAire data file.

##Wieker_summary_slide.pptx:

Powerpoint that describes the goals and processes of my dataset project.

##resume_excerpt.pdf:

An excerpt of what this dataset looks like in my Resume.

##original_DataCite_data (folder):

A folder that contains a set of folders, which each contain the json data for each institution from DataCite.

##DataCite_API.py: 

Accessing DataCite API for institution pages 1-40.

##DataCite_API_pages(41-100).py:

Accessing DataCite API for institution pages 41-100 if they existed.

##datacentersfull.txt:

Supplemental file for DataCite_API_pages(41-100).py, which is used to access institution names

##DataCite_csvconvert.py:

Extract & convert DataCite data to a csv file.

##DataCite_Doi.csv:

File that was created by DataCite_csvconvert.py; It is the elements that I extracted my raw data.

##curated_DataCite_doi:

The csv file that I created from my DataCite_agg.py script.

##curated_DataCite_doi_2.0.csv:

I made some hand eidts of my curated_DataCite_doi csv file. I added a column next to institution codes, which was a list of institution names that corresponded to the codes. This is the data file that I used for my jupyter notebook.

##DataCite_agg.py:
Py file to aggregate the DataCite_Doi.csv file by institution.

##grid.csv:

Main GRID database file that describes institutions.

##types.csv

supplemental GRID database file that describers institution types.

##grid_merge.py:

Merge GRID database files, so I have a file to show institution location and type.

##grid_merge.csv:

Merged GRID database that shows institution location and type.

##grid_curated.csv:

Only contains institutions from the grid_merge.csv file that are from my collected data.

##DataVerse_screenshot_1: 

Screenshot 1 of the query I did in DataVerse's repository to get dataset metadata.

##DataVerse_screenshot_2:

Screenshot 2 of the query I did in DataVerse's repository to get dataset metadata.

##DataVerse_doi.csv:

I handcoded this file from the dataset 2017 publication information that was available on DataVerse's repository.

##curated_DataVerse_doi:

I curated my DataVerse_doi.csv file, and this is the file that is read into my jupyter reproducible notebook.

##OpenAire_doi.txt:

I copy pasted all of the dataset 2017 publication dataset data that is present on their search repository page.

##OpenAire_screenshot:

screenshot of what OpenAire looked like when I copy pasted the publication data.

##OpenAire_doi.csv:

Handcoded csv from OpenAire_doi.txt.

##curated_OpenAire_doi.csv:

I curated my OpenAire_doi.csv file, and this is the file that is read into my jupyter reproducible notebook.

##institution_doi.csv:

Merged curated_DataCite_doi_2.0.csv, curated_DataVerse_doi.csv, curated_OpenAire_doi.csv, and grid_curated.csv into one data file.

##cleaned_institution_doi.csv:

Cleaned up some duplicate rows from institution_doi.csv.

##final_institution_doi.csv:

Final dataset; did some more cleaning (removed incorrect license information and reset index).



