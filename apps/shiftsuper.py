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


from webdriver_manager.chrome import ChromeDriverManager


fake = Faker()


def shift_super_app(driver, random_city, fake_identity):
    
        print('Filling Applicaion for ' + random_city)
        application_part_1(driver, random_city, fake_identity)
        driver.find_element_by_xpath(CONTINUE).click()
        #time.sleep(1)
        application_part_2(driver, random_city, fake_identity,
                           UPLOAD_A_RESUME_BUTTON, ATTACH_RESUME)
        driver.find_element_by_xpath(CONTINUE2).click()
        #time.sleep(1)
        application_part_3(driver, random_city, fake_identity)
        driver.find_element_by_xpath(SUPER_QUAL).click()
        #time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        application_part_4(driver, random_city, fake_identity)
        #time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        application_part_5(driver, random_city, fake_identity)
        #time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        #time.sleep(1)
        driver.find_element_by_xpath(QUEST).click()
        #time.sleep(2)


        try:
            element_present = expected_conditions.presence_of_element_located(
                (By.ID, 'SurveyControl_SurveySubmit'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        application_part_6(driver, random_city, fake_identity)
        driver.find_element_by_xpath(QUEST_SUBMIT).click()

        partner_application_part_6(driver, random_city, fake_identity)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()

        try:
            element_present = expected_conditions.presence_of_element_located(
                (By.ID, 'et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        driver.find_element_by_xpath(FULL_NAME).send_keys(
            fake_identity['first_name'] + " " + fake_identity['last_name'])

        driver.find_element_by_xpath(CONTINUE).click()
        #time.sleep(1)
        driver.find_element_by_xpath(SUBMIT_APP).click()
        #time.sleep(2)