from BeautifulSoup import BeautifulSoup
import math
import requests
import statistics
import sys

SOURCE_URI = 'http://h1bdata.info/index.php?em={0}&job=software&city=san+francisco&year=All+Years'
TITLE_FILTERS = [u'MANAGER', u'TEST']

# TODO: Calculate the CPI on demand since this won't work past the current year
# Source: https://www.bls.gov/regions/west/news-release/consumerpriceindex_sanfrancisco.htm
CPI = {2018: 0, 2017: 0.032213979, 2016: 0.030057392, 2015: 0.026140445, 2014: 0.028413659, 2013: 0.022420196, 
       2012: 0.026822058, 2011: 0.026029921, 2010: 0.013699057, 2009: 0.007308084, 2008: 0.03109957}

# TODO: Don't hard-code the current year
CURRENT_YEAR = 2018

JOB_TITLE_INDEX = 1
SALARY_INDEX = 2
DATE_INDEX = 4


def getRawData(company):
    page = requests.get(buildRequestUri(company))
    soup = BeautifulSoup(page.text)
    table = soup.find('table', attrs={'id':'myTable'})
    tableRows = table.findAll('tr')

    result = []

    for row in tableRows:
        cols = row.findAll("td")
        cols = [ele.text.strip() for ele in cols]
    
        if cols and isValidTitle(cols[JOB_TITLE_INDEX]):
            result.append(formatOutputRow(cols))

    return result


def isValidTitle(title):
    for filter in TITLE_FILTERS:
        if filter in title:
            return False

    return True


def buildRequestUri(company):
    return SOURCE_URI.format(company) 


def normalizeData(salary, date):
    year = int(date.split('/')[2])

    for adjustingYear in xrange(year, CURRENT_YEAR):
        salary = salary * (1 + CPI[adjustingYear])

    return salary


def formatOutputRow(row):
    salary = int(row[SALARY_INDEX].replace(',', ''))
    date = row[DATE_INDEX] 

    return [normalizeData(salary, date), date]


def printStatistics(data):

    rawData = []

    for row in data:
        rawData.append(row[0])

    print 'Low: ' + str(math.ceil(min(rawData)))
    print 'High: ' + str(math.ceil(max(rawData)))
    print 'Average: ' + str(math.ceil(statistics.mean(rawData)))
    print 'Median: ' + str(math.ceil(statistics.median(rawData)))
    print 'Standard Deviation: ' + str(math.ceil(statistics.stdev(rawData)))


def printPercentile(sample, data):
    # TODO: accept input to use for calculation
    return 0


def saveCsv(data):
    # TODO: convert and save to CSV if requested
    return

if len(sys.argv) < 2:
    print 'Error: please provide a company name as an argument.'
    exit(0)

formattedData = getRawData(sys.argv[1])
printStatistics(formattedData)
