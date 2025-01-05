from context import Reader
import sys


DATA = {}

def first_pass(instructions: list):
    if instructions[0][0] == "ORG":
        try:
            n = int(instructions[0][1])
        except:
            print("error in first instruction")
            sys.exit(1)
    else:
        print("Did you think about starting the program? using ")
        sys.exit(-1)
    
    for i in range(1, len(instructions)):
        if len(instructions[i]) > 2 and instructions[i][0][-1] == ",":
            DATA[instructions[i][0][:-1]] = i+n
            instructions[i].pop(0)


with Reader("example.txt") as file:
    first_pass(file)
