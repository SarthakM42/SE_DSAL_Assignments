event_queue = []
def add_event(event):
  event_queue.append(event)
  print(f"Event '{event}' is added to queue")

def process_event():
  if event_queue:
    x=event_queue.pop(0)
    print(f"event {x} is processed")
  else:
    print("no event is available for processing")



def display_pending_event():
  if event_queue:
    for event in event_queue:
      print(f"{event}")
  else:
    print("no pending events")



def cancel_event(event_name):
  if event_queue:
    event_queue.remove(event_name)
    print(f" '{event_name}' is cancelled")
  else:
    print(f"Event '{event_name}' is not found or already processed")

def menu():
  while True:
    print("\nevent queue menu: ")
    print("1. add event")
    print("2. process event")
    print("3. display pending events")
    print("4. cancel event")
    print("5. exit")

    choice = input("enter your choice (1-5): ")

    match choice:
      case '1':
        event = input("enter event name to add: ")
        add_event(event)
      case '2':
        process_event()
      case '3':
        display_pending_event()
      case '4':
        event_name = input("enter event name to cancel: ")
        cancel_event(event_name)
      case '5':
        print("exiting program")
        break
      case _:
        print("invalid choice")

menu()
print(event_queue)