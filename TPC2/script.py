from lark import Lark,Token
from lark import Transformer
from lark import Discard


f = open("TPC2/result.txt","r")

file = f.read()



entradas = file.split("==============================\n")


grammar = '''
start : recur
      | conc

recur: RMARK " " "*"? TEXTO SPACE? NEWLINE (sv SPACE? NEWLINE)+

conc: CMARK " " concept SPACE? NEWLINE area NEWLINE (sv NEWLINE)* linguas notas
sv : SVMARK " " VID " " TEXTO
   | SVMARK " " SIN " " TEXTO
   | SVMARK " " VAR " " TEXTO

concept: INT "  " NAME_CONC " "+ LETTER_SEX
area: AMARK " " NAME (SPACE NAME)?
linguas: (lingua)+
lingua: LMARK (trad NEWLINE)+
trad: OI TRADUC CI
notas: (NMARK TEXTO NEWLINE)*

SPACE: " "+
RMARK: "###R"
CMARK: "###C"
NMARK: "###N"
AMARK: "###A"
LMARK: "@pt" | "@es" | "@la" | "@en"
NAME : PLV ( " " PLV)* 
SVMARK : "###SV"


PLV: ( LETTER | "á" | "é" | "í" | "ó" | "ú" | "à" | "â"  | "è" | "ê" | "î" | "ô" | "û" | "ã" | "õ" | "ü" | "ç" | "ñ" |"-" | "\+" | "(" | ")" )+

VID: "Vid." | "Vid.-"
SIN: "SIN.-"
VAR : "VAR.-"
TEXTO: (PLV | " " | ";" | "(" | ")" | "[" | "]" | "‘" | "’" | "." | "," |  "“" | "”" | INT)+
OI: "<i>"
CI: "</i>"
TRADUC: TEXTO
NAME_CONC: NAME
LETTER_SEX: LETTER

%import common.NEWLINE
%import common.WORD
%import common.LETTER
%import common.INT
'''



class ExemploTransformer(Transformer):
    def start(self,elementos):
        return elementos
        
    def conc(self,conc):
        print("")
        return conc


    def concept(self,conceito):
        print("CS : \n- " + conceito[1].value)
        print("Genero : " + conceito[2].value)
        return conceito
    
    def area(self,area):
        print("Area : ",area[1].value)
        return area

    def lingua(self,ling):
        #print(ling)
        if ling[0].value == "@es":
            print("ES : ")
            for i in range(1,len(ling)):
                print("-",ling[i])

        elif ling[0].value== "@en":
            print("EN : ")
            for i in range(1,len(ling)):
                print("-",ling[i])
            
        elif ling[0].value== "@pt":
            print("PT : ")
            for i in range(1,len(ling)):
                print("-",ling[i])
            
        elif ling[0].value== "@la":
            print("LA : ")
            for i in range(1,len(ling)):
                print("-",ling[i])
        return ling
            
    def NEWLINE(self,nl):
        return Discard


    def  trad(self,trad):
        return trad[1].value

p = Lark(grammar)

counter=0

for i in range(1,len(entradas),1):
    
    try:
        tree = p.parse(entradas[i])
        data = ExemploTransformer().transform(tree)
    except:
        counter+=1













