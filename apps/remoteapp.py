from datetime import date
from constants.xPaths import *
from constants.urls import *
from constants.parser import *
from constants.location import *
from constants.email import *
from constants.elementIds import *
from constants.classNames import *
from constants.fileNames import *
from constants.common import *
from constants.functs import *
from apps.baristaapp import *
from apps.partnerapp import *
import requests
import functools
import os
import subprocess
import random
import sys
import time
import string
from selenium.webdriver.chrome import options

import speech_recognition as sr
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from constants.areaCodes import AREA_CODES

from resume_faker import make_resume
from password_generator import PasswordGenerator
from uszipcode import SearchEngine

from webdriver_manager.chrome import ChromeDriverManager

engine = SearchEngine()
fake = Faker()


def remote_app(driver, random_city, fake_identity):
    
    print('Filling Applicaion for ' + random_city)
    #time.sleep(10000)
    # application_part_1(driver, random_city, fake_identity)
    driver.find_element_by_xpath(RESUME_UPLOAD_PARTNER).click()
    # #time.sleep(1)
    remote_application_part_2(driver, random_city, fake_identity,
                        ATTACH_RESUME_PARTNER, RESUME_UPLOAD_PARTNER)
    
    time.sleep(1)

    

    
    remote_application_part_1(driver, random_city, fake_identity)
    driver.find_element_by_xpath(CONTINUE).click()



def remote_application_part_1(driver, random_city, fake_identity):
    info = ''
    for key in XPATHS_2.keys():

        if (key is'first_name'):
            #info = fake_identity['first_name']
            pass
        elif (key is'perfered_first_name'):
            info = fake_identity['first_name']
        elif (key is'last_name'):
            info = ''
            #info = fake_identity['last_name']
            pass
        elif( key  is'zip'):
            info = random.choice(list(engine.by_city(city=random_city))).zipcode
        elif (key  is'pn'):
            info = random_phone(format=3)


        driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)


    driver.find_element_by_xpath(CONTINUE).click()

    driver.find_element_by_xpath('et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_OtherInstitutionCity').send_keys(random_city)

    select = Select(driver.find_element_by_id(XPATHS_3.get('sb_experience')))
    select.select_by_visible_text(NO)

    select = Select(driver.find_element_by_id('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_UDFEducation_Education_32_Status"]'))
    select.select_by_value('com.taleo.functionalcomponent.talent.entity.common.selection.UDSElement__11080__3')

    time.sleep(2)
    driver.find_element_by_xpath(CONTINUE).click()
def remote_application_part_2(driver, random_city, fake_identity, xp1, xp2):

    # make resume
    info = ''
    resume_filename = fake_identity['last_name']+'-Resume'
    make_resume(fake_identity['first_name']+' '+fake_identity['last_name'],
                fake_identity['email'], resume_filename+'.pdf')

    # Send Resume
    info = os.getcwd() + '/'+resume_filename+'.pdf'
    driver.find_element_by_xpath(xp1).send_keys(info)

    #driver.find_element_by_xpath(xp2).click()

    printf(f"Successfully filled out app forms for {random_city}")
    try:
        driver.find_element_by_xpath(CONTINUE2).click()
    except:
        pass
    # take out the trash
    os.remove(resume_filename+'.pdf')