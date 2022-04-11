import random
import barnum
from constants.state_abbrev import *
from uszipcode import SearchEngine

city = random.choice(list(cap_to_state.keys()))
engine = SearchEngine()
zipcodes = engine.by_city(city=city)



CITIES_TO_STATES = {
    'Memphis': 'Tennessee',
    'Seattle': 'Washington',
    'Buffalo' : 'New York',
    city: cap_to_state[city],

}

CITIES_TO_ZIP_CODES = {
    'Memphis': ['38116', '38118', '38122', '38127', '38134', '38103'],
    'Seattle': ['98101', '98102', '98103', '98114', '98117', '98122'],
    'Buffalo' : ['14220', '14221', '14222', '14223', '14224', '14225'],
    'Philadelphia' : ['19019', '19050', '19082', '19092', '19108', '19109'],
    city : list(engine.by_city(city=city))


}

CITIES_TO_URLS = {
    #'Memphis': ['https://starbucks.taleo.net/careersection/1000222retail/jobdetail.ftl?job=210066205&lang=en&iniurl.src=OTH-11840'],
    #'Seattle' : ['https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220003195&lang=en#.YhUW6k9wwFc.link'],
    #'Buffalo' : ['https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220006906&lang=en'],
    # 'Philadelphia' : ['https://starbucks.taleo.net/careersection/1000222retail/jobdetail.ftl?job=220013249&lang=en&iniurl.src=OTH-11840',
    #                     'https://starbucks.taleo.net/careersection/1000222retail/jobdetail.ftl?job=210069745&lang=en&iniurl.src=OTH-11840',
    #                     'https://starbucks.taleo.net/careersection/1000222retail/jobdetail.ftl?job=220014930&lang=en&iniurl.src=OTH-11840']
    city : ['https://starbucks.taleo.net/careersection/1000222/jobdetail.ftl?job=220018256&iniurl.src=CWS-11700&tz=GMT-04%3A00&tzname=America%2FNew_York']


}




COUNTRY_CODE_US = 'US'
FULL_NAME_US = 'United States'
