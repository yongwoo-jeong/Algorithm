word = input()
letter = 0

def find(word):
    global letter
    if "c=" in word:
        word = word.replace("c=", "a")
        find(word)
    elif "c-" in word:
        word = word.replace("c-", "a")
        find(word)
    elif "dz=" in word:
        word = word.replace("dz=", "a")
        find(word)
    elif "d-" in word:
        word = word.replace("d-", "a")
        find(word)
    elif "lj" in word:
        word = word.replace("lj", "a")
        find(word)
    elif "nj" in word:
        word = word.replace("nj", "a")
        find(word)
    elif "s=" in word:
        word = word.replace("s=", "a")
        find(word)
    elif "z=" in word:
        word = word.replace("z=", "a")
        find(word)
    else:
        letter += len(word) 
        pass
    
find(word)

print(letter)

        
        
    
     
        