#OpenAire

##Data Cleaning Assessment: 

At this stage, the OpenAire dataset file will require little cleaning. The only messy component of this dataset comes from one of the repository names not having a name, and it is assigned as unknown repository. I will need to decide how to address this. If I decide to remove this unknown repository from my dataset, then I will need to make a hand edit to remove it. Other than this, no data cleaning is required on this data file. 

##Authorship: 

This dataset has been created by Alex Wieker. The contents of this file came from the data center counts that may be seen in the OpenAire publication search feature. 

##Attribution: 

The content of this dataset comes from the metadata of datasets that have been ingested into OpenAire that were also published in 2017. Most of the datasets come from Zenodo and Figshare, but others come from a variety of institutional repositories around the world. All metadata ingested in OpenAire is under a 4.0 CC-By 4.0 license. Further information may be found on OpenAire: http://api.openaire.eu/oai-pmh.html. 

##Provenance: 

The contents of this dataset come from searching OpenAire's data repository at: https://explore.openaire.eu/search/find. Dataset DOI counts are able to be seen next to institution names, and this metadata comes from the OpenAire API, of which comes from metadata when items are ingested into OpenAire. 

##Contents: 

The OpenAire dataset describes what institutions contributed datasets to OpenAire that were published in 2017, and it also gives a count of how many datasets were contributed. All information is being used in this data file because my data set needs to know what institutions contributed datasets to OpenAire and how many datsets were contributed in the publication year 2017. All of this data was collected in the last week of October in 2018. 

##Collection Process: 

I collected this data by hand coding a csv file from information that is displayed on OpenAire's data repository search features provided at: https://explore.openaire.eu/search/find. I selected the Reseach Data Tab. Under type, I also selected Dataset. I then selected only 2017 under the publication year facet. I then hand copied all of the data underneath Content Provider, which is the various institutions that contributed datasets to OpenAire that were published in 2017. Lastly, I hand coded this data into Excel to create this dataset. 
  

##Structure: 

The structure of this dataset is a csv file that has 38 rows and 2 columns. As such, there are two entities, institutions and dataset contribution counts per institution. Each row represents one institution that contributed dataset(s) to OpenAire and the counts of how many datasets. There are 38 records in this file, one per each institution. The first column are text data types because they are the names of the institutions. The second column is a column of number data types (integers) because they are the number of counts of datasets contributed to OpenAire by each institution.

##Description:

###Institution Name Column (1):

This is a column that lists every single institutional repository that contributed dataset(s) that were published in 2017 to OpenAire. These data value are text, and there is only one missing value, which is the unknown repository. OpenAire did not assign a name to this repository. 

###Dataset DOI Count Column (2):

This column describes how many datasets each institution contributed to OpenAire that were published in 2017. These data values are numbers (integers), and there are no units present. There are also no missing values in this column. 


