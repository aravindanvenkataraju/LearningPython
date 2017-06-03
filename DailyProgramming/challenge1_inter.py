def display_menu():
    for option in menu:
        print ("%d => %s" %(option, menu[option]))
    
def add_event():
    event_name = input("What's the event? ")
    while event_name == '':
        event_name = input("Event Name cannot be empty, what's the event? ")
    while True:
        try:
            event_time = int(input("When is the event? (a number between 0 - 24) "))
            if 0 > event_time > 24:
                print("Time cannot be less than 0 or greater than 24. Try again")
            else:
                break
        except:
            print("Enter a valid value!")
    if event_time in events:
        decision = input("There is already an event (%s) scheduled at %d:00 hours. Do you want to overwrite it? (Y/N) " % (events[event_time], event_time))
        if decision == 'Y':
            events[event_time] = event_name
            print("Event over-written successfully!")
        elif decision == 'N':
            print("No changes to events!")
        else:
            print("Invalid Input")
    else:
        events[event_time] = event_name
        print("Event added successfully!")
def delete_event():
    if show_all_events():
        try:
            event_time = int(input("Enter the event you want to delete."))
            if 0 > event_time > 24:
                print("Time cannot be less than 0 or greater than 24.")
            else:
                if event_time in events:
                    decision = input("Are you sure you want to delete the event '%s'? (Y/N) "%events[event_time])
                    if decision == 'Y':
                        print("%s is deleted!" % events.pop(event_time))
                    elif decision == 'N':
                        print("OK! event will not be removed.")
                    else:
                        print("Invalid choice")
                else:
                    print("No event found for at %d:00 hours"%event_time)
        except:
            print("Invalid event time!")
def show_event():
    try:
        event_time = int(input("Enter the event time you want to view."))
        if 0 > event_time > 24:
            print("Time cannot be less than 0 or greater than 24.")
        else:
            if event_time in events:
                print("The event scheduled at %d:00 hours is '%s'" % (event_time, events[event_time]))
            else:
                print("No event found for at %d:00 hours"%event_time)
    except:
        print("Invalid event time!")

def edit_event():
    try:
        event_time = int(input("Enter the event time you want to edit."))
        if 0 > event_time > 24:
            print("Time cannot be less than 0 or greater than 24.")
        else:
            if event_time in events:
                old_event = events[event_time];
                print("The event scheduled at %d:00 hours is '%s'" % (event_time, old_event))
                event_name = input("What's the new event? ")
                while event_name == '':
                    event_name = input("Event Name cannot be empty, what's the event? ")
                events[event_time] = event_name
                print("Event '%s' is replaced with event '%s' at %d:00 hours" % (old_event, event_name, event_time))
            else:
                print("No event found for at %d:00 hours"%event_time)
    except:
        print("Invalid event time!")
def purge_events():
    decision = input("Are you sure you want to purge the events? (Y/N) ")
    if decision == 'Y':
        events.clear()
        print("All events purged!")
    elif decision == 'N':
        print("OK! events will not be purged.")
    else:
        print("Invalid choice")
        
def show_all_events():
    if not events:
        print("No events available")
        return False
    else:
        print("The available events are:")
        for event in events:
            print("%s at %d:00 hours"%(events[event], event))
        return True
    
menu={1:"add event",2:"delete event",3:"show event",4:"edit event", 5: "show all events", 6:"purge events", 7:"exit daily events manager"}
events = dict()
print("Welcome to Daily event Manager")
while True:
    display_menu()
    option = int(input("Enter your choice: "))
    #print("the option is %s"%option)
    if option in menu:
        print ("You chose to %s" % menu[option])
        if menu[option] == "add event":
            add_event()
        if menu[option] == "delete event":
            delete_event()
        if menu[option] == "show event":
            show_event()
        if menu[option] == "edit event":
            edit_event()
        if menu[option] == "show all events":
            show_all_events()
        if menu[option] == "purge events":
            purge_events()
        if menu[option] == "exit daily events manager":
            print("Bye!")
            exit()
    else:
        print ("Invalid choice!")


