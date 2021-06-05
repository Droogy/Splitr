#!/usr/bin/env python3
'''
Erasr is an un-intended side-effect of testing splitr

it seems to erase part of PNG files without corrupting them

Usage:
To split a file - ./splitr.py file.png
To rejoin a file - ./split.py -m
'''
import sys
import itertools
import random
import os

def houseClean():
    files = ["thing1", "thing2", "reconstructed"]
    for file in files:
        if os.path.exists(file):
            os.remove(file)

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

def theTupler(mainFileByte):
    # this list comprehension checks if our tuples add up to the given byte 
    goodPairs = [tuple for tuple in pruned_pairs if(tuple[0] + tuple[1] == mainFileByte[0])]   
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
    global factors, raw_pairs, pruned_pairs 
    factors = [i for i in range(0, 130)]    # list we need to make permutations
    raw_pairs = itertools.permutations(factors, 2)  # tupled permutations
    pruned_pairs = [pair for pair in set(raw_pairs)]    # get rid of dupes
    if sys.argv[1] == "-m":     # merge files if set
        print("[*] Merging")
        unSplitr()
    else:
        houseClean()
        try:
            print("[*] Splitting")
            splitr()
        except IndexError:
            pass
    print("Done!")

if __name__ == "__main__":
    main()
