#!/usr/bin/env python3
import sys

def main():
    content = readInFile("passwords.txt")
    groupFound = False
    product = 0
    conditions = []
    passwords = []
    validPasswords = []

    # split the conditions and passwords into separate lists
    for line in content:
        splitContent = line.split(':')
        conditions.append(splitContent[0])
        passwords.append(splitContent[1])

    # Loop through conditions list
    # Set the conditions variables for that value
    # Perform the logic check to ensure the password is valid
    #    - If password[min] or password[max] = letter provided, but not and and not neither, the password is valid
    # If so, add it to the list of valid passwords
    for i in range(0, len(conditions), 1):
        invalid = False
        minString = conditions[i].split("-")
        maxString = minString[1].split(" ")
        letterString = maxString[1]
        letterCount = 0

        if(passwords[i][int(minString[0])] == letterString or passwords[i][int(maxString[0])] == letterString):
            if (passwords[i][int(minString[0])] == letterString and passwords[i][int(maxString[0])] == letterString):
                invalid = True
            else:
                invalid = False
        else:
            invalid = True
    
        # If the password passes the checks, add it to the list of valid passwords
        if (invalid == False):
            print("--Found one! Here are the conditions used--")
            print("maxnum: "+maxString[0]+"\nminnum: "+minString[0]+"\nletter: "+letterString+"\npassword: "+str(passwords[i])+"\nconditions: "+conditions[i])
            validPasswords.append(passwords[i])

        
    print("The total number of valid passwords is: "+str(len(validPasswords)))





def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

