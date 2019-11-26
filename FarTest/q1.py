class LetterFilter:

    def __init__(self, s):
        self.s = s
        

# Enter your code here. 
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
# class LetterFilter:
#
#   def __init__(self, s):
#       self.s = s
	
    def filter_vowels(self):
        sv = list(self.s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        i =0
        while i < len(sv):
            if sv[i] in vowels:
                sv.pop(i)
            else:
                i+=1
        svString = ''.join(sv)
        return svString


    def filter_consonants(self):
        sv = list(self.s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        i =0
        while i < len(sv):
            if sv[i] not in vowels:
                sv.pop(i)
            else:
                i+=1
        svString = ''.join(sv)
        return svString

s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())