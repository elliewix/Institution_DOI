import pandas as pd

# read in the DataCite csv file

DCdf = pd.read_csv("DataCite_Doi.csv")

# aggregate doicount by institution

doi_df = DCdf.groupby('institutioncode', as_index=False).doicount.max().rename(columns={'doicount': 'DOI Count'})

# aggregate  sample doi count by institution

doisample_df = DCdf.groupby('institutioncode', as_index=False).doi.count().rename(columns={'doi': 'Sample Doi Count'})

# merge doi count and sample doi count

DCdf_merge = pd.merge(doi_df, doisample_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])
# aggregate publication year and registration year by institution and unstack it into their own column names
# only interested in 2017 and 2018, so dropping other years

regyear_df = DCdf.groupby(['institutioncode','pubyear','regyear'], sort=False).size().unstack().reset_index().rename_axis(None, axis=1)
regyear_df = regyear_df.drop(columns=[2016,2015,2014,2013,2012,2011])
regyear_df = regyear_df.rename(columns={2017:'2017 Reg Year', 2018: '2018 Reg Year'})
regyear_df = regyear_df.rename(columns={'pubyear':'Publication Year'})

# merge df's

DCdf_merge2 = pd.merge(DCdf_merge, regyear_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])
DCdf_merge2['Data Source'] = 'DataCite'

# group by regional aggregator

aggregator_df = DCdf.groupby(['institutioncode'], as_index=False).aggregator.max().rename(columns={'aggregator':'Regional Aggregator'})
# merge df's

DCdf_merge3 = pd.merge(DCdf_merge2, aggregator_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])

# aggregate license data by institution and unstack
license_df = DCdf.groupby(['institutioncode','license'], sort=False).size().unstack().reset_index().rename_axis(None, axis=1)

# make new column names and drop old ones

license_df['CC0'] = license_df['https://creativecommons.org/publicdomain/zero/1.0/'] + license_df['https://creativecommons.org/licenses/publicdomain/zero/1.0/'] + license_df['https://creativecommons.org/share-your-work/public-domain/cc0/'] + license_df['https://creativecommons.org/choose/zero/']
license_df['CC Public Domain'] = license_df['https://creativecommons.org/publicdomain/mark/1.0/']
license_df['CC BY'] = license_df['https://creativecommons.org/licenses/by/3.0/'] + license_df['https://creativecommons.org/licenses/by/4.0/deed.de/'] + license_df['https://creativecommons.org/licenses/by/4.0/'] + license_df['https://creativecommons.org/licenses/by/3.0/us/'] + license_df['https://creativecommons.org/licenses/by/3.0/au/'] + license_df['https://creativecommons.org/licenses/by/3.0/de/deed.de/'] + license_df['https://creativecommons.org/licenses/by/4.0/deed.en_US/']
license_df['CC BY-SA'] = license_df['https://creativecommons.org/licenses/by-sa/3.0/'] + license_df['https://creativecommons.org/licenses/by-sa/4.0/'] + license_df['https://creativecommons.org/licenses/by-sa/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-sa/4.0/'] + license_df['https://creativecommons.org/licenses/by-sa/4.0/deed.de/']
license_df['CC BY-NC'] = license_df['https://creativecommons.org/licenses/by-nc/4.0/'] + license_df['https://creativecommons.org/licenses/by-nc/3.0/']
license_df['CC BY-ND'] = license_df['https://creativecommons.org/licenses/by-nd/3.0/'] + license_df['https://creativecommons.org/licenses/by-nd/4.0/'] + license_df['https://creativecommons.org/licenses/by-nc/3.0/us/']
license_df['CC BY-NC-SA'] = license_df['https://creativecommons.org/licenses/by-nc-sa/3.0/'] + license_df['https://creativecommons.org/licenses/by-nc-sa/4.0/'] + license_df['https://creativecommons.org/licenses/by-nc-sa/3.0/us/']
license_df['CC BY-NC-ND'] = license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/4.0/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/3.0/us/'] + license_df['https://creativecommons.org/licenses/by-nc-nd/4.0/deed.de/']
license_df['CC GPL'] = license_df['https://opensource.org/licenses/GPL-2.0'] + license_df['https://opensource.org/licenses/GPL-3.0']
license_df['CC MIT'] = license_df['https://opensource.org/licenses/MIT']
license_df['CC BSD'] = license_df['https://opensource.org/licenses/BSD-3-Clause'] + license_df['https://opensource.org/licenses/BSD-2-Clause']
license_df['CC NPOSL'] = license_df['https://opensource.org/licenses/NPOSL-3.0']
license_df['CC Zlib'] = license_df['https://opensource.org/licenses/Zlib']
license_df['CC Unspecified'] = license_df['https://creativecommons.org/']
license_df = license_df.drop(columns=['https://creativecommons.org/','https://opensource.org/licenses/Zlib', 'https://opensource.org/licenses/NPOSL-3.0', 'https://opensource.org/licenses/BSD-2-Clause', 'https://opensource.org/licenses/BSD-3-Clause', 'https://creativecommons.org/publicdomain/mark/1.0/', 'https://opensource.org/licenses/MIT','https://creativecommons.org/licenses/by-nc-nd/3.0/', 'https://creativecommons.org/licenses/by-sa/3.0/', 'https://opensource.org/licenses/GPL-2.0', 'https://opensource.org/licenses/GPL-3.0', 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'https://creativecommons.org/licenses/by-nd/3.0/','https://creativecommons.org/licenses/by-nd/4.0/','https://creativecommons.org/licenses/by-nc/3.0/us/', 'https://creativecommons.org/licenses/by-nc-sa/4.0/', 'https://creativecommons.org/licenses/by-nc-sa/3.0/us/', 'https://creativecommons.org/licenses/by/3.0/us/', 'https://creativecommons.org/licenses/by/4.0/', 'https://creativecommons.org/licenses/by/3.0/au/', 'https://creativecommons.org/licenses/by/3.0/de/deed.de/', 'https://creativecommons.org/licenses/by/4.0/deed.en_US/', 'https://creativecommons.org/licenses/by-nc/4.0/', 'https://creativecommons.org/licenses/by-nc/3.0/', 'CC BY-SA','https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by-sa/3.0/us/', 'https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by-sa/4.0/deed.de/', 'https://creativecommons.org/licenses/by/4.0/deed.de/', 'https://creativecommons.org/licenses/by-nc-nd/4.0/deed.de/', 'https://creativecommons.org/licenses/by-nc-nd/3.0/us/', 'https://creativecommons.org/licenses/by-nc-sa/3.0/', 'https://creativecommons.org/publicdomain/zero/1.0/', 'https://creativecommons.org/licenses/publicdomain/zero/1.0/', 'https://creativecommons.org/share-your-work/public-domain/cc0/' , 'https://creativecommons.org/choose/zero/', 'https://creativecommons.org/licenses/by/3.0/'])

# merge df's

DCdf_merge4 = pd.merge(DCdf_merge3, license_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])

# only one resource type so group by institution code and using max to show the one type

resourcetype_df = DCdf.groupby('institutioncode', as_index=False).resourcetype.max().rename(columns={'resourcetype': 'Resource Type'})

# merge df's

DCdf_merge5 = pd.merge(DCdf_merge4, resourcetype_df, how='left', left_on = ['institutioncode'], right_on = ['institutioncode'])

# count resource type incase some things don't match up

resourcetypecount_df = DCdf.groupby(['institutioncode','resourcetype'], sort=False).size().unstack().reset_index().rename_axis(None, axis=1).rename(columns={'dataset': 'Resource Type Count'})

# merge df's

DCdf_merge6 = pd.merge(DCdf_merge5, resourcetypecount_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])

# aggregate subresourcetype by institution and unstack into new columns. removing dirty ftp data.

subresourcetype_df = DCdf.groupby(['institutioncode','subresourcetype'], sort=False).size().reset_index()
filter_ftp = subresourcetype_df[subresourcetype_df['subresourcetype'].str.contains("ftp://")]
replace_ftp = subresourcetype_df.replace(filter_ftp, 'missing URL')
replace_ftp
cleaned_subresourcetype_df = replace_ftp.groupby(['institutioncode', 'subresourcetype'], sort=False).size().unstack().reset_index().rename_axis(None, axis=1)

# merge df's

DCdf_merge7 = pd.merge(DCdf_merge6, cleaned_subresourcetype_df, how='left', left_on=['institutioncode'], right_on=['institutioncode'])
DCdf_merge7.index = DCdf_merge7.index + 1
DCdf_merge7 = DCdf_merge7.rename(columns={'institutioncode': 'Institution Name'})

# write out the aggregated DataCite data

DCdf_merge7.to_csv('curated_DataCite_doi.csv')

