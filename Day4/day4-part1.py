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
        print(i)
        
        # Deal with the passport
        if content[i] == "" or i == len(content)-1:
            # For handling the last passport in the file
            if i == len(content)-1:
                i = i+1
            # Loop through lines to find substrings
            # print("firstLineNum: " + str(firstLineNum))
            for j in range (firstLineNum, i, 1):
                # print("line " + str(j) + ": " + content[j])
                if "byr:" in content[j]:
                    validParamCount = validParamCount + 1
                if "iyr:" in content[j]:
                    validParamCount = validParamCount + 1
                if "eyr:" in content[j]:
                    validParamCount = validParamCount + 1
                if "hgt:" in content[j]:
                    validParamCount = validParamCount + 1
                if "hcl:" in content[j]:
                    validParamCount = validParamCount + 1
                if "ecl:" in content[j]:
                    validParamCount = validParamCount + 1
                if "pid:" in content[j]:
                    validParamCount = validParamCount + 1
            
            # Check to see if it was valid
            # print(validParamCount)
            if validParamCount == 7:
                validPassportCount = validPassportCount + 1

            # Clean up our variables
            validParamCount = 0
            firstLineNum = i



    print(validPassportCount)


def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

