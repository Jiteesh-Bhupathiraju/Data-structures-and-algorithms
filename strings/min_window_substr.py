import  collections

import collections

def minWindow( s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        print(j, c, 'missing:',missing, need)
        if not missing: # when its zero i.e. when we found all
            while need[s[i]] < 0: need[s[i]] += 1; i += 1 # pushing up the non zero values for if found later
            print('\n','need at after inner upafte' ,need)
            if not J or j - i <= J - I: I, J = i, j # update statement if less or J is not yet set
            need[s[i]] += 1
            i += 1
            missing += 1  # SPEEEEEEEED UP!
    return s[I: J]

minWindow("ADOBECODEBANC", "ABC")