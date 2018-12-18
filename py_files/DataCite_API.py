import requests
import time



def DataCite_API():

    institution = "Scholars Portal/"    # set a folder name for each institution

    for i in range(1, 10):  # loop through all of the page URL's for each institution and write them out as file foldedrs
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.osp&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Natural Resources Canada/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.nrcan&nrc=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The McConnell Brain Imaging Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.neuro&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Canadian Polar Data Network (CPDN)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.ipy&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Hakai Institute/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.hakai&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Dalhousie University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.dal&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Canadian Cryospheric Information Network/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.ccin&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Biodiversity Institute of Ontario/"

    for i in range(1, 11):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.bold&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ArcticNet/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.an&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Agriculture and Agri-Food Canada/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.aafc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CERN-ZENODOresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cern.zenodo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CERN OpenData Portal/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cern.opendata&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "inspirehep net/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cern.inspire&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Virginia Tech Transportation Institute/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.vtti&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Utah/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.uutah&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Utah State University Merrill-Cazier Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.usu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of New Mexico Libraries/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.unmlib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSF Clinical & Translational Science Institute (CTSI)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucsfctsi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSD/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucsd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSC/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucsc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSB Advanced Graphics Lab/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucsbagl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSB/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucsb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UC Riverside/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UC Merced/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UC Irvine Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.uci&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CDL-UCDIRLresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucdirl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of California, Davis, University Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucdavis&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Collaborative Research in Computational Neuroscience (CRCNS)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucbcrcns&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UC Berkeley/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ucb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Alberta Libraries/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ual&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Texas Advanced Computing Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.tacc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Harvard Medical School/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.sbgrid&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Sage Bionetworks/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.sagebio&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Rutgers University Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.rutgers&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CDL-R2Rresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.r2r&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Pitt Quantum Repository/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.pqr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Pittsburgh/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.pitt&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Partnership for Interdisciplinary Studies of Coastal Oceans (PISCO)/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.pisco&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UTA Petroleum Engineering/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.pgerr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Odum Institute for Research in Social Science/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.odumunc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Snow and Ice Data Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.nsidc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "FIGSHARE-NSFresults/"

    for i in range(1, 101):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.nsfadc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Center for Ecological Analysis and Synthesis (NCEAS)/"

    for i in range(1, 13):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.nceas&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Center for Atmospheric Research (NCAR)/"

    for i in range(1, 15):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ncar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "MorphoBank/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.morphoba&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "MIT Laboratory of Computational Physiology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.mitlcp&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UNC Library - Resource Description and Management/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.libunc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Johns Hopkins University Data Archive/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.jhu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Incorporated Research Institutions for Seismology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.iris&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "iPlant Collaborative (at University of Arizona)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.iplant&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Marine and Coastal Research Institute of Columbia/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.invemar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UCSF ImmPort/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.immport&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Interdisciplinary Earth Data Alliance/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ieda&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "International Crops Research Institute for the Semi-Arid Tropics (ICRISAT)/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.icrisat&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Fred Hutchinson Cancer Research Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.fhcrc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Dublin Institute of Technology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.dit&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Drug Design Data (D3R) Resource/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.d3r&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Columbia University Libraries Information Services (CUL IS)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.culis&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Cornell University Library/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.cul&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Carnegie Mellon University Libraries/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.cmu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Potato Center/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.cip&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Center for International Earth Science Information Network (CIESIN)/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.ciesin&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "California Digital Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.cdl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Climate, Atmospheric Science and Physical Oceanography/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cdl.caspo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Caltech Library/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=caltech.library&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Brown Digital Repository/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=brown.bdr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Ulster University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.ulster&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UK Data Archive/"

    for i in range(1, 39):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.ukda&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of East London/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.uel&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Surrey/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.surrey&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Strathclyde/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.strath&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Science and Technology Facilities Council/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.stfc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of St Andrews/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.standrew&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Southampton/"

    for i in range(1, 31):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.soton&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Sheffield/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.shef&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Sir Alister Hardy Foundation for Ocean Science/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.sahfos&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Royal Society of Chemistry/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.rsc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Rothamsted Research/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.rothres&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Royal Holloway, University of London/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.rhul&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Queen's University Belfast/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.qub&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Queen Mary University of London/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.qmul&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Portsmouth/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.portsmth&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Plymouth University/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.plymouth&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Oxford University Library Service Databank/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.oxdb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The Open University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.open&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Natural History Museum, London/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.nhm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Natural Environment Research Council/"

    for i in range(1, 18):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.nerc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Edinburgh Napier University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.napier&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Manchester Metropolitan University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.mmu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "BL-MENDELEYresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.mendeley&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Middlesex University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.mdx&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Marine Institute/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.marineie&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "London School of Hygiene and Tropical Medicine/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.lshtm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Liverpool/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.lpool&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Leeds/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.leeds&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Loughborough University/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.lboro&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Lancaster/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.lancs&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Keele University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.keele&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "King's College London/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.kcl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "BL-IMPERIALresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.imperial&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Heriot-Watt University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.hwu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Hertfordshire/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.herts&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Sheffield Hallam University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.hallam&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Glasgow/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.glasgow&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Faculty of 1000 Research Ltd/"

    for i in range(1, 15):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.f1000r&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Exeter/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.exeter&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Essex/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.essex&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Edinburgh/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.ed&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Durham University/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.durham&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Dundee/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.dundee&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Cefas/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.cefas&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Cardiff University/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.cardiff&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Cambridge/"

    for i in range(1, 18):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.cam&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Brunel University London/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.brunel&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Bristol/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.bristol&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Birkbeck, University of London/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.birkbeck&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Birmingham/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.bham&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Bath/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.bath&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Aston University/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.aston&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Cranfield University/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.cran&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Archaeology Data Service/"

    for i in range(1, 14):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.ads&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Aberdeen/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bl.abdn&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UNINETT Sigma AS, Norway/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.uninett&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DataverseNO/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.uit-ord&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NSD – Norsk senter for forskningsdata/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.nsd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Norsk Polarinstitutt/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.npolar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Norwegian Marine Data Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.nmdc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NILU - Norsk institutt for luftforskning/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.nilu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The Norwegian Institute of Bioeconomy Research/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=bibsys.nibio&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of New England/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre95&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Agriculture Victoria/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre92&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Australian Data Archive/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre87&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Flinders University Library Research Data/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre86&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Victoria University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre80&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of South Australia/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre78&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Tasmania/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre77&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Edith Cowan University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre75&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "RMIT University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre61&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Technology, Sydney/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre59&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Bond University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre57&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The University of Adelaide/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre55&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of New South Wales/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre53&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Analysis and Policy Observatory/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre50&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The University of Melbourne/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre49&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Southern Cross University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre47&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Computational Infrastructure/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre41&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of the Sunshine Coast/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre39&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Western Sydney University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre35&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "James Cook University/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre28&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Swinburne University of Technology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre27&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ANDS-CENTRE25results/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre25&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The University of Western Australia/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre23&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "La Trobe University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre22&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Deakin University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre16&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Sydney Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre11&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Queensland University of Technology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre-9&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Curtin University/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre-6&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ANDS-CENTRE-3results/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre-3&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Griffith University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.centre-1&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Australian Institute of Marine Science (AIMS)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.c175&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NSW Office of the Environment and Heritage/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.c163&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Central Queensland University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.c145&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Federation University Australia/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ANDS.C122&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of South Queensland/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ands.c113&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


    institution = "Ocean Tracking Network/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.otndc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Simon Fraser University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.sfu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CybelePress/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.tpoder&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of British Columbia/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.ubc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Université de Montréal Biodiversity Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.udembc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Guelph/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.ugardr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Manitoba Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.umanlib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Ottawa/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.uottawa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Prince Edward Island/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cisti.upei&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Climate Adaptation Science Centers/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=climsc.csc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CMCC Foundation - Ocean Predictions and Applications Division/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cmcc.opa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "GigaDB/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cngb.gigadb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CISER Data Archive/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cornell.ciser&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "African Population and Health Research Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.aphrc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Istituto Nazionale di Geofisica e Vulcanologia/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.ingv&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Istituto Nazionale di Oceanografia e di Geofisica Sperimentale/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.ogsts&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Università degli Studi di Bologna/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unibo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(2)

    institution = "University of Calabria/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unical&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Università degli Studi di Catania/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unict&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Salento/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unile&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Università degli Studi di Milano-Bicocca/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unimib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Università degli Studi di Torino/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=crui.unito&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(2)

    institution = "CSC - IT Center for Science/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=csc.csceudat&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CSIC-DIGITALresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=csic.digital&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Infraestructura Mundial de Información en Biodiversidad/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=csic.gbif&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


    institution = "CGA/"

    for i in range(1, 12):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cngb.cga&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CYBERL-CYBERDOIresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=cyberl.cyberdoi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DataFirst Client/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dafi.client&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CRAWDAD/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dartlib.crawdad&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Axiom Data Science/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=datacite.axiom&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


    institution = "DATACITE-GTEXresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=datacite.gtex&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DATACITE-TOPMEDresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=datacite.topmed&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Wyoming/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dcco.wyoming&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Belgian Institute for Space Aeronomy/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.bira&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "4TU Centre for Research Data/"

    for i in range(1, 20):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.data4tu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DELFT-EASYresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.easy&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "European Commission Joint Research Centre Directorate G/"

    for i in range(1, 21):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.jrc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "KNMI Data Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.knmi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "MAASTRO Clinic/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.maastro&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "SURFsara/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.surfsara&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universiteit Utrecht/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.uu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universiteit van Amsterdam/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.uva&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Vlaams Instituut voor de Zee/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=delft.vliz&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Aalborg University Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.aau&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DTIC Datacente/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.dtic&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DK-GBIFresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.gbif&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "SiB Colombia/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.gbif-co&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The State Archives/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.sa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Statsbiblioteket/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dk.sb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)

    institution = "Landcare Research New Zealand Ltd/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=doinz.landcare&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Auckland Data Publishing and Discovery Service/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=doinz.nzau&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DRYAD-DRYADresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=dryad.dryad&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "EDI-EDIresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=edi.edi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Earth Observing System Data and Information System/"

    for i in range(1, 37):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=esdis.eosdis&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Plutof Data Management and Publishing Platform/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=estdoi.bio&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Qsardb Databank/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=estdoi.qdb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DataDOI/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=estdoi.repo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ETHZ Data Archive - Research Data/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ethz.da-rd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "IUMSP: Data/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ethz.iumspdat&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "SICAS/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ethz.sicas&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "World Glacier Monitoring Service/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ethz.wgms&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Swiss Federal Institute for Forest, Snow and Landscape Research WSL/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ethz.wsl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Publications Office of the European Union/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=europ.data&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "FIGSHARE-ARSresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.ars&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "figshare ASHA Publications/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.asha&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Cape Peninsula University of Technology/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.cput&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "US Environmental Protection Agency/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.epa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Janelia/"

    for i in range(1, 15):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.janelia&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Figshare Datacite/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.orcid&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "St Edwards University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.stedward&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Sussex/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.sussex&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Figshare test Datacenter/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.test&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Cape Town (UCT)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.uct&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University College of Southeast Norway/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.usn&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Utrecht University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.uu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Western Cape/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=figshare.uwc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "GDCC-HARVARD-DVresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gdcc.harvard-dv&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Harvard Medical School Sleep Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gdcc.harvard-slp&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Syracuse University Qualitative Data Repository/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gdcc.syr-qdr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Austrian Social Science Data Archive/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.aussda&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Forschungsdaten- und Servicezentrum der Bundesbank/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.db-bank&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Forschungsdatenzentrum Deutsches Zentrum für Altersfragen (FDZ-DZA)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.deas&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Data Service Center for Business and Organizational Data/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.dsz-bo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Swiss Center for Expertise in Social Research/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.fors&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "GESIS Leibniz Institute for the Social Sciences/"

    for i in range(1, 13):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.gesis&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Histarch - Historische Archäologie/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.histarch&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Human Science Research Council SA/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.hsrc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "GESIS-ICPSRresults"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.icpsr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Ifakara Health Institute/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.ihi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "INDEPTH Network/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.indepth&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institut zur Qualitätsentwicklung im Bildungswesen/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.iqb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Nationales Bildungspanel (National Educational Panel Study, NEPS)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.neps&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Health Monitoring Research Data Centre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.rki&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "SHARE - ERIC/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.share&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Forschungsdatenzentrum Sozio-ökonomisches Panel (FDZ SOEP)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.soep&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Survey Research Data Archive Taiwan/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.srda&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University Library Heidelberg/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.ubhd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UBMA/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.ubma&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University Library Vechta"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.ubve&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Wissenschaftszentrum Berlin für Sozialforschung/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.wzb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "GESIS ZPID/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=gesis.zpid&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "IEEE DataPort/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=ieee.dataport&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "AERIS - Pôle français de données et services pour l'atmosphère/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.aeris&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Collaborating Academics/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.ca&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Socio-political data center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.cdsp&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Center for International Cooperation in Agricultural Research for Development/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.cirad&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Editions of contemporary archives/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.eac&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Ecole et observatoire des sciences de la terre/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.eost&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institut Français de Recherche pour l'Exploitation de la Mer/"

    for i in range(1, 9):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.ifremer&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institut International du Froid/"

    for i in range(1, 11):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.iif&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institut National de Recherche Agronomique/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.inra&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


    institution = "Institut Pierre-Simon Laplace/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.ipsl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institut de Recherche pour le Développement/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.ird&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Laboratoire ATmosphères, Milieux, Observations Spatiales/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.latmos&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Observatoire Midi-Pyrénées/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.omp&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Observatoire des Sciences de l'Univers de Grenoble/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.osug&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Observatoire des Sciences de l'Univers Terre Homme Environnement Temps Astronomie de Franche-Comté Bourgogne/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.osutheta&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Observatoire Terre Environnement de Lorraine/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.otelo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "INIST-SHOMresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.shom&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University Paul-Valéry Montpellier 3/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=inist.upvm3&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Indiana University Bloomington Libraries/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=iu.bl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Japan Link Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=jalc.jalc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Japan Link Center/"

    for i in range(1, 15):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=madrono.cm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "OpenBioMaps Consortium/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=mtakik.obiomap&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "MTAKIK-RESPECTHresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=mtakik.respecth&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Global Monitoring Division/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=noaa.gmd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Oceanic and Atmospheric Administration (NOAA) National Centers for Environmental Information (NCEI)/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=noaa.ncei&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Oceanic and Atmospheric Administration (NOAA) NCEI and NCL/"

    for i in range(1, 10):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=noaa.ncei-ncl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NRCT Data Center/"

    for i in range(1, 24):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=nrct.db1&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "SAEON Data Centre/"

    for i in range(1, 14):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=nrf.saeon&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National University of Singapore/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=nus.sb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "New York University Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=nyu.library&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Northwest Knowledge Network/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=orbis.nkn&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Oregon State University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=orbis.osu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Oregon/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=orbis.uoregon&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Washington Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=orbis.uwl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Oak Ridge National Laboratory Distributed Active Archive Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=orbis.uwl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "AMES Laboratory/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.ames&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Argonne National Lab/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.anl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Office of Science (SC)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.bgc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Coherent X-ray Imaging Data Bank/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.cxidb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DOE Generic/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.doe&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DOE Geothermal Data Repository/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.doegdr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Transportation Library, US Department of Transportation/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.dotntl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Environmental Protection Agency/"

    for i in range(1, 11):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.epa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Information Marketplace for Policy and Analysis of Cyber-Risk & Trust (IMPACT)/"

    for i in range(1, 6):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.impact&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "OSTI-LBNLresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.lbnl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DOE Marine and Hydrokinetic Data Repository/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.mhkdr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Aeronautics and Space Administration - Planetary Data System (NASA-PDS)/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.nasapds&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NETL Energy Data eXchange (EDX)/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.netledx&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Institutes of Health, National Institute of Mental Health/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.nimh&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Institutes of Standards and Technology/"

    for i in range(1, 5):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.nist&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Renewable Energy Laboratory (NREL)/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.nrel&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Oak Ridge National Laboratory - Atmospheric Radiation Measurement (ARM) Data Archive/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.ornlarm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "NGEE-Arctic (Next Generation Ecosystems Experiement)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.ornlngee&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Pacific Northwest National Laboratory/"

    for i in range(1, 9):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.PNNL&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Oak Ridge National Lab’s Terrestrial Ecosystem Science Scientific Focus Area/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.tessfa&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "US Department of Agriculture, Agricultural Data Commons/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=osti.usdaadc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Alliance for Crops, Soils, and Environmental Science Societies/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.acsess&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Adaptive Biotechnologies/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.adaptive&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Data Repository for the University of Minnesota/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.drum&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Purdue University/"

    for i in range(1, 12):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.ezid&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "IPUMS/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.ipums&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institute for Research on Innovation and Science/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.irisink&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Univ Chicago Materials Data Facility/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.mdf&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "National Cancer Informatics Program Hub, NIH/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.nciph&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Nanyang Technological University/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.ntu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Northwestern University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.nul&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Penn State Institutes of Energy and the Environment PSU Data Commons/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.psiee&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Illinois Libraries/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.uiuclib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Maryland Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.umd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Michigan Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.umich&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Nebraska-Lincoln Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.unl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UW-Biological Magnetic Resonance Bank/"

    for i in range(1, 29):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.uwbmrb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "PURDUE-UWISCresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=purdue.uwisc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "RG-RGresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=rg.rg&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Kinder Institute/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=rice.kinder&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Smithsonian Institution/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=si.si&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "TalkBank/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=sml.talkbank&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "The Cancer Imaging Archive/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=sml.tcia&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Digital Antiquity (TDAR)/"

    for i in range(1, 8):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=sml.tdar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "DataGuru-LU, Department of Physical Geography and Ecosystem Science, Lund University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.dataguru&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Demographic Data Base/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.ddb&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Environment Climate Data Sweden/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.ecds&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ICOS Carbon Portal/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.icos&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Swedish National Data Service/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.snd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Stockholm University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=snd.su&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Journal «Theoretical and applied ecology»/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=spbpu.o-kratkoe&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Barbara A Mikulski Archive for Space Telescopes/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=stsci.mast&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Digital Research Infrastructure for the Arts and Humanities/"

    for i in range(1, 15):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=subgoe.dariah&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Stanford Digital Repository/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=sul.sdr&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)



    institution = "Gulf of Mexico Research Initiative Information and Data Cooperative/"

    for i in range(1, 19):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tdl.griidc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Texas Digital Library/"

    for i in range(1, 8):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tdl.tdl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Romania ADL Association/"

    for i in range(1, 12):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.adlnet&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


    institution = "Leibniz-Institut für Astrophysik Potsdam (AIP)/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.aip&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Apeiron WSBPI/"

    for i in range(1, 7):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.apeiron&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Beilstein-Institut zur Förderung der Chemischen Wissenschaften/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.beilst&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Deutsches Zentrum für Luft- und Raumfahrt/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.dlr-eoc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Deutscher Wetterdienst - Klimaüberwachung/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.dwd&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "EARSeL eProceedings, University of Oldenburg/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.earsel&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "EEUMETSAT/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.eumetsat&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "German Neuroinformatics Node/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.g-node&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Sonderforschungsbereich GEO-Q Institut für Erdmessung (IFE)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.geoq&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Geoforschungszentrum Potsdam/"

    for i in range(1, 4):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.gfz&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "IPK Gatersleben/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ipk&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Institute of Science and Technology Austria/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ista&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Korea Institute of Science and Technology Information/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.kisti&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Karlsruher Institut für Technologie/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.kit&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Karlsruher Institut für Technologie - Institut für Organische Chemie/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.kit-ioc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "LDEO - Lamont-Doherty Earth Observatory, Columbia University/"

    for i in range(1, 14):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ldeo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Forschungsdatenrepositorium LUH/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.luis&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "MB-Mediasports/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.moredata&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Max Planck Digital Library/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.mpdl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Neon Neue Energieökonomik GmbH/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.neon&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universität Ulm, Kommunikations- und Informationszentrum (kiz)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.oparu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "TIB-PANGAEAresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.pangaea&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "FIZ Karlsruhe – Leibniz-Institut für Informationsinfrastruktur/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.radar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Warsaw Interdisciplinary Centre for Mathematical and Comutational Modelling/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.radar&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universitätsbibliothek RWTH Aachen University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.rwth&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Thieme Chemistry/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.thieme&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "TIB-TOPOIresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.topoi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universitätsbibliothek Rostock/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ub-hro&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universitätsbibliothek Duisburg-Essen/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ubde&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Otto-von-Guericke-Universität Magdeburg/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ubovgu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "IT-Servicezentrum, Universität Bayreuth/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ubt&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Technische Universität München, Universitätsbibliothek/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ubtum&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universität Konstanz - Bibliothek/"

    for i in range(1, 8):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.ukon&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Bielefeld University/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.unibi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "World Data Center for Climate/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.wdcc&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Weierstraß-Institut für Angewandte Analysis und Stochastik/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.wias&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF)/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.zalf&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Konrad-Zuse-Zentrum Berlin/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tib.zib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "CaltechDATA/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tind.caltech&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "China Geological Survey/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=tsinghua.ngac&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Iowa Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=uiowa.prod&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Kentucky Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=uky.lib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Massachusetts (UMass) Amherst/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=umass.uma&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Massachusetts (UMass) Medical School/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=umass.umw&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Richter Library, University of Miami/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=uml.richter&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "UNM Research Data Services/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=unm.rds&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "USC-DLresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=usc.dl&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ISI Kidney Datasets/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=usc.kidney&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "USGS-PRODresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=usgs.prod&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "College of William & Mary/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.cwm&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "George Mason University/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.gmu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Virginia Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.uva-libra&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Virginia Minor Laboratory/"

    for i in range(1, 10):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.uva-minorlab&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "University of Virginia Minor Laboratory/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.vcu&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Virginia Tech/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=viva.vt&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Washington University in St Louis Libraries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=wustl.lib&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Bundesamt für Strahlenschutz/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.bfs&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Project BioFresh, Leibniz-Institute of Freshwater Ecology and Inland Fisheries/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.biofresh&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "ZBMED-DSMZresults/"

    for i in range(1, 41):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.dsmz&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universität Würzburg/"

    for i in range(1, 9):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.jmuw&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Museum für Naturkunde - Leibniz-Institut für Evolutions- und Biodiversitätsforschung/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.mfn&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Universitätsbibliothek Regensburg/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.pf&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "Westfälische Wilhelms-Universität Münster, Institut für Medizinische Informatik/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbmed.wwuimi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "LMU-ifo Economics & Business Data Center/"

    for i in range(1, 2):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbw.ifo&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)

    institution = "RWI - Rheinisch-Westfälisches Institut für Wirtschaftsforschung e V/"

    for i in range(1, 3):
        filename = institution + "DataCite_result_page" + str(i) + ".json"
        result = requests.get("https://api.datacite.org/works?query=&resource-type-id=dataset&data-center-id=zbw.rwi&year=2017&page[number]=" + str(i))
        print(result)

        with open(filename, 'w') as fout:
            fout.write(result.text)
        time.sleep(4)


DataCite_API()








