from context import Reader
import sys


OUTPUT = []
DATA = {
    "others": {
        "CLA": '7800',
        "CLE": '7400',
        "CMA": '7200',
        "CME": '7100',
        "CIR": '7080',
        "CIL": '7040',
        "INC": '7020',
        "SPA": '7010',
        "SPN": '7008',
        "SZA": '7004',
        "SZE": '7002',
        "HLT": '7001',
        "INP": 'F800',
        "OUT": 'F400',
        "SKI": 'F200',
        "SKO": 'F100',
        "ION": 'F080',
        "IOF": 'F040'
    },
    "mem_ref": {
        "AND": ["0", "8"],
        "ADD": ["1", "9"],
        "LDA": ["2", "A"],
        "STA": ["3", "B"],
        "BUN": ["4", "C"],
        "BSA": ["5", "D"],
        "ISZ": ["6", "E"]
    },
    "labels": {}
}


def first_pass(instructions: list):
    if instructions[0][0] == "ORG":
        try:
            n = int(instructions[0][1])
        except:
            print("error in first instruction")
            sys.exit(1)
    else:
        print("Did you think about starting the program? using origin (ORG)")
        sys.exit(-1)
    
    for i in range(1, len(instructions)):
        if len(instructions[i]) > 2 and instructions[i][0][-1] == ",":
            DATA["labels"][instructions[i][0][:-1]] = i+n-1
            instructions[i].pop(0)


def second_pass(instructions:list):
    n = int(instructions[0][1])
    for i in range(1, len(instructions)):
        s = f"{(i+n-1):016b} "
        if len(instructions[i]) == 1 and instructions[i][0] != "END":
            hex = DATA["others"].get(instructions[i][0], "err")
            if hex == "err":
                print("You have an error in the system")
                sys.exit(1)
            hex = int(hex, 16)
            OUTPUT.append(s + f"{hex:016b}")
        elif instructions[i][-1] == "I":
            ini = DATA["mem_ref"].get(instructions[i][0])
            if ini == "err":
                print("You have an error in the system")
                sys.exit(1)
            ini = int(ini[1], 16)
            num = DATA["labels"][instructions[i][1]]
            OUTPUT.append(s + f"{ini:04b}{num:012b}")
        else:
            OUTPUT.append(f"just for test, i mean this is line {i}")


with Reader("example.txt", OUTPUT) as file:
    first_pass(file)
    second_pass(file)

print(OUTPUT)