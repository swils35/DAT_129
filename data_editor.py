#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:59:23 2019

@author: StephanieWilson
"""

# a program that interacts with any of the data structures created by class
# members

dictionary = {"race": "tour de france", "winners": {"2017": "Chris Froome", 
                                                    "2018": "Geraint Thomas",
                                                    "2019": "Egan Barnal"},
"stages": {"2019": {"stage 1": "Brussels", "stage 2": "Lyon", 
                    "stage 3": "Saint Etienne"}}}

# greeting
def main():
    
    print("Hello. What task would you like to complete?")
    print()
    menu()

# prints main menu and allows user to choose what they wish to do    
def menu():
    
    # print menu
    print("1: Add a key:value pair")
    print("2: Remove a key:value pair")
<<<<<<< HEAD
    print("3: Update the value of a key")
    print("4: View the dictionary")
    print("5: Tasks complete. View dictionary")
=======
    print("3: View the value associated to a key")
    print("4: Update the value of a key")
    print("5: View the dictionary")
    print("6: Tasks complete. View dictionary")
>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f
    
    # set choice to false
    choice = False
    
    # menu control structure
    while choice == False:
        
        choice = int(input("Please choose an option from above. "))
        
        if choice == 1:
<<<<<<< HEAD
            add(dictionary)
            print()
            menu()
=======
            add()
>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f
            
        elif choice == 2:
            remove()
            
        elif choice == 3:
            update()
            
        elif choice == 4:
<<<<<<< HEAD
            viewDict(dictionary)
            print()
            menu()
=======
            viewDict()
>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f
            
        elif choice == 5:
            complete()
            
        elif choice == 0:
            print("Sorry! That's not a valid input.")
            choice = int(input(" Please choose an option from above. "))
            print()
            
        if choice < 0 or choice > 5:
            print("Sorry! that's an invalid input.")
            choice = False
        

# add a new key:value pair   
<<<<<<< HEAD
def add(dictionary):
    
    nest = 0
    sub = input("Do you wish to add to a sub-dictionary? ")
#    user_input = (" ")
    add_dictionary = dictionary
    
    if sub == "Y" or sub == "y":
        sub = str(input("Okay, please enter the name of the sub-dictionary. "))
        key = input("Please enter the key you would like to add. ")
        value =  input("Please enter the key's associated value. ")
            
        nest += 1
         
        if type(sub) == dict:
            print()
           
            for key in sub:
                add()
#               add(key, value[sub], nest)
        
#        else:
#            print("Sorry! That's not a valid input.")
#            user_input = input(" Please enter the name of the sub-dictionary. ")
#            add(user_input)
#            print()            
            
    else:
        
        key = input("Please enter the key you would like to add. ")
        value =  input("Please enter the key's associated value. ")
        dictionary[key] = value
                        
    return add_dictionary
    
=======
def add():
    
    sub = input("Would you like to add to a sub-dictionary? Y/N ")
  
    # if the key:value pair goes in the second level
    if sub == "Y" or sub == "y":
        
        sub = str(input("Okay, please enter the name of the sub-dictionary. "))
        sub2 = input("Is there an additional sub-dictionary? Y/N ")
        
        # if the key:value pair goes in the third level
        if sub2 == "Y" or sub2 == "y":
            
            sub2 = str(input("Okay, please enter the name of the sub-sub-dictionary. "))
            key = str(input("Please enter the key you would like to create. "))
            value = str(input("Please enter the value you would like to create. "))
            
            dictionary[sub][sub2][key] = value
            
            print()
            menu()
            print()
            
            return dictionary
        
        else:
            
            key = str(input("Please enter the key you would like to create. "))
            value = str(input("Please enter the value you would like to create. "))
            
            dictionary[sub][key] = value
            
            print()
            menu()
            print()
            
            return dictionary
    
    # the key:value pair is at the top level of the dictionary    
    else:
        
       key = str(input("Please enter the key you would like to create. "))
       value = str(input("Please enter the value you would like to create. "))
       
       dictionary[key] = value
        
       menu()
       
       return dictionary
       
       print()
       menu()
       print()

>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f

# remove a key:value pair
def remove():
    
    sub = input("Is the pair you wish to remove in a sub-dictionary? Y/N ")
  
    # if the key:value pair goes in the second level
    if sub == "Y" or sub == "y":
        
        sub = str(input("Okay, please enter the name of the sub-dictionary. "))
        sub2 = input("Is there an additional sub-dictionary? Y/N ")
        
        # if the key:value pair goes in the third level
        if sub2 == "Y" or sub2 == "y":
            
            sub2 = str(input("Okay, please enter the name of the sub-sub-dictionary. "))
            key = str(input("Please enter the key of the pair you wish to remove. "))
            
            del dictionary[sub][sub2][key]
            
            print()
            menu()
            print()
            
            return dictionary
        
        else:
            
            key = str(input("Please enter the key of the pair you wish to remove. "))
            
            del dictionary[sub][key]
            
            print()
            menu()
            print()
            
            return dictionary
    
    # the key:value pair is at the top level of the dictionary    
    else:
        
       key = str(input("Please enter the key of the pair you wish to remove. "))
       
       del dictionary[key]
        
       menu()
       
       return dictionary
       
       print()
       menu()
       print()
    
                 
# update the value of an existing pair
def update():
    sub = input("Is the pair you wish to update in a sub-dictionary? Y/N ")
  
    # if the key:value pair goes in the second level
    if sub == "Y" or sub == "y":
        
        sub = str(input("Okay, please enter the name of the sub-dictionary. "))
        sub2 = input("Is there an additional sub-dictionary? Y/N ")
        
        # if the key:value pair goes in the third level
        if sub2 == "Y" or sub2 == "y":
            
            sub2 = str(input("Okay, please enter the name of the sub-sub-dictionary. "))
            key = str(input("Please enter the key of the pair you wish to update. "))
            value = str(input("Please enter the new value. "))
            
            dictionary[sub][sub2][key] = value
            
            print()
            menu()
            print()
            
            return dictionary
        
        else:
            
            key = str(input("Please enter the key of the pair you wish to update. "))
            value = str(input("Please enter the new value. "))
            
            dictionary[sub][key] = value
            
            print()
            menu()
            print()
            
            return dictionary
    
    # the key:value pair is at the top level of the dictionary    
    else:
        
       key = str(input("Please enter the key of the pair you wish to update. "))
       value = str(input("Please enter the new value. "))
       
       dictionary[key] = value
       
       print()
       menu()
       print()
       
       return dictionary          


# view the dictionary
<<<<<<< HEAD
# credit to Brian Overland
# https://www.quora.com/How-do-I-nicely-print-a-nested-dictionary-in-Python       
def viewDict(val, nest = 0):
       
    if type(val) == dict:
        print()
        nest += 1
        for key in val:
            print(nest * " ", end="")
            print(key, end=":")
            viewDict(val[key], nest)
            
    else:
        print(val)
                        
    return dictionary        
=======
def viewDict():
    
    print()
    print(dictionary)
    print()
    
    menu()
>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f
    

# finished    
def complete():
    print()
    print("Okay. Here's your updated dictionary:")
    print()
<<<<<<< HEAD
    viewDict(dictionary)
=======
    print(dictionary)
>>>>>>> a9c3697c798238f05a8118ee2d93a40bdfadd86f
    
    
main()
