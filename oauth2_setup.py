from google_auth_oauthlib.flow import InstalledAppFlow 
import pickle

# Determine the scope 
scopes = ["https://www.googleapis.com/auth/calendar"] # determine scope as Google Console Project can access everything from a user's calendar 

# OAuth 2.0 Authorization flow. Google created a help class for helping with Installed Application Authorization Flow
flow = InstalledAppFlow.from_client_secrets_file(r"./Credentials/oauth_credentials.json", scopes=scopes)
credentials = flow.run_console() # Access token 

# Saving credentials using Pickle (module for saving any Python objects)
pickle.dump(credentials,open("./Credentials/token.pickle", "wb")) # .dump() is used for dumping any Python Object into a file 
