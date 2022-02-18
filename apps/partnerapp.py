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
from resume_faker import *
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

def partner_application_part_4(driver, random_city, fake_identity):

    # make resume
    info = ''
    resume_filename = fake_identity['last_name']+'-Resume'
    make_resume(fake_identity['first_name']+' '+fake_identity['last_name'],
                fake_identity['email'], resume_filename+'.pdf')

    # Send Resume
    info = os.getcwd() + '/'+resume_filename+'.pdf'
    driver.find_element_by_xpath(UPLOAD_A_RESUME_BUTTON).send_keys(info)

    driver.find_element_by_xpath(ATTACH_RESUME).click()
    
    os.remove(resume_filename+'.pdf')





def partner_application_part_2(driver, random_city, fake_identity):

    # SELECT EMPLOY HISTORY
    select = Select(driver.find_element_by_id(EMPLOY_HISTORY))
    select.select_by_visible_text(NO)

    # SELECT THE PLACE OF RESIDENCE
    select = Select(driver.find_element_by_id(REGION_COUNTRY))
    select.select_by_visible_text(COUNTRY)
    select = Select(driver.find_element_by_id(REGION_STATE))
    select.select_by_visible_text(CITIES_TO_STATES[random_city])
    select = Select(driver.find_element_by_id(REGION_CITY))
    select.select_by_visible_text(random_city)
    info = ''

    for key in XPATHS_2.keys():
    
        match key:
            case 'first_name':
                info = fake_identity['first_name']
                driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)
            case 'perfered_first_name':
                info = fake_identity['first_name']
                driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)
            case 'last_name':
                info = fake_identity['last_name']
                driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)
            case 'zip':
                info = random.choice(CITIES_TO_ZIP_CODES[random_city])
                driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)
            case 'pn':
                info = random_phone(format=3)
                driver.find_element_by_xpath(XPATHS_2.get(key)).send_keys(info)
            case default:
                pass

    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()


def partner_application_part_3(driver, random_city, fake_identity):
    

    # WORK EXPERIENCE
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_Employer"]').send_keys(fake.company())
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_JobFunction"]').send_keys(fake.job())
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm:dv_cs_experience_CurrentEmployer"]').click()



    #EDUCATION
    #driver.find_element_by_xpath('')
    # SELECT
    select = Select(driver.find_element_by_id('et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_StudyLevel'))
    select.select_by_value(str(random.randint(1, 9)))
    

    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Institution"]').send_keys(random.choice(unis))
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_OtherInstitutionCity"]').send_keys(random_city)
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Program"]').send_keys(random.choice(degrees))


    select = Select(driver.find_element_by_id('et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_UDFEducation_Education_32_Status'))
    select.select_by_visible_text('Graduated - Degree Completed')


def partner_application_part_5(driver, random_city, fake_identity):
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__5166"]').click()
    driver.find_element_by_xpath('//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__15815"]').click()


def partner_application_part_6(driver, random_city, fake_identity):

    l = ['3', '6', '7', '9', '12', '16']

    select = Select(driver.find_element_by_id("et-ef-content-ftf-gp-j_id_id16pc9-page_0-sourceTrackingBlock-recruitmentSourceType"))
    select.select_by_value(random.choice(l))
    driver.find_element_by_id("et-ef-content-ftf-gp-j_id_id16pc9-page_0-sourceTrackingBlock-recruitmentSourceType").click()

