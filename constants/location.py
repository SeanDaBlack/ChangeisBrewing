import random
import barnum
from constants.state_abbrev import *
from uszipcode import SearchEngine

# city = random.choice(list(cap_to_state.keys()))
# engine = SearchEngine()
# zipcodes = engine.by_city(city=city)



CITIES_TO_STATES = {
    'Elmira': 'New York',
    'Seattle': 'Washington',
    'Ithaca' : 'New York',
    #city: cap_to_state[city],

}

CITIES_TO_ZIP_CODES = {
    'Elmira': ['14901', '14902', '14904', '14905'],
    'Seattle': ['98101', '98102', '98103', '98114', '98117', '98122'],
    'Ithaca' : ['14850', '14851', '14852'],
    'Philadelphia' : ['19019', '19050', '19082', '19092', '19108', '19109'],
    #city : list(engine.by_city(city=city))


}

CITIES_TO_URLS = {
    #'Memphis': ['https://starbucks.taleo.net/careersection/1000222retail/jobdetail.ftl?job=210066205&lang=en&iniurl.src=OTH-11840'],
    #'Seattle' : ['https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220003195&lang=en#.YhUW6k9wwFc.link'],
    'Elmira' : ['https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220008435&lang=en',
                       'https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220011416&lang=en',
                       'https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220002690&lang=en'],

    'Ithaca' : ['https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220020074&lang=en',
                        'https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220011417&lang=en#.Yljvvb2yhJY.link',
                        'https://starbucks.taleo.net/careersection/jobdetail.ftl?job=220016345&lang=en#.YljvvdL4v7Q.link'],
    #city : ['https://starbucks.taleo.net/careersection/1000222/jobdetail.ftl?job=220018256&iniurl.src=CWS-11700&tz=GMT-04%3A00&tzname=America%2FNew_York']


}




COUNTRY_CODE_US = 'US'
FULL_NAME_US = 'United States'
