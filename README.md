# Splitr
Take a file, split it in twain - or put it back together.

---
# Note

Splitr is a dumb utility I made as part of a kata. It doesn't have much of a practical application besides perhaps obfuscating some files or flags for CTF challenges.

---

# Usage

Split a file in two
`./Splitr.py secret.png`
- Note that the two file halves will be named thing1 and thing2 respectively, make sure you hold onto those!

Next when we're ready to put the files back together just run the -m (merge) flag
`./Splitr.py -m`
- this will generate a file called "reconstructed" which will be a copy of the original file
---
# To-Do

- At least a crumb of error-handling
- Maybe just delete original file?
- Detect file extension and append to copy
