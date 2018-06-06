import re
heroRegex = re.compile(r'Batman | Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
