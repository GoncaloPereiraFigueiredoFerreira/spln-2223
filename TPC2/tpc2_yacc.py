import ply.yacc as yacc



"""
PT: Ola
ES: Hola
EN: Hi
CT: Hola
LA: Oi
AREA: COISAS
GENERO: F

PT: Adeus
ES: Adios
EN: Bye
CT: Adios
LA: Xau
AREA: COISAS
GENERO: M

"""


def p_1(p):
    "Dic: Es"
    pass

def p_2(p):
    "Es: E LINHA_B Es"

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
    "LING: ID_LING ':' '\n' TS"


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