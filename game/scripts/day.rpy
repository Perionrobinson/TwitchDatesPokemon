init python:
    class Day:
        dayNum = 1
        dayString = "Day 1, Monday"
        weekdayNum = 1
        daysOfTheWeek = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        weekdayString = "Monday"
        
        def __init__(self):
            pass
            
        def nextDay(self):
            self.dayNum += 1
            self.weekdayNum = (self.weekdayNum % 5) + 1
            self.weekdayString = self.daysOfTheWeek[self.weekdayNum]
            self.dayString = "Day " + `self.dayNum` + ", " + self.weekdayString
