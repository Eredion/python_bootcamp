import sys
import string

def filterwords(str, n):
    for simbol in string.punctuation :
        str = str.replace(simbol, ' ')
    words = str.split()
    filtered = list('')
    for word in words:
        if len(word) > n :
            filtered.append(word)
    print(filtered)

if __name__== '__main__':
    try:
        filterwords(str(sys.argv[1]), int(sys.argv[2]))
    except:
        print("ERROR")
        exit(1)
    exit(0)
