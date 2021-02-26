from sys import stdin
from Parser import clean

def main():
    print(*clean.cleanCode(stdin.readlines()),sep='\n')
main()