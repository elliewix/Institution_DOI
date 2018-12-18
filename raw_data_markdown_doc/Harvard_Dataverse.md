#Harvard Dataverse

##Data Cleaning Assessment: 

This dataset will require little cleaning because there is only two messy data values. As such, I will probably delete the Northeastern University / Harvard University row because it is unclear what institution that is being described. Also, Kings College London has a zero value even though it is inbetween the ten's, and if you click it, you see that there are ten datasets from them. I plan to replace this zero with a ten.

##Authorship: 

This dataset was created by Alex Wieker. It was created from metadata on the Hardvard Dataverse search page. 

##Attribution: 

The data in this file comes from metadata that Harvard Dataverse makes accessible on the search page of its data repository. The metadata itself comes from metadata of items, in this case datasets, that are ingested into Harvard Deverse. Also, all metadata is under a CC0 license, and additional information may be found at: http://guides.dataverse.org/en/4.2/api/. 

##Provenance: 

All of the data that I collected in this data file comes from the search page on Harvard Dataverse's data repository, which comes from its API, and the metadata in the API is the metadata that instiuttional repositories give Harvard Dataverse when they ingest digital objects (the dataset metadata).

##Contents: 

This dataset describes what institutions have contributed datasets to Harvard Dataverse that were published in 2017. Also, all data in this dataset is being used because I need to know the dataset submission DOI count per institution, so all data is pertinent. The data itself has not been collected yet, but it will be done in the time period of November 5th, 2018 - November 12th, 2018.

##Collection Process: 

To collect this data, I went to the search page of Harvard Dataverse's data repository: 
https://dataverse.harvard.edu/dataverse/harvard. I selected only Datasets on the top left,  and I selected only 2017 under the publication year facet. Lastly, under the author affiliation facet, I kept clicking more until I could see every single institution. I then hand coded this dataset in Excel based upon the DOI counts of datasets next to each institution. 

##Structure: 

This file is a csv file . There are two kinds of entities in this file. There are institution names with the text data type value that represent what institutions submitted datasets in the year 2017. There are also number entities with the integer data type value that describe how many datasets from the 2017 publication year each institution contributed to Harvard Dataverse. As such, each row describes how many datasets a given institution contributed to Harvard Dataverse in 2017. Since there are 100 institutions in this dataset, there are 100 rows and two columns (100 records). 

##Descriptions:

###Institution NAme Column (1): 

This column contains the names of institutions that have contributed datasets to Harvard Dataverse that were published in 2017. These data values are text data. Also, there are no units present, and there are no missing values in this column. 

###Dataset DOI Count Column (2): 

this column contains the counts of how many datasets these institutions contributed to Harvard Dataverse that were published in the year 2017. The data values of these are number values (integers), and there are no units present. There are also no known missing values; The numbers that are here are what is reported by Harvard Dataverse. 

