scores='846601'
elf_1_idx=0
elf_2_idx=1
recipes='37'
while scores not in recipes[-7:]:
    recipes+=str(int(recipes[elf_1_idx])+int(recipes[elf_2_idx]))
    elf_1_idx=(elf_1_idx+int(recipes[elf_1_idx])+1)%len(recipes)
    elf_2_idx=(elf_2_idx+int(recipes[elf_2_idx])+1)%len(recipes)
print(recipes[int(scores):int(scores)+10])
print(recipes.index(scores))
