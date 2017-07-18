import re

test_str = 'https://Windows123 12.jpg http://sdsdsd.jpg'
pattern = re.compile(r'http[s]?://.*?\.(?:jpg|png)')
for m in pattern.finditer(test_str):
    print(m.group())
print(pattern.findall(test_str))