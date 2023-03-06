import ply.yacc as yacc
import sys
import ply.lex as lex
from tpc2_lex import tokens


def p_1(p):
    "Dic: Es"
    pass

def p_2(p):
    "Es: E LINHAB Es"

def p_3(p):
    "Es: E"

def p_4(P):
    "E: ITEMS"

def p_5(p):
    "ITEMS: ITEM '\n' ITEMS"
    pass

def p_6(p):
    "ITEMS: ITEM"
    pass

def p_7(p):
    "ITEM: AT_CONC"
    pass

def p_8(p):
    "ITEM: LING"
    pass


def p_9(p):
    "AT_CONC: ID ':' VAL"


def p_10(p):
    "LING: IDLING ':' '\n' TS"


def p_11(p):
    "TS: TS '\n' T"

def p_12(p):
    "TS: T"


def p_13(p):
    "T: '-' RESTO AT_TS"


def p_14(p):
    "AT_TS: AT_TS AT_T"

def p_15(p):
    "AT_TS: "


def p_16(p):
    "AT_T: '\n' '+' ID ':' VAL"


# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()

# Start parsing the input text
for line in sys.stdin:
    parser.success = True
    parser.flag = True        # set to True when (+)
    parser.last = 0
    parser.nInter = 0
    parser.intervalos = []

    parser.parse(line)

