from lark import Lark,Token
from lark import Transformer
from lark import Discard
import json

f = open("TPC3/globalDictionary.txt","r",encoding="utf-8")
f2 = open("TPC3/ptToEnglish.json","w",encoding="utf-8")
file = f.read()



grammar = '''

start : conc (LB conc )*
      
conc: ((ling | area | genero) "\\n") +

ling: LNG ":" " " "\\n" "-" " " trad ("\\n" "-" " " trad)*

trad: TEXTO

area: AR ":" " " " " TEXTO

genero: GEN ":" " " LETTER

LNG: "EN " | "CS " | "ES " | "PT " | "LA "
AR: "Area "
LB: "\\n"
GEN: "Genero "
PLV: ( LETTER | "á" | "é" | "í" | "ó" | "ú" | "à" | "â"  | "è" | "ê" | "î" | "ô" | "û" | "ã" | "õ" | "ü" | "ç" | "ñ" |"-" | "\+" | "(" | ")" )+
TEXTO: (PLV | " " | ";" | "(" | ")" | "[" | "]" | "‘" | "’" | "." | "," |  "“" | "”" | INT)+



%import common.NEWLINE
%import common.WORD
%import common.LETTER
%import common.INT
'''

p = Lark(grammar)

counter=0




class PTtoENTransformer(Transformer):
    def __init__(self):
        self.dicionario={}

    def start(self,elementos):
        json.dump(self.dicionario,f2,indent=True,ensure_ascii=False)
        return elementos
    
    def conc(self,conceito):
        english = []
        sinonimos=[]
        genero=""
        area=""
        nome=""
        
        for i in conceito:
            if i[0] == "PT ":
                nome=i[1]
                for j in range(2,len(i),1):
                    sinonimos.append(i[j])
            elif i[0]=="EN ":
                
                for j in range(1,len(i),1):
                    english.append(i[j])
            elif i[0]=="Genero":
                genero=i[1]
            elif i[0]=="Area":
                area=i[1]
        
        self.dicionario[nome]={"Area":area,"Sinonimos":sinonimos,"English":english,"Genero":genero}
            
        return conceito
    
    def ling(self,ling):
        if (ling[0] == "PT "):
            self.dicionario[ling[1]] ={}
        return ling

    def LNG(self,lng):
        return lng.value
    
    def genero(self,gen):
        if gen[1]=="m":
            return ["Genero","masculino"]
        elif gen[1]=="f":
            return ["Genero","feminino"]
        elif gen[1]=="s":
            return ["Genero","sem genero"]
        else:
            return ["Genero","outro"]

    def trad(sel,trad):
        return trad[0]

    def area(self,area):
        return ["Area", area[1]]

    def LETTER(self,l):
        return l.value

    def TEXTO(self,texto):
        return texto.value




        
    
tree = p.parse(file)
data = PTtoENTransformer().transform(tree)
