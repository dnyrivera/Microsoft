# Using sys library and passa parameter for the console
import sys

parsec = int(sys.argv[1])
lightyears = 3.26156 * parsec

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")

# python3 main.py 10


parsec_input = input("Provide input in parsec: ")
parsec = int(parsec_input)
lightyears = 3.26156 * parsec

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")


print("1" + 2)
