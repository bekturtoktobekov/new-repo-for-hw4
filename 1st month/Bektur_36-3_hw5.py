data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

letters = set('qwertyuiopasdfghjklzxcvbnm')

for i in data:
    lower_letters = set(i.lower())
    if  lower_letters & letters:
        designations.append(i)
    else:
        codes.append(i)

operators = {}
index = 0
while index < len(codes):
    operator = designations[index]
    code = codes[index]

    if operator in operators:
        operators[operator].add(code)
    else:
        operators[operator] = {code}
    index += 1
operators.pop('Fonex')
operators.pop('Katel')

new_code_pairs = {'O!' : {'0700','0500'},
                  'Megacom' : {'0999','0555'},
                  'Beeline' : {'0222','0777'}
                  }
for operator, new_codes in new_code_pairs.items():
    if operator in operators:
        operators[operator].update(new_codes)

for operator, codes in operators.items():
   print(f"{operator}: {', '.join(codes)}")
