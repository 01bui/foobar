# Lookup Table
# 'op': Precedence grade
ops = {
    '+' : 0,
    '*' : 1,
}

# Check if a token is a valid operand in lookup table
def isOp(token):
    return token in ops.keys()

# Compare the precedence of two operands.
# If result is less than 0: op2 has higher precedence than op1
# If result is greater than 0: op1 has higher precedence than op2
# Otherwise, op1 and op2 have equal precedence
def precedence(op1, op2):
    if not isOp(op1) or not isOp(op2):
        raise ValueError('Invalid operands: %s %s' % (op1, op2))
    return ops[op1] - ops[op2]

def answer(str):
    out = []
    stack = []
    for item in str:
        print item
        if item in ops.keys():
            while len(stack) != 0 and isOp(stack[-1]):
                if precedence(item, stack[-1]) < 0:
                    out.append(stack.pop())
                    continue
                break
            stack.append(item)
        else:
            stack.append(item)
            out.append(stack.pop())
    while len(stack) != 0:
        out.append(stack.pop())
    return ''.join(out)

if __name__ == '__main__':
    input = "2+3*4"
    output = answer(input)
    print output

    input = "2*4*3+9*3+5"
    output = answer(input)
    print output
