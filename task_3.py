import argparse
OPERANDS = {'+','-'}

parser = argparse.ArgumentParser()
parser.add_argument('expresion')
strng = parser.parse_args().expresion

def is_eval(strng):
    size = len(strng)
    if size == 0: return False
    i = 0
    if not strng[i].isdigit():
        return False
    while i < size-1:
        i += 1
        if strng[i].isdigit():
            continue
        if strng[i] in OPERANDS:
                if i+1 < size and strng[i+1].isdigit():
                    i += 1
                    continue
        return False
    return True

ans_1 = is_eval(strng)
ans_2 = eval(strng) if ans_1 else None
print(ans_1, ans_2)
