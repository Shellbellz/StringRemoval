'''
stringRemoval.py
Accepts input from user,removes all strings,
and makes a list and displays the numbers in the list
'''

'''
main function controls flow of program when called
assigns returned list from userInput function to variable
passes value to called stringRemoval function
'''
def main():
    theList = userInput()
    stringRemoval(theList)
'''
userInput function accepts no value
accepts input, tests user input
loops through the range of input and appends to list
returns the list
'''
def userInput():
    listCount = input('How many items would you like the list to have? ')
    while testValue(listCount):
        listCount = input('How many items would you like the list to have, enter a number: ')
    userList = []
    for i in range(int(listCount)):
        listItems = input('What would you like to add to the list? ')
        userList.append(listItems)
    return userList
'''
stringRemoval function accepts list
tests for int in the list and assigns to variable
displays numbers from list
'''
def stringRemoval(list):
    list = [item for item in list if testValue(item) == False]
    if len(list) == 0:
        print('There are no numbers in the list.')
    else:
        print(list)
'''
testValue function accepts one value
tries to cast value as int and returns true or false if value isn't int or not
'''
def testValue(value):
    try:
        int(value)
        return False
    except:
        return True

main()