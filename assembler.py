from context import Reader
import sys


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
        print("Did you think about starting the program? using ")
        sys.exit(-1)
    
    for i in range(1, len(instructions)):
        if len(instructions[i]) > 2 and instructions[i][0][-1] == ",":
            DATA["labels"][instructions[i][0][:-1]] = i+n
            instructions[i].pop(0)


with Reader("example.txt") as file:
    first_pass(file)
