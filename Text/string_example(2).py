#coding : utf-8
__author__ = 'lau.wenbo'


import string

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except Exception as e:
    print('ERROR:', str(e))

print('safe_substitute():', t.safe_substitute(values))