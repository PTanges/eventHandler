# An Event object represents a date and range for time of day
# Invariant: Every Event's start value must be lower than the end value
# and the hours are military time from 0 to 24

class Event:
  def __init__ (self, Date, eventName, startTime, endTime):
    self._Date = Date
    self._eventName = eventName
    
    self.validateHour(startTime)
    self._startTime = startTime
    
    self.validateHour(endTime)
    self.validateTime(endTime)
    self._endTime = endTime

  def validateHour(self, Hour):
    if Hour > 24 or Hour < 0:
      raise ValueError("Invalid hour: " + str(Hour))

  def validateTime(self, eventTime):
    if self._startTime > eventTime:
      raise ValueError("Error. Event Start Time must be before Event End Time")

  @property
  def Date(self):
    return self._Date
  
  @Date.setter
  def Date(self, Date):
    self._Date = Date

  @property
  def eventName(self):
    return self._eventName
  
  @eventName.setter
  def eventName(self, eventName):
    self._eventName = eventName

  @property
  def startTime(self):
    return self._startTime
  
  @startTime.setter
  def startTime(self, startTime):
    self.validateHour(startTime)
    self._startTime = startTime

  @property
  def endTime(self):
    return self._endTime
  
  @endTime.setter
  def endTime(self, endTime):
    self.validateHour(endTime)
    self.validateTime(endTime)
    self._endTime = endTime

  def __str__(self):
    return self._eventName + "\n" + str(self._Date.month) + "/" + str(self._Date.day) + "/" + str(self._Date.year) + "\n" + "Starts at: " + str(self._startTime) + "\n" + "Ends at: " + str(self._endTime)