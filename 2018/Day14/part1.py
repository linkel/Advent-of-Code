from blist import blist 

INPUT = 513401

recipe_list = [3,7]
#recipe_list = blist(recipe_list)

elf_1_idx = 0
elf_2_idx = 1

#513411
while(len(recipe_list) < 11513411):
    new_recipe_unbroken = recipe_list[elf_1_idx] + recipe_list[elf_2_idx]
    stringed = str(new_recipe_unbroken)
    for char in stringed:
        recipe_list.append(int(char))
    elf_1_idx = elf_1_idx + recipe_list[elf_1_idx] + 1
    while elf_1_idx >= len(recipe_list):
        elf_1_idx = elf_1_idx - len(recipe_list)
    elf_2_idx = elf_2_idx + recipe_list[elf_2_idx] + 1
    while elf_2_idx >= len(recipe_list):
        elf_2_idx = elf_2_idx - len(recipe_list)
    
sequence = [5,1,3,4,0,1]


for idx, a in enumerate(recipe_list):
    print(idx)
    if recipe_list[idx:idx+6] == [5,1,3,4,0,1]:
        print(idx)
        break