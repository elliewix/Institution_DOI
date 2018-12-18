import requests
import os.path
import json
import time
import os

def get_datacenter_results(centerid, year): #
    centerclean = centerid.replace('.','-')     # get institution dataset data for the year 2017
    base = 'https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=' + centerid \
            + '&year=' + str(year)
    r = requests.get(base)
    maxpages = int(json.loads(r.text)['meta']['total-pages'])
    if maxpages > 100:  # set max page count
        maxpages = 100
    dirname = centerclean + 'results/'
    if os.path.exists(dirname):
        print('folder already exists', dirname)
    else:
        os.mkdir(dirname)
    for i in range(1, maxpages + 1):
        url = base + '&page[number]='+ str(i)
        fname = dirname + centerclean + str(i) + '.json'
        if os.path.exists(fname):
            print('already have', fname)
        else:
            r = requests.get(url)
            with open(fname, 'w') as fout:
                fout.write(r.text)
            print('got', fname)
            time.sleep(3)
    return base

with open('datacentersfull.txt', 'r') as fin:
    centers = [f.split(' -')[0] for f in fin.readlines()]   # cleaning file names

print(centers)

for center in centers:
    get_datacenter_results(center, 2017)