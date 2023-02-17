from roman import *

ar = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
print(ar) #выводим результат перевода
for i in ar:
    print(i, '->' ,roman_to_int(i)) #из арабских переносим в римские 

ob=[4, 58, 1994, 26, 99, 69, 80]
for i in ob:
    print(i, '->',int_to_roman(i)) #из римских в арабские

