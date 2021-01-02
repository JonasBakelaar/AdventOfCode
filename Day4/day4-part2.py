#!/usr/bin/env python3
# Author: Jonas Bakelaar
# Date: Dec. 24, 2020
# Project: Advent of Code 2020

import sys

def main():
    j = 0
    validPassportCount = 0
    validParamCount = 0
    firstLineNum = 0
    content = readInFile("input.txt")

    for i in range(0, len(content), 1):
        # Find the beginning and end of a passport
        # Loop through those lines to search for substrings
        # Increment count for number of valid fields
        #    - Separate flag for cid present
        # Validate yes/no valid
        
        # Deal with the passport
        if content[i] == "" or i == len(content)-1:
            # For handling the last passport in the file
            if i == len(content)-1:
                i = i+1
            # Loop through lines to find substrings
            # print("firstLineNum: " + str(firstLineNum))
            # print(i)
            for j in range (firstLineNum, i, 1):
                # print("line " + str(j) + ": " + content[j])
                if "byr:" in content[j]:
                    # Get value to validate
                    stringToValidate = getStringToValidate(content[j], "byr:")

                    #Validate the value
                    if len(stringToValidate) == 4 and int(stringToValidate) >= 1920 and int(stringToValidate) <= 2002:
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)
                
                if "iyr:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "iyr:")

                    #Validate the value
                    if len(stringToValidate) == 4 and int(stringToValidate) >= 2010 and int(stringToValidate) <= 2020:
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)
                
                if "eyr:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "eyr:")

                    #Validate the value
                    if len(stringToValidate) == 4 and int(stringToValidate) >= 2020 and int(stringToValidate) <= 2030:
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)

                if "hgt:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "hgt:")

                    splitString = stringToValidate.split("in")

                    if len(splitString) == 1:
                        # Deal with cm
                        splitString = stringToValidate.split("cm")
                        intVal = int(splitString[0])
                        if intVal > 149 and intVal < 194:
                            if "cm" in stringToValidate:
                                validParamCount = validParamCount + 1
                                # print(stringToValidate+"cm")
                    else:
                        # Deal with in
                        intVal = int(splitString[0])
                        if intVal > 58 and intVal < 77:
                            if "in" in stringToValidate:
                                validParamCount = validParamCount + 1
                                print(stringToValidate+"in")
                        
                if "hcl:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "hcl:")

                    valid = True
                    if stringToValidate[0] == '#' and len(stringToValidate) == 7:
                        for l in range (1, len(stringToValidate), 1):
                            if stringToValidate[l].isalnum() == False:
                                valid = False
                    else:
                        valid = False

                    if (valid == True):
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)

                if "ecl:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "ecl:")

                    if stringToValidate == "amb" or stringToValidate == "blu" or stringToValidate == "brn" or stringToValidate == "gry" or stringToValidate == "grn" or stringToValidate == "hzl" or stringToValidate == "oth":
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)
                if "pid:" in content[j]:
                    stringToValidate = getStringToValidate(content[j], "pid:")

                    if stringToValidate.isnumeric() == True and len(stringToValidate) == 9:
                        validParamCount = validParamCount + 1
                        # print(stringToValidate)
            
            # Check to see if it was valid
            # print(validParamCount)
            if validParamCount == 7:
                validPassportCount = validPassportCount + 1

            # Clean up our variables
            validParamCount = 0
            firstLineNum = i



    print(validPassportCount)

# Description: Retrieves the string to validate based on a field provided in a string
# Input: the string to parse, the field the search for
# Output: The value of the field to search for
def getStringToValidate(content, field):

    # print("line to validate: " + content)
    stringToValidate = ""
    fieldInString = content.find(field)

    # If the field is in the string, search for the value. If it's not, just return an empty string
    if fieldInString != -1:
        for i in range(fieldInString+4, len(content), 1):
            if content[i] != " ":
                stringToValidate = stringToValidate + content[i]
            else:
                break
    # print("return String: " + stringToValidate)
    return stringToValidate

# Description: Reads a file, returns its contents line by line in a list
# Input: filename to read
# Output: An array of strings
def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

