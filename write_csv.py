import csv                          # Writing csv file using the Python CSV module 
import pts_ligue_scrapping          # Importing module that scraps the data to access it 

with open(r"Schedule.csv","w") as schedule:
    schedule_writer = csv.writer(schedule, delimiter = ",", lineterminator = "\n")

    # Writing header 
    schedule_writer.writerow(pts_ligue_scrapping.headers)
    
    # Writing each event row by row in a csv file
    for event in pts_ligue_scrapping.events:
        schedule_writer.writerow([event[0].strftime(r"%Y-%m-%dT%H:%M:%S"), event[1].strftime(r"%Y-%m-%dT%H:%M:%S"),event[2],event[3],event[4]])
