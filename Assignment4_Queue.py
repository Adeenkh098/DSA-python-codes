event_queue=[]

def addevent(event):
    event_queue.append(event)
    print(f"EVENT {event} ADDED TO THE QUEUE")

def process():
    if not  event_queue:
        print("NO EVENTS IN QUEUE TO PROCESS")
    else:
        event =  event_queue.pop(0)
        print(f"PROCESSING EVENT: {event}")

def print_event():
    if not  event_queue:
        print("NO PENDING EVENTS")
    else:
        print(f"PENDING EVENTS :{event_queue}")
    
def cancel_event(event):
    if event in event_queue:
        event_queue.remove(event)
        print(f" CANCELLED EVENT :{event}")
    else:
        print(f"EVENT : {event} NOT FOUND ")
    
while(True):
    print("\n---EVENT PROCESSING SYSTEM--- ")
    print("ENTER 1: FOR ADDING EVENT ")
    print("ENTER 2: FOR PROCESSING AND EVENT ")
    print("ENTER 3: FOR PRINTING AN EVENT ")
    print("ENTER 4: FOR CANCELLING AN EVENT ")
    print("ENTER 5: FOR EXIT")
    try:
        choice = int(input("ENTER YOUR CHOICE (1 TO 5):"))
    except ValueError:
        print("ERROR : INVALID ARGUMENT ")
    if (choice == 1):
        try:
            n = int(input("ENTER THE NO OF EVENTS YOU ARE GOING TO ADD"))
        except ValueError:
            print("ERROR : INVALID ARGUMENT ")
        for i in range(n):
            event = input(f"ENTER THE {i+1} EVENT NAME:")
            addevent(event)
        
    elif (choice == 2):
        process()
    elif (choice == 3):
        print_event()
    elif (choice ==4 ):
        event = input("ENTER THE EVENT NAME THAT YOU WANT TO CANCEL ")
        cancel_event(event)
    elif(choice==5):
        break
    else:
        print("INVALID INPUT , TRY AGAIN ")
