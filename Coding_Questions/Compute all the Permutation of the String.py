Example 1: Using recursion
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('yup'))

==>Output:
yup
ypu
uyp
upy
puy
pyu
None



Example 2: Using itertools
from itertools import permutations

words = [''.join(p) for p in permutations('pro')]

print(words)

==>Output:
['pro', 'por', 'rpo', 'rop', 'opr', 'orp']
