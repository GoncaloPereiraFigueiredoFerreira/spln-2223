import ply.lex as lex


literals = [":","\n","+","-"]
tokens = ["ID","IDLING","VAL","LINHAB","RESTO"]


def t_ID(t):
    r"\w+(?:'\w+)*"
    return t

def t_IDLING(t):
    r"(ES) | (PT) | (CS) | (EN)"
    return t

def t_VAL(t):
    r"[A-Za-z\s\p{P}]"
    return t

def t_LINHAB(t):
    r"\n\n"
    return t

def t_RESTO(t):
    r"[A-Za-z\s\p{P}]\n"
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
#-------------------------------------------------------------- 
# Build the lexer
lexer = lex.lex()
 