# For demonstration purposes, this script deletes the events that were created with events_creator.py
from googleapiclient.discovery import build
import pickle 

# Load access token 
my_credentials = pickle.load(open(r"./Credentials/token.pickle", "rb"))

# Building a service object that is going to interact with Google API 
service = build("calendar","v3",credentials = my_credentials)

# Get my Calendar ID
my_calendar_id = service.calendarList().list().execute()["items"][0]["id"]

# Get the event ID of all the events created using event_creator.py and store them in a list
delete_events = [event["id"] for event in service.events().list(calendarId = my_calendar_id, q="FC Gatineau").execute()["items"]] # the q argument is a free text search terms. It finds events that match these terms in any field, except for extended properties. 

# Delete all events created by event_creator.py using the list ids 
for event_id in delete_events:
    service.events().delete(calendarId= my_calendar_id, eventId=event_id).execute()