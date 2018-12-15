input = 320851

recipes = [3,7]
elf1 = 0
elf2 = 1

while len(recipes) < input+10:
    # move current elf1 and elf2
    score1 = recipes[elf1]
    score2 = recipes[elf2]
    elf1 = (elf1+score1+1)%len(recipes)
    elf2 = (elf2+score2+1)%len(recipes)
    # add sum of score digits to recipes
    new_score1 = recipes[elf1]
    new_score2 = recipes[elf2]
    digits = list(map(int, str(new_score1+new_score2)))
    recipes += digits

print("".join(map(str, recipes[input:input+10])))
