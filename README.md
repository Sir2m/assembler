# Assembler
---
In chatGPT age, assignments and projects became a harder task since you need it to be clear that _it is not made by chatGPT_. For this, I made this almost over-engineered assembler to make it in a way that won't come out of chatGPT or LLMs in general.

### Project
---
The project consists of the basic assembler, based on the instructions set in __Computer System Architecture, Mano__'s book as a project in the _computer organization_ course in the university. The program uses a custom context manager, since chatGPT won't do this.

The program takes as input the file path, which has in it the assembly code, then outputs the machine code binary of it.

### Manual
---
To use the repo, do the following:
1) Clone the repo:
```bash
git clone https://github.com/Sir2m/assembler.git
```
2) Enter the repo:
```bash
cd assembler
```
3) Run python script
```shell
python assembler.py filename
```
An output file called `results.txt` should be found with the machine code.