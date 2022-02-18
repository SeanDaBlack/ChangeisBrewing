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
os.environ['WDM_LOG_LEVEL'] = '0'


today = date.today()

# Adds /usr/local/bin to my path which is where my ffmpeg is stored
os.environ["PATH"] += ":/usr/local/bin"

fake = Faker()

# Add printf: print with flush by default. This is for python 2 support.
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function-unbuffer-python-output#:~:text=Changing%20the%20default%20in%20one%20module%20to%20flush%3DTrue
printf = functools.partial(print, flush=True)

r = sr.Recognizer()


def audioToText(mp3Path):
    # deletes old file
    try:
        os.remove(CAPTCHA_WAV_FILENAME)
    except FileNotFoundError:
        pass
    # convert wav to mp3
    subprocess.run(
        f"ffmpeg -i {mp3Path} {CAPTCHA_WAV_FILENAME}", shell=True, timeout=5)

    with sr.AudioFile(CAPTCHA_WAV_FILENAME) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            printf('Converting audio transcripts into text ...')
            return(text)
        except Exception as e:
            printf(e)
            printf('Sorry.. run again...')


def random_phone(format=None):
    area_code = str(random.choice(AREA_CODES))
    middle_three = str(random.randint(0, 999)).rjust(3, '0')
    last_four = str(random.randint(0, 9999)).rjust(4, '0')

    if format is None:
        format = random.randint(0, 4)

    if format == 0:
        return area_code+middle_three+last_four
    elif format == 1:
        return area_code+' '+middle_three+' '+last_four
    elif format == 2:
        return area_code+'.'+middle_three+'.'+last_four
    elif format == 3:
        return area_code+'-'+middle_three+'-'+last_four
    elif format == 4:
        return '('+area_code+') '+middle_three+'-'+last_four


def gen_password():
    let = list(string.ascii_letters)
    num = list(string.digits)
    characters = list(string.ascii_letters + string.digits + "!@#$%&")

    length = random.randint(6, 30)

    password = []
    for i in range(length):
        x = random.choice(characters)
        if x not in password:
            password.append(x)
        else:
            i = i-1

    x = random.choice(let)
    if not x in password:
        x.capitalize()
        password.append(x)

    x = random.choice(num)
    if x not in password:
        password.append(x)

    random.shuffle(password)
    return "".join(password)


def saveFile(content, filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)
# END TEST


def solveCaptcha(driver):
    # Logic to click through the reCaptcha to the Audio Challenge, download the challenge mp3 file, run it through the audioToText function, and send answer
    googleClass = driver.find_elements_by_class_name(CAPTCHA_BOX)[0]
    time.sleep(2)
    outeriframe = googleClass.find_element_by_tag_name('iframe')
    time.sleep(1)
    outeriframe.click()
    time.sleep(2)
    allIframesLen = driver.find_elements_by_tag_name('iframe')
    time.sleep(1)
    audioBtnFound = False
    audioBtnIndex = -1
    for index in range(len(allIframesLen)):
        driver.switch_to.default_content()
        iframe = driver.find_elements_by_tag_name('iframe')[index]
        driver.switch_to.frame(iframe)
        driver.implicitly_wait(2)
        try:
            audioBtn = driver.find_element_by_id(
                RECAPTCHA_AUDIO_BUTTON) or driver.find_element_by_id(RECAPTCHA_ANCHOR)
            audioBtn.click()
            audioBtnFound = True
            audioBtnIndex = index
            break
        except Exception as e:
            pass
    if audioBtnFound:
        try:
            while True:
                """
                try:
                    time.sleep(3)
                    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, AUDIO_SOURCE)))
                except Exception as e:
                    print(f"Waiting broke lmao {e}")
                """
                driver.implicitly_wait(10)
                href = driver.find_element_by_id(
                    AUDIO_SOURCE).get_attribute('src')
                response = requests.get(href, stream=True)
                saveFile(response, CAPTCHA_MP3_FILENAME)
                response = audioToText(CAPTCHA_MP3_FILENAME)
                printf(response)
                driver.switch_to.default_content()
                iframe = driver.find_elements_by_tag_name('iframe')[
                    audioBtnIndex]
                driver.switch_to.frame(iframe)
                inputbtn = driver.find_element_by_id(AUDIO_RESPONSE)
                inputbtn.send_keys(response)
                inputbtn.send_keys(Keys.ENTER)
                time.sleep(2)
                errorMsg = driver.find_elements_by_class_name(
                    AUDIO_ERROR_MESSAGE)[0]
                if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                    printf("reCaptcha defeated!")
                    break
        except Exception as e:
            printf(e)
            printf('Oops, something happened. Check above this message for errors or check the chrome window to see if captcha locked you out...')
    else:
        printf('Button not found. This should not happen.')

    time.sleep(2)
    driver.switch_to.default_content()
