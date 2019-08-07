from selenium import webdriver
from datetime import datetime, timedelta
import re 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Instantiating a Chrome driver object
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver,10)
driver.implicitly_wait(30)                                                             # Setting an implicit wait of 30 seconds. It is good practice to set up an implicit wait right after the driver was created to avoid "ElementNotFound" errors and give the browsermore time to load.  
driver.maximize_window()                                                               # Maximize window

# Navigating to PTS Ligue page using Selenium 
driver.get("http://www.tsisports.ca/tsi/ligue.aspx")

# Navigate to Ligues
ligues = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@href="Ligues.aspx"]')))
ligues.click()

# Navigate to PLSQ Ligue
# driver.find_element_by_xpath('(//span[contains(text(),"PLSQ")]//preceding-sibling::a)[1]').click()
plsq = wait.until(EC.element_to_be_clickable((By.XPATH,'(//span[contains(text(),"PLSQ")]//preceding-sibling::a)[1]')))
plsq.click()

# Change language to English 
plsq = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()=\"EN\"]")))
plsq.click()

# Navigating to specific team 
driver.find_element_by_xpath('//a[contains(text(), "Standings")]').click()                   # click on Standings drop-down menu
driver.find_element_by_xpath('//a[@href="l_classam.aspx"]').click()                          # click on "Standings per division" 
driver.find_element_by_xpath('//a[text()="PLSQ-M"]').click()                                 # click on "PLSQ-M"
driver.find_element_by_xpath("(//span[text()='Validated Standing']//parent::a)[1]").click()  # click on "Validated Standing"
driver.find_element_by_xpath("//a[contains(text(),\"FC Gatineau\")]").click()                # click on FC Gatineau 
driver.switch_to.window(driver.window_handles[1])                                            # switch focus to new tab

# Creating an empty dictionary that will store data 
data_dict = {}
labels = ["Date_", "Time_", "Fieldname_", "Home_", "Visit_"] # dictionary labels, they also serve for creating the xpath that will find the elements we need. We can add "RezH_" and "RezV_" to the labels if we wanted the scores

# Create a xpath 
xpath = "//span[contains(@id,\"ContentPlaceHolder1_gamesTeam1_viewGames_lbl"   # xpath used to locate searched content in the table

# Scrapping data from the web
for label in labels: # Every key in the dictionary will represent a list of the corresponding data
    data_dict[label.replace("_","")] = [x.text for x in driver.find_elements_by_xpath(xpath + label + "\")]")]

# Creating a list of events (represented by a list). Each event contains: Date (ex: 'Sat 2019-05-04'), Time (ex: '15:00'), Location, HomeTeam and AwayTeam
events = [list(a_list) for a_list in list(zip(*data_dict.values()))]  #  data_dict.values() returns a list of the values in the data_dict. list(zip(*data_dict.values())) returns a list of tuples representing each event, then I typecast each tuple to a list 

# Combine each event's Date and Time into a string of this format: "%Y-%m-%dT%H:%M:%S". This simplifies the creation of events with the Google Calendar API later. 
for event in events:
    # event[:2] can only be assigned to an iterable, that's why we have to put the string inside a list (which is an iterable)
    event[:2] = [" ".join(event[:2])] # Merging Date and Time elements in each list. This operation removes the Date and Time item in each list, and inserts a new list of a single element in their place. 
    # Convert data to its corresponding type. Date -> date "%Y-%m-%dT%H:%M:%S" Location -> string , HomeTeam -> string, AwayTeam -> string
    event[0] = datetime.strptime(re.sub(r"([A-Za-z]+\s)", "",event[0]).strip(), r"%Y-%m-%d %H:%M") # removes the word in front of the numbers and any extra space. The method datetime.strptime() creates a datetime object from a string (1st argument) and the expected format (2nd argument)
    # Insert a column "EndTime"
    event[1:] = [event[0] + timedelta(hours = 1, minutes = 30)] + event[1:] # Setting up end time of the event after 2h

# Determine headers 
headers = ["StartTime", "EndTime", "FieldName","HomeTeam","AwayTeam"]

# Closing webdriver
driver.quit()  # close the entire browser, .close() closes the current tab
