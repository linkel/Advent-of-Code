from blist import blist 

INPUT = 513401

recipe_list = [3,7]
#recipe_list = blist(recipe_list)

elf_1_idx = 0
elf_2_idx = 1
store_most_recent = []
#513411
def findRecipe(recipe_list):
    elf_1_idx = 0
    elf_2_idx = 1
    store_most_recent = []
    while True:
        new_recipe_unbroken = recipe_list[elf_1_idx] + recipe_list[elf_2_idx]
        stringed = str(new_recipe_unbroken)
        for char in stringed:
            recipe_list.append(int(char))
            store_most_recent.append(int(char))
            while len(store_most_recent) > 6:
                store_most_recent.pop(0)
            if store_most_recent == [5, 1, 3, 4, 0, 1]:
                return (len(recipe_list))
        elf_1_idx = elf_1_idx + recipe_list[elf_1_idx] + 1
        while elf_1_idx >= len(recipe_list):
            elf_1_idx = elf_1_idx - len(recipe_list)
        elf_2_idx = elf_2_idx + recipe_list[elf_2_idx] + 1
        while elf_2_idx >= len(recipe_list):
            elf_2_idx = elf_2_idx - len(recipe_list)

print(findRecipe(recipe_list))