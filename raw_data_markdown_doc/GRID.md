#GRID: 

##Data Cleaning Assessment:

This dataset originates from two GRID csv files ,grid.csv & type.csv, and I want to migrate into one. I will merge them in the Pandas' module by doing a left merge. After merging the two files, I will drop the grid_id, state, and city columns in PANDAS because they are not necessary for my final dataset. 

##Authorship: 

This dataset will have been created by Alex Wieker, which will have been modified from two GRID csv files. 


##Attribution: 

All of the data in this file comes from the GRID database provided by Digital Science. This database of information that describes institutional repositories around the world. Additionally, all of the data in this database is under a CC0 1.0 license, and access information may be found at: 
https://grid.ac/downloads

##Contents: 

This file describes the institutions that will be in my final dataset, such that it assigns a GRID id, institution name, a country, and institution type for each institution. For the purposes of my final dataset, I will be using the country and institution type data because that is what this data set is aiming to contribute to my final dataset. The GRID csv file sources of this dataset were collected in September 2018. 

##Collection: 

I downloaded the GRID database at: https://www.grid.ac. To create this dataset, I did a left join to on the grid.csv and types.csv, making a new dataset, grid_merge.csv. I then made an empty csv file, grid_curated.csv, where I was copy pasting the institution rows that are in my final dataset. Also, this dataset will be made with Excel.

##Description: 

This data file is in a csv file format. In this dataset there are four entities, GRID id's, country name's, institution name's, and institution type's entities. Each row will represent one institution from my final dataset, and this row will describe the name of an institution, what country it is located it, what type of institution it is (private or public), and it will have an assigned GRID identifier. I do not currently have the exact dimensions. Even though there are 425 institutions in DataCite, 100 in Harvard Dataverse, and 38 in OpenAire, there are overlaps, so the total institution count will not be the full 563. In any case, there will be about 500 rows, one for each institution in this dataset, and there will be 4 columns, one column for each entitity. There are text data types, number data types (integers), and categorical data in this dataset. These categories d

##Descriptions: 

###Institution Name Column (1):

This column names every single institution that will be present in my final dataset. It is a text data type value. There are no mising entities. This column comes from copy pasting every single institution in my dataset into this column. Also, there are no units for this data type.

###Name (2): 

This is a column from the GRID database, and these names how are GRID names the insitutions in my dataset.  Also, there are no units for this data type.

###Country Column (3):

This column describes what country each institution is located in. These data types are text data. There are missing elements because not every single institution in my dataset exists in the GRID database. Also, there are no units present in this column. 


###Institution Type Column (4): 

This column describes what each institution's type is. As such, this is categorical data. There are missing elements in this file because not every single institution in my dataset is present in the GRID database. Also, the GRID database does not distinguish between a library of a univeristy and the university itself, so I have changed any library type from education to archive because that is how GRID describes libraries. Also, I have changed some data repositories to other that GRID Does not have in their database because that is how GRID describes data repositories.  There are no units per se, but the categories have assigned meaning. Somple categories are education, government, non-profit, and company. These categories are rather self-explantory and mean what they suggest. 