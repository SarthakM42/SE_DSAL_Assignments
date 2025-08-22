undo_stack = []
redo_stack = []

def make_change():
  change=input("enter your text: ")
  undo_stack.append(change)
  redo_stack.clear()

make_change()
print(undo_stack)

def undo_action():
  document=undo_stack.pop()
  redo_stack.append(document)

undo_action()
print(undo_stack)

def redo_action():
  document=redo_stack.pop()
  undo_stack.append(document)

redo_action()
print(undo_stack)

def display():
  print(undo_stack)

while True:
  print("\n1. Make Change ")
  print("2. Undo ")
  print("3. Redo ")
  print("4. Display ")
  print("5. Exit ")
  choice=int(input("Entter Your Choice: "))
  print()
  if choice == 1:
    make_change()
    
  elif choice == 2:
    undo_action()

  elif choice == 3:
    redo_action()

  elif choice == 4:
    display()

  elif choice == 5:
    exit()
    break
  
  else:
    print("Invalid input")