#DataCite

##Data Cleaning Assessment: 

Since DataCite metadata is very regulated with no missing values, I do not need to clean this dataset. However, I will need to clean my final dataset because institution names will probably overlap with different names. It should not take more than a few hours brecause I can clean it with OpenRefine's cluster feature. 

##Authorship: 

This dataset will have been created by Alex Wieker, which has been compiled from DataCite metadata. 


##Attribution: 

The metadata in this file has been pulled from Datacite's API, and the source fo the metadata from the API comes from the metadata of items that are ingested into Datacite. Additionally, all metadata on DataCite is under a CC0 license, and further information may be found on their website: https://support.datacite.org/docs/api. Lastly, attribution is due to Elizabeth Wickes becuase I used and modified her DataCite API code, which was how I was able to produce the data that utlimately make this file. 

##Provenance: 

The data in this dataset comes from DataCite's API, which comes from the metadata of ingested items. 

##Contents: 

This dataset describes what institutions contributed datasets to DataCite that were published in 2017, and it also describes how many datasets were contributed by each institution. Since I am making this dataset, it will already be curated from the full metadata that I got from the API. As such, this dataset will have institution names and coresponding dataset counts, which I will utilize in my final dataset.  Some sampling collection was completed in the last two weeks of October and on November 3rd in 2018. However, I will be overriding that data when I run my code on November 4, 2018 because many new queries were added to my code. 
I should also note that some items will have registration dates and publication dates because of embargos.

##Collection Process:

To collect this data, I first identified the data center id's, which may be found on the DataCite Statistics page: https://stats.datacite.org/#tab-datacentres. I then made queries for each data center id with the publication year 2017 and had the type of dataset. I then copied what queries had results into a txt file where I then added these queries to my DataCite_API py file, which I had modified from code that Elizabeth Wickes had distributed to our class. In my DataCite_API py file, it runs all of the queries and outputs the data into json files. I used my DataCite_API.py script to get all of the institution pages from 1-40, and I used DataCite_API_pages(41-100).py to get all of the page numbers from 41-100 if it went that high. In the end, I collected up to 100 sample pages from each institution, only about thirty institutions went above 41 pages.

##Structure: 

The data is in a csv file format. There are two kinds of entities in this dataset, institution names and dataset counts for each institution. Under the first column of each row, it will give the name of the institution with a text data type and under the second column it will give a number value data type (integer) that describes how many datasets that institution has given to DataCite that were published in 2017. Since there are 425 institution this dataset, there will be 425 rows and many columns. 


##Descriptions:

###Institution Name Column: 

This column contains the names of each institution that contributed datasets to DataCite that were published in 2017. There are no units present and the data values are text data. There are no missing values within this column because all known institution id's are known quantities. I handcoded this names, so they would match corresponding institution codes

###Institution Code Column:

These are string codes that were from the json. They will be dropped in Pandas and replaced by the Institution Name Column. This column is a DOI count of my sample collection. There are no missing values or data units.


###Dataset DOI Count Column: 

This column contains number data values (integer) that describe how many datasets that institution in the corresponding row has contributed to DataCite that were also published in 2017. For example, if a data center has the number three in this column, then that data center contributed three datasets do DataCite that were published in 2017. Each number in this column represents that many datasets. As such, there are no units assigned in this column. Also, there are no missing values in this column because all measurements are based on known quantities. 

###Sample DOI Count Colum:

This column is a DOI count of my sample collection. There are no missing values or data units. There are no missing values.

###Publication Year Column:

This column describes the year of data collection for row. This is a integer number with no units. There are no missing values.

###2017 & 2018 Registration Year:

These two columns give a count of how many dois each institution had for the 2017 & 2018 registration year respectively. There may be missing values because this field is not always used. 

###Data Source:

I hand coded this column in Excel to describe what data repository each row came from. There are no missing values, and this is a string data type. There are no missing values.


###Regional Aggeregator:

This column describes where each institution aggregates their data. There are no missing values, and this is a string data type. There are no missing values.

###CC Licenses:
 
This column gives a count of how many of each license in my dataset a given institution uses. There may be missing value because not every institution uses every single license. This is a string data type. I ended up dropping these from my final dataset because I had transformed these columns incorrectly in Pandas.

###Resource Type:

This column describes the resource's that each institution contributed to this dataset. There are no missing values, and this is a string data type. There are no missing values.

###Resource Type Count:

This column is a count of the resource type to see if anything is off. There are no missing values and it is a string data type.

###Subresourcetypes

There are many columns in this data file that describe the subresource types that each institution have used to describe their datasets. There are many missing values because not every single institution used every sub resource type. This is a integer data type. 


