#!/usr/bin/env python3
'''
Splitr by Droogy
----------------
Splitr takes any file and splits it into two files, Splitr can also-
rejoin these file fragments

Usage:
To split a file - ./splitr.py file.png
To rejoin a file - ./split.py -m
'''
import sys
import itertools
import random

def splitr():
    with open(sys.argv[1], "rb") as mainFile:
        mainFileByte = mainFile.read(1)
        while mainFileByte != b"":
            # create 2 files which will each hold part of main file
            fileOne = open("thing1", "ab+")
            fileTwo = open("thing2", "ab+")
            # need to handle ints 0-2 because they mess up our lists
            if(mainFileByte[0] == 0):
                fileOne.write(b"\x00")
                fileTwo.write(b"\x00")
                mainFileByte = mainFile.read(1)
            elif(mainFileByte[0] == 1):
                fileOne.write(b"\x01")
                fileTwo.write(b"\x00")
                mainFileByte = mainFile.read(1)
            elif(mainFileByte[0] == 2 ):
                fileOne.write(b"\x00")
                fileTwo.write(b"\x02")  
                mainFileByte = mainFile.read(1) 
            else: # here is our important routine that reads most of the file
                final = theTupler(mainFileByte)
                byteOne = final[0]
                byteTwo = final[1]
                fileOne.write(bytes([byteOne]))
                fileTwo.write(bytes([byteTwo]))
                mainFileByte = mainFile.read(1)


def theTupler(mainByte):
    factors = []    # list containing every positive number less than our num
    goodPairs = []   # contains the tuples that add up to our int
    byteMe = mainByte[0]    # initializes our current byte as an integer
    
    while byteMe != 0:
        byteMe -= 1
        factors.append(byteMe)
    # itertools does the hard work here and creates a list of tuples
    raw_pairs = itertools.permutations(factors, 2)

    # this routine checks if our tuples add up to the given byte 
    for tuple in raw_pairs:
        if (tuple[0] + tuple[1]) == (factors[0]+1):
            goodPairs.append(tuple)
    
    final = random.choice(goodPairs)     # select a random tuple
    return final    # return a tuple which sums our byte

# this routine is ezpz, just puts everything back together!
def unSplitr():
    with open("thing1", "rb") as fileOne:
        with open("thing2", "rb") as fileTwo:
            with open("reconstructed", "wb") as final:
                byteOne = fileOne.read(1)
                byteTwo = fileTwo.read(1)
                while byteOne and byteTwo != b"":
                    adder = byteOne[0] + byteTwo[0]
                    finalByte = final.write(bytes([adder]))
                    byteOne = fileOne.read(1)
                    byteTwo = fileTwo.read(1)

def main():
    # check if flag is set to merge, if not, run the split routine
    if sys.argv[1] == "-m":
        print("[*] Merging")
        unSplitr()
    else:
        print("[*] Splitting")
        splitr()
    print("Done!")

if __name__ == "__main__":
    main()