import argparse
OPERANDS = {'+','-','*','/'}

parser = argparse.ArgumentParser()
parser.add_argument('var_1')
parser.add_argument('operand')
parser.add_argument('var_2')
var = parser.parse_args()
var_1, var_2 = var.var_1, var.var_2
operand = var.operand
if operand not in OPERANDS:
    raise Exception('NotImplementedError')
try:
    ans = eval(f'{var_1} {operand} {var_2} ')
except:
    raise Exception('NotImplementedError')
print(ans)
