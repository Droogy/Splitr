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

def splitr():
    with open(sys.argv[1], "rb") as mainFile:
        mainFileByte = mainFile.read(1)
        while mainFileByte != b"":
            # create 2 files which will each hold part of main file
            fileOne = open("thing1", "ab+")
            fileTwo = open("thing2", "ab+")
            # check if byte is divisible by two, if it is, then we just store-
            # x-1 in one file, and \x01 in the other
            if(mainFileByte[0] % 2 != 0):
                byte2write = mainFileByte[0] - 1
                # note the brackets around "byte2write" avoid a weird null-byte problem
                fileOne.write(bytes([byte2write]))
                fileTwo.write(b"\x01")
                mainFileByte = mainFile.read(1)
            # if our byte is just 1, store 1 in one file and zero in the other
            elif mainFileByte == b"\x01":
                fileOne.write(b"\x01")
                fileTwo.write(b"\x00")
                mainFileByte = mainFile.read(1)
            # if our file is divisible by two, store each half in each file
            else:
                byte2write = mainFileByte[0] // 2
                fileOne.write(bytes([byte2write]))
                fileTwo.write(bytes([byte2write]))
                mainFileByte = mainFile.read(1)
    # be polite and close your files!
    mainFile.close()
    fileOne.close()
    fileTwo.close()

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
    fileOne.close()
    fileTwo.close()
    final.close()

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