#coding : utf-8
__author__ = "lau.wenbo"


import string

s = 'The quick brown fox jumped over the lazy dog.'

print(s)
# 首字母大写
print(string.capwords(s))

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))
