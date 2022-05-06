# eventHandler
'''
You will be writing a scheduling application allowing a convention center to schedule events. This program will contain two different classes: Date and Event. Both classes should be defined on their own .py modules.

You may use the Date class we designed in class in lecture 18 (which will also be posted on Canvas).

The Event class should have the following attributes:

# event_date (which should be a Date object)
# event_name
# start_hour: Uses a 24-hour clock, so should be a value between 0 and 23
# end_hour: Uses a 24-hour clock, so should be a value between 0 and 23


The Event class should have the following methods:

# __str__. Return a string representation of all important info about this Event: The name of the event, the start and end times (you can simply print their value i.e. from 14 to 16) and the Date. 
# Properties and setters for the attributes. 
# A constructor which takes a name, start and end hours, and a Date object. 
Note: For sake of simplicity, each event will only take one day (i.e. no multiday events). Each event will also not go past midnight, so start_hour must be less than end_hour. For example, an event that starts at 2pm and ends at 4pm would have a start_hour of 14 and an end_hour of 16. 

In your program's main function, create a list to hold the Event objects the user creates. Continually give the user the following choices:

# Add an Event to the list. Ask the user for the date info (day, month, year) start and end time (the user should enter values between 0 and 23) and the name of the event. Create a new Date object with the given day, month, and year and then create a new Event object with the Date object you created, the name, the start time, and then end time. Before adding the new Event to the list, check for overlaps: If there is already an event in the list that takes place on the same date as the new event and its time overlaps the new event, print out the info about the overlapping event and do not add the new event.
#    Hint: if two events are on the same date and one has a start time of 5 and an end time of 10 and the second has a start time of 10 and an end time of 12, this is NOT an overlap. Both events can be take place. However, if one has a start time of 5 and an end time of 10 and the second has a start time of 9 and an end time of 12, this IS an overlap and both cannot take place.
# Cancel an event: The user will type in the name of the event to cancel. Remove the event from the list (if it exists). 
# View all events: In a loop, print the info of all the events currently planned. 
# Quit
'''
