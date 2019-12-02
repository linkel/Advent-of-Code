


def addr(A, B, C):
    reg[C] = reg[A] + reg[B]

def addi(A, B, C):
    reg[C] = reg[A] + B

def mulr(A,B,C):
    reg[C] = reg[A] * reg[B]

def muli(A,B,C):
    reg[C] = reg[A] * B

def banr(A,B,C):
    reg[C] = reg[A] & reg[B]

def bani(A,B,C):
    reg[C] = reg[A] & B

def borr(A,B,C):
    reg[C] = reg[A] ^ reg[B]

def bori(A,B,C):
    reg[C] = reg[A] ^ B

def setr(A,B,C):
    reg[C] = reg[A]

def seti(A,B,C):
    reg[C] = A

def gtir(A,B,C):
    if A > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0

def gtri(A,B,C):
    if reg[A] > B:
        reg[C] = 1
    else:
        reg[C] = 0

def gtrr(A,B,C):
    if reg[A] > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0

def eqir(A,B,C):
    if A == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0

def eqri(A,B,C):
    if reg[A] == B:
        reg[C] = 1
    else:
        reg[C] = 0

def eqrr(A,B,C):
    if reg[A] == reg[B]:
        reg[C] = 0
    else:
        reg[C] = 0

opcodes = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

count = 0
# massage the input
behaves_like_three = 0
for s in res:
    if s == "":
        pass
    elif "Before" in s:
        register_before = s[s.find("[")+1:s.find("]")].split(", ")
        register_before = [int(i) for i in register_before]
        count += 1
    elif "After" in s:
        register_after = s[s.find("[")+1:s.find("]")].split(", ")
        register_after = [int(i) for i in register_after]
        count += 1
    else:
        command = s.split(" ")
        command = [int(i) for i in command]
        count += 1
    #print(count)
    if count == 3:
        opcodes_that_work = []
        for fn in opcodes:
            reg = {0:register_before[0],1:register_before[1],2:register_before[2],3:register_before[3]}
            #print(reg)
            fn(command[1],command[2], command[3])
            result = []
            for k,v in reg.items():
                result.append(v)
            if result == register_after:
                opcodes_that_work.append(1)
        print(opcodes_that_work)
        if len(opcodes_that_work) >= 3:
            behaves_like_three += 1
        count = 0

print(behaves_like_three)

#print(register_before)
#print(command)
#print(register_after)