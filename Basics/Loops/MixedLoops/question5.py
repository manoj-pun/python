# Use a for loop over names, and a while loop inside to count UPPERCASE characters in each
# name.
# names = ["ALICE","Bob","cArOL","DAVE","eve"]

names = ["ALICE", "Bob", "cArOL", "DAVE", "eve"]


for name in names:
    idx = 0
    count = 0
    
    while idx < len(name):
        if name[idx].isupper():
            count += 1
        idx += 1
    
    print(f"{name} -> {count} uppercase letters")