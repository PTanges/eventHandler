from Date import Date
from Event import Event

def eventOverlap(eventHandler, newEvent):
  for event in eventHandler:
    if event.Date == newEvent.Date:
      if (newEvent.startTime > event.startTime and newEvent.startTime < event.endTime) or (newEvent.endTime > event.startTime and newEvent.endTime < event.endTime) or (event.startTime == newEvent.startTime and event.endTime == newEvent.endTime):
          return True
  return False

def addEvent(eventHandler):
  year = int(input("What year is the event taking place? "))
  month = int(input("What month (1-12) is the event taking place? "))
  day = int(input("What is the numbered day of the event? "))

  newDate = Date(day, month, year)

  eventName = input("What is the name of the event? ")
  startTime = int(input("What time does the event start?\nMilitary Time: "))
  endTime = int(input("What time does the event end?\nMilitary Time: "))

  newEvent = Event(newDate, eventName, startTime, endTime)

  # Run comparison if >2 events are created. Add event if no contradiction
  if len(eventHandler) >= 1:
    if eventOverlap(eventHandler, newEvent) is False:
      eventHandler.append(newEvent)
    else:
      print("The new event overlaps a current event")
      print(newEvent)
  else:
    eventHandler.append(newEvent)

# Remove an event from list
def cancelEvent(eventHandler):
  command = input("Enter the name of the event: ")
  for index in range(len(eventHandler)):
    if command == eventHandler[index].eventName:
      del eventHandler[index]
      print(f'The event {command} has been removed')

# Print all events in list
def viewEvents(eventHandler):
  for index in range(len(eventHandler)):
    print(f'{eventHandler[index]}\n')
  if len(eventHandler) == 0:
    print("There are no events currently scheduled")

def main():
  # List holds event objects
  eventHandler = []

  # Venue Structure to handle input
  while True:
    choice = int(input("\nEnter\n1) add an event\n2) cancel an event\n3) view all events\n4) quit program\nCommand: "))
    if choice == 1:
      addEvent(eventHandler)
    elif choice == 2:
      cancelEvent(eventHandler)
    elif choice == 3:
      viewEvents(eventHandler)
    elif choice == 4:
      break

if __name__ == "__main__":
  main()