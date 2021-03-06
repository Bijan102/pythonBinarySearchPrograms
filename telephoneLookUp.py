#Author:    Bijan Fazeli
#Version:   May 17, 2016

'''
Purpose:
    This program utilizes the binary search algo to find a match
'''

#Global lists
names = []
numbers = []

#
#   binarySearch  - Executes a binary search on a list.
#   
#   @param values - The list
#   @param low    - The low index
#   @param high   - The high index
#   @param target - The target to look for
#   @return       - The index at which the target occurs, or -1 if it does not occur
#
def binarySearch(values, low, high, target):
    if low < high:
        mid = (low + high) // 2
        if values[mid] == target: return mid
        elif values[mid] < target: return binarySearch(values, mid+1, high, target)
        else: return binarySearch(values, low, mid - 1, target)
    else: return -1

#
#   lookUp       - Executes appropriate binary search depending on
#                   the parameter's value.
#                   L would be for phone search
#                   N would be for name search
#                   Otherwise an error message is printed
#
#   @param value - The type of pair search to be done.
#
def lookUp(value):
    name = ""
    number = ""
    
    if value == "L" :
        name = input("Enter the name: ")
        result = binarySearch(names, 0, len(names) - 1, name)
        if result == -1 : print("Sorry, couldn't find what you were looking for.")
        else: print(numbers[result], "is the number of:", name)
    elif value == "N" :
        number = input("Enter the number: ")
        result = binarySearch(numbers, 0, len(numbers) - 1, number)
        if result == -1 : print("Sorry, couldn't find what you were looking for.")
        else: print(names[result], "is the owner of:", number)
    else: print("Sorry, but I didn't understand your input")

#Create a main
def main():
    #Opening a file and start writing to it
    create = open("GG.txt", "w")
    create.write("Bob|555-1234\nJoe|555-2345\nJohn|555-3456\nLuke|555-4567")
    create.write("\nMark|555-5678\nMatthew|555-6789\n")
    create.close()

    #Open the GG.txt file for read only
    readW = open("GG.txt", "r")
    value = readW.read(1)
    temp = value

    #Create a while loop to store the values in the file into global lists
    while(temp != ""):
        if(temp == "|"):
            names.append(value[:-1])
            value = readW.read(9)
            numbers.append(value[:-1])
            value = ""
        temp = readW.read(1)
        value += temp

    answer = input("L)ookup Name, Lookup N)umber or Q)uit? ").upper()

    #Get user response and continue to ask user for another input
    #so long as input value is not Q
    while answer != "Q":
        print()
        lookUp(answer)
        answer = input("\nL)ookup Name, Lookup N)umber or Q)uit? ").upper()

    #Print goodbye
    print("\nGoodbye")

#Call main
main()
