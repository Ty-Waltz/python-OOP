class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.count = 0


        def add_count(self):
            self.count += 1
       
        def get_participant_count(self):
             return(self.count)


        def __str__(self):
            return(f"Name:{self.name}\n"
            f"Date: {self.date}\n"
            f"Number of guests: {self.count}")


event = Event("The Event","August 2nd, 2027")      
print("Original Event")
print(event)
#print(event.get_participant_count())


event.add_count()
event.add_count()
event.add_count() 
event.add_count()


print("Updated event:")
print(event)
#print("The new count of people is:")
#print(event.get_participant_count())
