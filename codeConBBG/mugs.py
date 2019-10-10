
import sys

data = sys.stdin.read().splitlines()

colourNumber = data[0]
notSet = set()
allColours = {'Black', 'White', 'Yellow', 'Blue', 'Red'}

for colour in data[1:] :
    
    notSet.add(colour)
    if len(notSet) == 4:
        break

colourAnswer = allColours - notSet
for x in colourAnswer:
    print(x)
