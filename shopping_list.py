# make a list to hold onto our items
shopping_list = []

# print out instructions
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

# ask for new items
while True:
    new_item = input(" >")
    
    #be able to quit
    if new_item == 'DONE':
        break
    
#add new items to the list
    shopping_list.append(new_item)    

#print out the list
print("Here's your list: ")

for item in shopping_list:
    print(item)
    
