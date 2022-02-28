from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import locators
import sys
from selenium.webdriver.chrome.options import Options


# from selenium.webdriver.common.keys import Keys
st = 0.25

# Moodle Test Automation Plan
# launch Moodle App website - validate we are on the home page
# navigate to Log in Screen - validate we are on the login page
# login with admin account - validate we are on the Dashboard page
# navigate to Add new User page - validate
# populate the new user form using Faker fake data
# submit the form - validate
# search for new user - validate
# logout
# login with new user credentials - validate
# logout
# login with admin account
# search for a new user
# delete new user

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)



# s = Service(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=s)  go back to run none headless
infinity = ''' /\.../\          
              (  •.•  )           
               ..=*=..            
          **~~( \.||./ )  ©Shawna '''

def setUp():
    print(f'Launch Moodle App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.moodle_url)
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == (locators.moodle_url) and driver.title == (locators.moodle_home_page_title):
        print('Woot!!! Moodle Launched Successfully')
        print(f'Moodle homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(st)
    else:
        print(f'Moodle did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()

def tearDown(): #
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

# login to Moodle
def log_in(username, password):
    if driver.current_url == (locators.moodle_url):  # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == (locators.moodle_login_page_url): # check we are on the login page
            print('Moodle App Login Page is displayed!')
            sleep(st)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(st)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(st)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate we are at the Dashboard
            if driver.title == (locators.moodle_dashboard_page_title) and driver.current_url == (locators.moodle_dashboard_url):
                assert driver.current_url == (locators.moodle_dashboard_url)
                assert driver.title == (locators.moodle_dashboard_page_title)
                print('--------------------~*~--------------------')
                print(f'Login Successful. Moodle Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again.')

def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(st)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(st)
    if driver.current_url == (locators.moodle_url):
        print('--------------------~*~--------------------')
        print(f'Logout Successful! at {datetime.datetime.now()}')

def create_new_user():
    # navigate to Site Admin
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(st)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(st)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(st)
    # validate we are on 'Add a new user page'
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'--- Navigate to Add a New user Page - Page Title: {driver.title}')
    sleep(st)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(st)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(st)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(st)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(st)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(st)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(st)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(st)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(st)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(st)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(st)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(st)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    sleep(st)
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(st)
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(st)
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(st)

    # driver.find_element(By.XPATH, '//input[@value="4"]').click()
    sleep(st)
    driver.find_element(By.XPATH, '//Label[contains(., "Create an alias/shortcut to the file")]').click()
    driver.find_element(By.XPATH, '//button[contains(., "Select this file")]').click()
    sleep(st)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(st)
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(st)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(st)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(st)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(st)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(st)
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(st)
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + "\n")
        sleep(st)
    driver.find_element(By.LINK_TEXT, 'Optional').click()
    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(st)
    ######################################################
    # press submit button
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(st)
    print(f'------------New User "{locators.new_username}/{locators.new_password}, {locators.email} is added-----')
    #####################################################
    logger('created')

def search_user():
    if driver.current_url == locators.moodle_user_main_page and driver.title == locators.moodle_user_main_page_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed
        print('Browse list of users page is displayed')
        sleep(st)
        print(f'-----Search for user by email address: {locators.email}')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(st)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]'):
            print(f'---User" {locators.email} is found---')

def check_new_user_can_login():
    if driver.title == (locators.moodle_dashboard_page_title) and driver.current_url == (locators.moodle_dashboard_url):
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'--User with full name {locators.full_name} is displayed--')
            # logger('created')

def delete_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(st)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(st)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(st)
    search_user()
    driver.find_element(By.XPATH, '//*[contains(@title, "Delete")]').click()
    sleep(st)
    assert driver.find_element(By.XPATH, '//h2[contains(., "Delete user")]').is_displayed()
    driver.find_element(By.XPATH, '//button[contains(., "Delete")]').click()
    print(f'--------------------~*~--------------------\nUser {locators.new_username} Has been deleted.')
    logger('deleted')

def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

# setUp()
# log_in(locators.admin_username, locators.admin_password)
# create_new_user()
# search_user()
# log_out()
# # -------------------------------
# # ------Login as New User--------
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# # log_out()
# # # ------Delete New User---------
# # log_in(locators.admin_username, locators.admin_password)
# # delete_user()
# # log_out()
# # tearDown()