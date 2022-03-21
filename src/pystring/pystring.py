import math
def purge(str,purgestr):
    for char in str:
        if char in purgestr:
            str = str.remove(char)
    return str