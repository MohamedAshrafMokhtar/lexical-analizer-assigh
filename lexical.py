# Simple Lexical Analyzer in Python

# Define token types
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

# Input expression (you can change this line)
expression = "x = 10 + y * (5 - 2)"

# Helper functions
def is_letter(char):
    return char.isalpha()

def is_digit(char):
    return char.isdigit()

def lookup(char):
    if char == '+':
        return ADD_OP
    elif char == '-':
        return SUB_OP
    elif char == '*':
        return MULT_OP
    elif char == '/':
        return DIV_OP
    elif char == '=':
        return ASSIGN_OP
    elif char == '(':
        return LEFT_PAREN
    elif char == ')':
        return RIGHT_PAREN
    else:
        return None

# Lexical analyzer logic
i = 0
while i < len(expression):
    char = expression[i]

    if char.isspace():
        i += 1
        continue

    if is_letter(char):
        lexeme = char
        i += 1
        while i < len(expression) and (expression[i].isalnum()):
            lexeme += expression[i]
            i += 1
        print(f"Next token is: {IDENT}, Next lexeme is {lexeme}")

    elif is_digit(char):
        lexeme = char
        i += 1
        while i < len(expression) and expression[i].isdigit():
            lexeme += expression[i]
            i += 1
        print(f"Next token is: {INT_LIT}, Next lexeme is {lexeme}")

    else:
        token = lookup(char)
        if token:
            print(f"Next token is: {token}, Next lexeme is {char}")
        else:
            print(f"Unknown symbol: {char}")
        i += 1