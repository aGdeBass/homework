import tkinter as tk

# Rejestry w architekturze x86
R8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
R16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
R32 = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI"]
MOD = ["11", "00"]
LABELS = []
COUNTER = [0]
MACHINECODES = []
def checkRegister(register): # Sprawdza typ rejestru i zwraca jego rozmiar i numer
    if register in R8:
        return [8, R8.index(register)]
    elif register in R16:
        return [16, R16.index(register)]
    elif register in R8:
        return [32, R32.index(register)]
    else:
        return [1, "Nieprawidłowy rejestr"]
    
def decToBin(number): # konwersja dziesiętna na 3-bitową binarną
    value = bin(number).replace("0b", "")
    if len(value) == 2:
        value = "0" + value
    elif len(value) == 1:
        value = "00" + value
    return value

def addBlock(reg1, reg2):
    opcodes = ["0x00", "0x01", "0x02", "0x03"] # add opcodes in x86
    if reg2[0] != "[" : # sprawdza czy drugi argument nie jest pamięcią
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2.upper())


        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[0] + decToBin(returnReg2[1]) + decToBin(returnReg1[1]) # tworzenie 8-bitowej liczby binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[0], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[1], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[1], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak
    
    else: # for memory
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2[1:-1].upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[1] + decToBin(returnReg1[1] + decToBin(returnReg2[1])) # tworzenie 8-bitowej wersji binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[2], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[3], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[3], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak

def subBlock(reg1, reg2):
    opcodes = ["0x28", "0x29", "0x2A", "0x2B"]

    if reg2[0] != "[":
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2.upper())


        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[0] + decToBin(returnReg2[1]) + decToBin(returnReg1[1]) # tworzenie 8-bitowej liczby binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[0], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[1], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[1], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak
    
    else: # for memory
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2[1:-1].upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[1] + decToBin(returnReg1[1] + decToBin(returnReg2[1])) # tworzenie 8-bitowej wersji binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[2], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[3], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[3], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak
        
def andBlock(reg1, reg2):
    opcodes = ["0x20", "0x21", "0x22", "0x23"]
    if reg2[0] != "[":
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2.upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[0] + decToBin(returnReg2[1]) + decToBin(returnReg1[1]) # tworzenie 8-bitowej liczby binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[0], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[1], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[1], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak
    
    else: # pamięć
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2[1:-1].upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[1] + decToBin(returnReg1[1] + decToBin(returnReg2[1])) # tworzenie 8-bitowej wersji binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[2], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[3], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[3], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak

def orBlock(reg1, reg2):
    opcodes = ["0x08", "0x09", "0x0A", "0x0B"]

    if reg2[0] != "[":
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2.upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[0] + decToBin(returnReg2[1]) + decToBin(returnReg1[1]) # tworzenie 8-bitowej liczby binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[0], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[1], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[1], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak
    
    else: # pamięć
        returnReg1 = checkRegister(reg1.upper())
        returnReg2 = checkRegister(reg2[1:-1].upper())

        if (returnReg1[0] == 1 or returnReg2[0] == 1):
            return "Coś poszło niezgodnie z planem" # jeśli jeden z argumentów nie jest rejestrem
        if (returnReg1[0] != returnReg2[0]):
            return "Argumenty muszą być tego samego typu"
        
        BinaryValue = MOD[1] + decToBin(returnReg1[1] + decToBin(returnReg2[1])) # tworzenie 8-bitowej wersji binarnej
        DecValue = int(BinaryValue, 2) # wartość binarna na dziesiętną
        if (returnReg1[0] == 8): # rejestry są typem bajtowym
            return [opcodes[2], hex(DecValue)]
        elif (returnReg1[0] == 16): # rejestry są typu word
            return ["0x66", opcodes[3], hex(DecValue)]
        
        elif (returnReg1[0] == 32): # rejestry są typu dword
            return [opcodes[3], hex(DecValue)]
        
        else:
            return "Coś poszło niezgodnie z planem" # jak coś pójdzie nie tak

def assembler(instruction, counter):
    if instruction[0].upper() == "ADD":
        retToken = addBlock(instruction[1], instruction[2])
        machineCode(retToken, counter)
    elif instruction[0].upper() == "SUB":
        retToken = subBlock(instruction[1], instruction[2])
        machineCode(retToken, counter)
    elif instruction[0].upper() == "AND":
        retToken = andBlock(instruction[1], instruction[2])
        machineCode(retToken, counter)
    elif instruction[0].upper() == "OR":
        retToken = orBlock(instruction[1], instruction[2])
        machineCode(retToken, counter)
    elif instruction[0].upper() == "JMP":
        lable = instruction[1]
        LABELS.append([lable, counter])
        retToken = ["0xEB", lable]
        machineCode(retToken, counter)
    
    elif instruction[0][-1] == ":": # jeśli osiągniemy znak ":"
        lable_address = instruction[0][:-1]
        retToken = [lable_address]
        machineCode(retToken, counter)
    
    else:
        print("Coś poszło niezgodnie z planem")

def machineCode(Token, counter):
    
    if len(Token) == 1:
        newCounter = COUNTER[counter] + 0 # zliczanie pamięci dla skoków
        COUNTER.append(newCounter)
        for list in LABELS:
            if list[0] == Token[0]:
                jmpAmount = hex(COUNTER[counter] - COUNTER[list[1]] - 2) # liczenie ilości skoków
                for mCode in MACHINECODES:
                    if mCode[2] == Token[0]:
                        mCode[2] = jmpAmount
                        break
                break
    

    else:
        newCounter = COUNTER[counter] + len(Token) # zliczanie pamięci skoków
        COUNTER.append(newCounter)
        mem = hex(COUNTER[counter]) + '\t'
        newList = []
        newList.append(mem)
        for item in Token:
            newList.append(item)

        MACHINECODES.append(newList)

def entry():
    print("Wprowadź dane:")
    line = input()
    instructions = []
    while line.lower() != "end":
        instructions.append(line.split(" "))
        line = input()
    counter = 0
    for instruction in instructions: # przekazuje instrukcji do asemblera
        assembler(instruction, counter)
        counter = counter + 1

entry()


for list in MACHINECODES:
    print(*list)