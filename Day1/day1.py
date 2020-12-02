#!/usr/bin/env python3
import sys

def main():
    content = readInFile("expensereport.txt")
    pairFound = False

    for i in range(0, len(content), 1):
        content[i] = int(content[i])
    content.sort(reverse=True)

    # Do the thing
    for i in range(0, len(content), 1):
        for j in range(len(content)-1, 0, -1):
            if (content[i]+content[j]) == 2020:
                pairFound = True
                sum = content[i] * content[j]
                break
            if (content[i]+content[j] > 2020):
                break
        if (pairFound == True):
            break
    
    print("The entries that sum to 2020 multiplied together are:")
    print(sum)


def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

