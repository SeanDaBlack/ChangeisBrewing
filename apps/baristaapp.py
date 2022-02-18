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


from webdriver_manager.chrome import ChromeDriverManager


fake = Faker()


def application_part_1(driver, random_city, fake_identity):
    for key in XPATHS_2.keys():

        match key:
            case 'first_name':
                info = fake_identity['first_name']
            case 'perfered_first_name':
                info = fake_identity['first_name']
            case 'last_name':
                info = fake_identity['last_name']
            case 'zip':
                info = random.choice(CITIES_TO_ZIP_CODES[random_city])
            case 'pn':
                info = random_phone(format=3)
            case 'work_experience_employer':
                info = fake.company()
            case 'work_experinece_title':
                info = fake.job()

        driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)

        # SELECT THE PLACE OF RESIDENCE
        select = Select(driver.find_element_by_id(REGION_COUNTRY))
        select.select_by_visible_text(COUNTRY)
        select = Select(driver.find_element_by_id(REGION_STATE))
        select.select_by_visible_text(CITIES_TO_STATES[random_city])
        select = Select(driver.find_element_by_id(REGION_CITY))
        select.select_by_visible_text(random_city)

        # SELECT EMPLOY HISTORY
        select = Select(driver.find_element_by_id(EMPLOY_HISTORY))
        select.select_by_visible_text(NO)

        # SELECT AVALIABLILITY
        select = Select(driver.find_element_by_id(WILLING_WORK_HOURS))
        select.select_by_value(str(random.randint(1, 5)))
        select = Select(driver.find_element_by_id(PREF_HOURS))
        select.select_by_value(str(random.randint(1, 5)))

        driver.find_element_by_xpath(XPATH_AVAL['hours_holi']).click()
        driver.find_element_by_xpath(XPATH_AVAL['hours_times']).click()
        driver.find_element_by_xpath(XPATH_AVAL['current_job']).click()


def application_part_2(driver, random_city, fake_identity, xp1, xp2):

    # make resume
    info = ''
    resume_filename = fake_identity['last_name']+'-Resume'
    make_resume(fake_identity['first_name']+' '+fake_identity['last_name'],
                fake_identity['email'], resume_filename+'.pdf')

    # Send Resume
    info = os.getcwd() + '/'+resume_filename+'.pdf'
    driver.find_element_by_xpath(xp1).send_keys(info)

    driver.find_element_by_xpath(xp2).click()

    printf(f"successfully filled out app forms for {random_city}")

    # take out the trash
    os.remove(resume_filename+'.pdf')


def application_part_3(driver, random_city, fake_identity):
    for key in XPATH_QUALS.keys():

        driver.find_element_by_xpath(XPATH_QUALS.get(key)).click()


def application_part_4(driver, random_city, fake_identity):
    for key in XPATH_EEO.keys():
        driver.find_element_by_xpath(XPATH_EEO.get(key)).click()

    driver.find_element_by_xpath(random.choice(XPATH_RACES)).click()


def application_part_5(driver, random_city, fake_identity):
    for key in XPATH_VOL.keys():
        if key in ('VOL_NAME'):
            driver.find_element_by_xpath(XPATH_VOL.get(key)).send_keys(
                fake_identity['first_name'] + " " + fake_identity['last_name'])
        elif key in ('VOL_DATE'):
            driver.find_element_by_xpath(XPATH_VOL.get(
                key)).send_keys(today.strftime("%m/%d/%y"))
        elif key in ('VOL_no'):
            driver.find_element_by_xpath(XPATH_VOL.get(key)).click()


def application_part_6(driver, random_city, fake_identity):
    for key in XPATH_QUEST.keys():
        driver.find_element_by_xpath(XPATH_QUEST.get(key)).click()
