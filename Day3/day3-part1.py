#!/usr/bin/env python3
# Author: Jonas Bakelaar
# Date: Dec. 24, 2020
# Project: Advent of Code 2020

import sys

def main():
    j = 0
    treeCount = 0
    content = readInFile("input.txt")
    for i in range(1, len(content), 1):
        s = list(content[i])
        j = j + 1
        if (j > 30):
            j = j - 31
        if (content[i][j] == '#'):
            treeCount = treeCount + 1
            s[j] = '0'
        else:
            s[j] = 'X'
        content[i] ="".join(s)

    for line in content:
        print(line)

    print("trees hit: "+ str(treeCount))


def readInFile(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content

if __name__ == '__main__':
    main()

