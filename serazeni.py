names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

sorted_names = []

for name in names:

    for i in range(len(sorted_names)):
        if name < sorted_names[i]:
            sorted_names.insert(i,name)
            break
    else:
        sorted_names.append(name)

print(sorted_names)

# vzorové řešení
# Vytvoř list, do kterého vložíš jeden prvek z list `names`. Zároveň ho z listu `names` odstraň. Tento krok se ti bude hodit, když budeš chtít přidávat a seřazovat další jméno z listu `names` do listu `sorted_names`
# sorted_names = [names.pop(0)]
#
# # Začni vnější for loop, kterým budeš procházet seznam `names` (měl by mít už o jeden prvek méně)
# for name in names:
#     # Zační vnitřní for loop, kterým budeš procházet seznam `sorted_names` a pomocí podmínkového výrazu, `break` a `else` vlož jméno z `names` buď na pozici, nebo za pozici daného jméno v listu `sorted_names`
#     for i,s_name in enumerate(sorted_names):
#         if name < s_name:
#             sorted_names.insert(i,name)
#             break
#     else:
#         sorted_names.append(name)
#
# # Vytiskni seřazená jména
# print(sorted_names)