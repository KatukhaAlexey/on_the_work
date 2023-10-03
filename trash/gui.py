import re
regexp = 'a'
s = 'vasya@mial.ru'
match = re.search(regexp, s)
print(match.group(0), match.start(), match.end())