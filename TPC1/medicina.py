import re
import ply.lex as lex
import ply.yacc as yacc

f = open("TPC1/medicina.xml","r",encoding="utf-8")

counter =0

dictionary={}
newlines = ""

for line in f:
    if counter < 434 or counter > 109362: counter+=1
    else:
        counter+=1
        # Limpar texto
        res = re.sub(r'<text.* font="19"><b>\s*(\d+.*)</b></text>', r'###C \1', str(line))
        res = re.sub(r'<text.* font="19"><b>\s*(\S.*)</b></text>', r'###R \1', res)
        res = re.sub(r"<text top=\"\d+\" left=\"\d+\" width=\"\d+\" height=\"\d+\" font=\"\d+\">","",str(res)) #Remove tags de texto
        res = re.sub(r"</text>\n","\n",str(res)) # Remove end text tags
        res = re.sub(r"^ *\n","",str(res)) # Remove empy spaces
        res = re.sub(r"^<i>\s+</i>\n","",str(res)) #Remove empty spaces
        res = re.sub(r"^<b>\s+</b>\n","",str(res)) #Remove empty spaces
        res = re.sub(r"\s*(en|pt|es|la)\s*\n",r'@\1',str(res)) 
        res = re.sub(r";\n",";",str(res))

        newlines+=res

print(newlines)