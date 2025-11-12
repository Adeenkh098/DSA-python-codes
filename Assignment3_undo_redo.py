undo_list = []
redo_list = []

def undo():
    if not undo_list:
        print("Nothing to undo!")
    else:
        last_word = undo_list.pop()
        redo_list.append(last_word)
        print("Current sentence:", " ".join(undo_list))

def redo():
    if not redo_list:
        print("Nothing to redo!")
    else:
        last_word = redo_list.pop()
        undo_list.append(last_word)
        print("Current sentence:", " ".join(undo_list))


user_input = input("ENTER THE SENTENCE: ")
undo_list = user_input.split()

print("\nCHOOSE THE OPERATION")
print("1 FOR UNDO")
print("2 FOR REDO")
print("3 FOR EXIT")

while True:
    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        undo()
    elif choice == 2:
         redo()
    elif choice == 3:
         break
    else:
        print("INVALID NUMBER")  
      
