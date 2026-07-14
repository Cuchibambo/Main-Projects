import sys

def main():
    input = sys.stdin.readline
    texte = input()
    texte = texte.upper()
    letters = {}
    for char in texte:
        if char.isalpha():
            if char in letters.keys(): letters[char] += 1
            else: letters[char] = 1
    print(sorted(letters.items(), key=lambda x:x[1], reverse=True)[0][0])

main()