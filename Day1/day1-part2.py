#!/usr/bin/env python3
import sys

def main():
    content = readInFile("expensereport.txt")
    groupFound = False
    product = 0

    for i in range(0, len(content), 1):
        content[i] = int(content[i])
    content.sort(reverse=True)

    # Do the thing
    for i in range(0, len(content), 1):
        for j in range(len(content)-1, 0, -1):
            sum = (content[i]+content[j]) 
            # print("first loop sum: ", sum)
            if (content[i]+content[j]) < 2020:
                for k in range(len(content)-1, 0, -1):
                    sum = (content[i]+content[j]+content[k]) 
                    # print("second loop sum: ", sum)
                    if ((content[i]+content[j]+content[k]) == 2020):
                        print("found!")
                        groupFound = True
                        product = content[i]*content[j]*content[k]
                        break
                    if ((content[i]+content[j]+content[k]) > 2020):
                        break
            if (content[i]+content[j] > 2020):
                break
            if (groupFound == True):
                break
        if (groupFound == True):
            break
    
    print("The entries that sum to 2020 multiplied together are:")
    print(product)


def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

