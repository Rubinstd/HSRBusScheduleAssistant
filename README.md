# HSRBusScheduleAssistant
Code for the backend of a Google Assistant command for checking nearby bus schedules using GTFS-realtime data.

General Notes
-------------
Currently a work in progress.

HSR GTFS Data
------------
The GTFS Data in this repository is all the data that is needed for reading the GTFS realtime data (ex. tables for translating various id values).

Python Code
-----------
Currently the python code is used for finding the next bus times given a natural name for the bus (ex. 5C) . It does so by:

- Finding the route and trip id's for any bus route that relates to the name given.
- Narrowing down the upcoming routes for a stop nearby (currently the stop is hardcoded to Main at Emmerson but this will be later changed to find the nearest stop to the user).
- Translating the bus times given in POSIX time to a more readable format (24 hour format currently) and then returning upcoming bus times to the user.

The goal is to find an efficient way now to host this code (ex. Using Amazon Lambda) so that the google action can call this when the assistant is asked the next bus time.

Google Action
-----------
There is a google action that will work with this code is currently set up to recognize when a user is asking for a bus route scheduleand then pass that bus route name on to the python code to actually handle the data analysis that must be done to determine the upcoming busses.

More information about this will be added later.
