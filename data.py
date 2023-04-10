#!/usr/bin/python3

import codecs
def main():
    #Create a list called fruits and display it
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)

    #Get a new fruit from user, add to end of list, and display list
    newFruit = input("Enter a Fruit. ")
    fruits.append(newFruit)
    print(fruits)

    #Get number from user and display fruit at that index
    index = int(input("Enter a number. "))
    if index < 0:
        print("Please enter a larger number. ")
    elif index > len(fruits):
        print("Please enter a smaller number. ")
    else:
        print("{} : {}".format(index,fruits[index - 1]))

    #Add fruit to beginning of list and display list
    fruits.insert(0, "Pineapple")
    print(fruits)

    #print out list using for loop
    for fruit in fruits:
        print(fruit)

    #create a dictionary and display it
    data = dict(name = "Chris", city = "Seattle", cake = "Chocolate")
    print(data)
    
    #remove the cake entry and display dictionary
    data.pop('cake')
    print(data)

    #add fruit index and display dictionary
    data['fruit'] = 'Mango'
    print(data)

    #display the dictionary keys
    for key in data.keys():
        print(key)

    #display the dictionary values
    for value in data.values():
        print(value)

    #display whether cake exists as a key
    print("Found" if "cake" in data else "The cake is a lie!")

    #display whether Mango is a value
    for value in data.values():
        if value == "Mango":
            print("Jackpot")
            break
    else:
        print("No such luck.")

    #create sets s2, s3, and s4
    s2 = set(range(0,21,2))
    s3 = set(range(0,21,3))
    s4 = set(range(0,21,4))
    print(s2,s3,s4)

    #display union of s2 and s3
    print(s2 | s3)

    #display intersection of s3 and s4
    print(s3 & s4)

if __name__ == "__main__": main()