import json
import glob
import csv

# load in all files in directory that end with json

path = glob.glob('/Users/sender/PycharmProjects/IS590_ODM/**/*.json', recursive=True)


# make an empty list to loop over all of the files that end with json

allrows = []

for file in path:
    infile = open(file, 'r')
    text = infile.read()
    infile.close()

    try:
         data = json.loads(text)

    except:
        print('failed on', file)
        continue

    try:    # Python was failing on one record, but the record is still in my output. Extract the data element.
        records = data['data']

    except:
        continue
    # extracting total doi count per institution in 2017.
    total = data['meta']['total']
    doicount = str(total)

    # loop over records to extract wanted elements.
    for record in records:
        row = []
        pubyear = record['attributes']['published']  # publication date
        doi = record['attributes']['doi']  # individual doi's
        regyear = record['attributes']['registered']  # registration date
        regyear = regyear.split('-')
        regyear = regyear[0]
        resourcetype = record['attributes']['resource-type-id']  # resource type
        subresourcetype = record['attributes']['resource-type-subtype']  # subresource type
        license = record['attributes']['license']  # licensing information
        institutioninformation = record['attributes']['data-center-id']  # ['container-title'] institution information
        clean_institutioninformation = institutioninformation.split('.')
        institution = clean_institutioninformation[1]   # institution name
        aggregator = clean_institutioninformation[0]    # regional data aggregator
        row.append(pubyear)
        row.append(doicount)
        row.append(doi)
        row.append(regyear)
        row.append(resourcetype)
        row.append(subresourcetype)
        row.append(license)
        row.append(institution)
        row.append(aggregator)
        allrows.append(row)

    # write out data to csv file

    headers = ['pubyear', 'doicount', 'doi', 'regyear', 'resourcetype', 'subresourcetype', 'license', \
               'institutioncode', 'aggregator']

    with open('DataCite_Doi.csv', 'w', newline='') as outfile:
        csvout = csv.writer(outfile)
        csvout.writerow(headers)
        csvout.writerows(allrows)




