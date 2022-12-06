import random

adjective =['tasty', 'ethically sourced', 'vegan', 'unsalted', 'grass fed', 'uncooked', 'moist', 'steaming', 'medical-grade', 'congealed', 'whipped', 'day-old', 'denatured', 
            'quivering', 'freshly squeezed', 'farm fresh', 'organic', 'synthetic', 'pharmaceutical', 'raw', 'artisinal', 'primeaval' ]
white_stuff = ['plaster', 'Irish cream', 'mashed potatoes', 'vanilla icing', 'sunscreen', 'exterior latex paint', 'plumbers caulk','greek yogurt', 'bull semen', 'crisco', 'mayonaise', 
               'pizza dough', 'nail polish', 'rice pudding', 'tapioca', 'grits', 'cream of wheat',
               'milk of magnesia', 'sebum', 'Elmers glue', 'sour cream', 'myelin']
            
def describe_lather():
    adj = random.choice(adjective)
    term = random.choice(white_stuff)
    return adj + ' ' + term

for k in range(10):
    print(describe_lather())
