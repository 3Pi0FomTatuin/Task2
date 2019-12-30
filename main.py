import re
import lib

converter = lib.Converter()
expr = '123445 + 123 = 123568'
expr = expr.replace(' ', '')

words = []
lexemes = re.split(r'(\+|-|\*|/|=)', expr)
for s in lexemes:
    if s == '+':
        words.append('plus')
    elif s == '-':
        words.append('minus')
    elif s == '*':
        words.append('multiply')
    elif s == '/':
        words.append('divide')
    elif s == '=':
        words.append('equals')
    elif s.isdigit():
        words.append(converter.number_to_words(s))
    else:
        print('invalid input')
        break

print(' '.join(words))
