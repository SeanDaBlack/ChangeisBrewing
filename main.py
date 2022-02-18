from datetime import date
from apps.partnerapp import partner_application_part_3
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
os.environ['WDM_LOG_LEVEL'] = '0'


today = date.today()

# Adds /usr/local/bin to my path which is where my ffmpeg is stored
os.environ["PATH"] += ":/usr/local/bin"

fake = Faker()

# Add printf: print with flush by default. This is for python 2 support.
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function-unbuffer-python-output#:~:text=Changing%20the%20default%20in%20one%20module%20to%20flush%3DTrue
printf = functools.partial(print, flush=True)

r = sr.Recognizer()


def start_driver(random_city):

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(CITIES_TO_URLS[random_city])
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, APPLY_NOW_BUTTON_1)))
    driver.find_element_by_xpath(APPLY_NOW_BUTTON_1).click()
    driver.find_element_by_xpath(PRIVACY_ACCEPT).click()
    driver.find_element_by_xpath(NEW_CANIDATE_BUTTON).click()
    return driver


def generate_account(driver, fake_identity):
    # make fake account info and fill

    info = ''
    email = fake_identity['email']
    # pwo = PasswordGenerator()
    password = gen_password()

    for key in XPATHS_1.keys():
        if key in ('email', 'email-retype'):
            info = fake_identity['email']
        elif key in ('pass', 'pass-retype'):
            info = password
        elif key == 'username':
            info = fake_identity['first_name'] + \
                fake_identity['last_name'] + str(random.randint(0, 10000))

        driver.find_element_by_xpath(XPATHS_1.get(key)).send_keys(info)

    driver.find_element_by_xpath(REGISTER_ACCOUNT).click()

    # try:
    #     element_present = expected_conditions.presence_of_element_located(
    #         (By.ID, 'et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_FirstName'))
    #     WebDriverWait(driver, 10).until(element_present)
    # except TimeoutException:
    #     print("Timed out waiting for page to load")

    time.sleep(random.randint(0, 2))

    printf(f"successfully made account for fake email {email}")


def fill_out_application_and_submit(driver, random_city, fake_identity):

    if random_city == 'Memphis':
        application_part_1(driver, random_city, fake_identity)
        driver.find_element_by_xpath(CONTINUE).click()
        time.sleep(1)
        application_part_2(driver, random_city, fake_identity,
                           UPLOAD_A_RESUME_BUTTON, ATTACH_RESUME)
        driver.find_element_by_xpath(CONTINUE2).click()
        time.sleep(1)
        application_part_3(driver, random_city, fake_identity)
        time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        application_part_4(driver, random_city, fake_identity)
        time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        application_part_5(driver, random_city, fake_identity)
        time.sleep(1)
        driver.find_element_by_xpath(CONTINUE).click()
        time.sleep(1)
        driver.find_element_by_xpath(QUEST).click()
        time.sleep(2)

        try:
            element_present = expected_conditions.presence_of_element_located(
                (By.ID, 'SurveyControl_SurveySubmit'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        application_part_6(driver, random_city, fake_identity)
        driver.find_element_by_xpath(QUEST_SUBMIT).click()

        try:
            element_present = expected_conditions.presence_of_element_located(
                (By.ID, 'et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        driver.find_element_by_xpath(FULL_NAME).send_keys(
            fake_identity['first_name'] + " " + fake_identity['last_name'])

        driver.find_element_by_xpath(CONTINUE).click()
        time.sleep(1)
        driver.find_element_by_xpath(SUBMIT_APP).click()
        time.sleep(2)

        print("APPLICATION SENT")
    elif random_city == 'Seattle':
        try:
            driver.find_element_by_xpath(
                '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        except:
            driver.find_element_by_xpath(
                '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)

        partner_application_part_2(driver, random_city, fake_identity)
        time.sleep(1)

        partner_application_part_3(driver, random_city, fake_identity)

        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)
        partner_application_part_4(driver, random_city, fake_identity)
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)
        partner_application_part_5(driver, random_city, fake_identity)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()

        time.sleep(1)
        partner_application_part_6(driver, random_city, fake_identity)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)
        application_part_4(driver, random_city, fake_identity)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)
        application_part_5(driver, random_city, fake_identity)
        driver.find_element_by_xpath(
            '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
        time.sleep(1)
        try:
            element_present = expected_conditions.presence_of_element_located(
                (By.ID, 'et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName'))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        driver.find_element_by_xpath(FULL_NAME).send_keys(
            fake_identity['first_name'] + " " + fake_identity['last_name'])

        driver.find_element_by_xpath(CONTINUE).click()
        time.sleep(1)
        driver.find_element_by_xpath(SUBMIT_APP).click()
        time.sleep(2)
        
        


def random_email(name=None):
    if name is None:
        name = fake.name()

    mailGens = [lambda fn, ln, *names: fn + ln,
                lambda fn, ln, *names: fn + "." + ln,
                lambda fn, ln, *names: fn + "_" + ln,
                lambda fn, ln, *names: fn[0] + "." + ln,
                lambda fn, ln, *names: fn[0] + "_" + ln,
                lambda fn, ln, *names: fn + ln +
                str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn + "." + ln +
                str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn + "_" + ln +
                str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn[0] + "." +
                ln + str(int(1 / random.random() ** 3)),
                lambda fn, ln, *names: fn[0] + "_" + ln + str(int(1 / random.random() ** 3)), ]

    emailChoices = [float(line[2]) for line in EMAIL_DATA]

    return random.choices(mailGens, MAIL_GENERATION_WEIGHTS)[0](*name.split(" ")).lower() + "@" + \
        random.choices(EMAIL_DATA, emailChoices)[0][1]


def main():
    while True:
        random_city = random.choice(list(CITIES_TO_URLS.keys()))
        try:
            driver = start_driver(random_city)
        except Exception as e:
            printf(f"FAILED TO START DRIVER: {e}")
            pass


        time.sleep(1)

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = random_email(fake_first_name+' '+fake_last_name)

        fake_identity = {
            'first_name': fake_first_name,
            'last_name': fake_last_name,
            'email': fake_email
        }

        try:
            generate_account(driver, fake_identity)
        except Exception as e:
            printf(f"FAILED TO CREATE ACCOUNT: {e}")
            pass


        try:
            fill_out_application_and_submit(driver, random_city, fake_identity)
        except Exception as e:
            printf(f"FAILED TO FILL OUT APPLICATION AND SUBMIT: {e}")
            pass

            driver.close()

            continue

        driver.close()


if __name__ == '__main__':
    main()
    sys.exit()