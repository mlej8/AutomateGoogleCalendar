![GSuite](https://user-images.githubusercontent.com/43357040/62482770-1953d000-b784-11e9-89b3-a8dc984a6f52.png)
# AutomateGoogleCalendar

## Why automate Google Calendar?

Imagine having to create over a thousand individual events with different name, location, start time, end time and description in your team's Google Calendar. This can be a a tedious and very time consuming task. Are you looking for a smarter and more effective way to get the paperwork done? 

___AutomateGoogleCalendar is the tool that will get this task done worry-free!___

This project utilises Selenium to scrap data on soccer events from http://www.tsisports.ca/. Then, it combines ressources from Google RESTful API (Google Sheet API and Google Calendar API) to create events in your own Google Calendar. 

## Getting Started
### Prerequisites
1. First, clone this repository using:
```
git clone https://github.com/mlej8/AutomateGoogleCalendar.git
```
2. Install the dependencies of this project using: 
```
git install -r requirements.txt
```
3. Install a **ChromeDriver that is compatible to the version of your ChromeBrowser** in the InstagramBot folder on https://chromedriver.chromium.org/downloads
### Create Google Developer Console Project
4. Visit Google Developer Console and login using you Google Account at: https://console.developers.google.com/
5. Create a new project named AutomateGoogleCalendar
6. Enable Google Sheet API and Google Calendar API. 
7. Create a service account key and an OAuth 2.0 client IDs. Then, store these two credentials keys in AutomateGoogleCalendar/Credentials/. 
### Running the project
8. Run write_google_sheet.py to scrap data from http://www.tsisports.ca/ and write it in a Google Sheet named "FC Gatineau Schedule"
9. Run oauth2_setup.py to get an Access token from Google. This script will store this access token at AutomateGoogleCalendar/Credentials/
10. Run event_creator.py to create all the event in your Google Calendar
11. Delete all events using delete_events.py
## Built With
* [Selenium](https://www.seleniumhq.org/) - Web Browser Automation Framework
* [Google Calendar API](https://developers.google.com/calendar/) - Module to work with Google Calendar
* [Google Sheet API](https://developers.google.com/sheets/api/) - Module to work with Google Sheets
* [gspread](https://github.com/burnash/gspread) - Module to work with Google Sheets
* [googleapiclient.discovery](https://github.com/googleapis/google-api-python-client/blob/master/googleapiclient/discovery.py) - A client Library for Google's discovery based APIs.
* [oauth2client.service_account](https://oauth2client.readthedocs.io/) - OAuth2Client Service account credentials Class
* [Pickle](https://docs.python.org/3/library/pickle.html) - Module for serializing and de-serializing a Python object structure
* [google_auth_oauthlib.flow](https://google-auth-oauthlib.readthedocs.io/en/latest/) - Module provides integration with requests-oauthlib for running the OAuth 2.0 Authorization Flow and acquiring user credentials
* [datetime](https://docs.python.org/3/library/datetime.html) - Module to work with dates and times
## Authors

* **Michael Li**
