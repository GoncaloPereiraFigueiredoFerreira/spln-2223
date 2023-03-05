import re
import ply.lex as lex
import ply.yacc as yacc

f = open("TPC2/medicina.xml","r",encoding="utf-8")

counter =0

dictionary={}
newlines = ""

for line in f:
    if counter < 434 or counter > 109362: counter+=1
    else:
        counter+=1
        # Limpar texto
        res = re.sub(r'<text.* font="19"><b>\s*(\d+.*)</b></text>', r'==============================\n###C \1', str(line))
        res = re.sub(r'<text.* font="19"><b>\s*(\S.*)</b></text>', r'==============================\n###R \1', str(res))
        res = re.sub(r'<text.* font="24">\s*(\S.*)</text>', r'###N \1',  str(res))
        res = re.sub(r'<text.* font="21"><i>\s*(\S.*)</i></text>', r'###A \1',  str(res))
        res = re.sub(r'<text.* font="6">\s*(\S.*)</text>', r'###SV \1',  str(res))
        res = re.sub(r'<text.*font="17">  (SIN\.-\s*\S.*)</text>', r'###SV \1',  str(res))
        res = re.sub(r'<text.*font="17">  (VAR\.-\s*\S.*)</text>', r'###SV \1',  str(res))
        res = re.sub(r"<text top=\"\d+\" left=\"\d+\" width=\"\d+\" height=\"\d+\" font=\"\d+\">","",str(res)) #Remove tags de texto
        res = re.sub(r"</text>\n","\n",str(res)) # Remove end text tags
        res = re.sub(r"^ *\n","",str(res)) # Remove empy spaces
        res = re.sub(r"^<i>\s+</i>\n","",str(res)) #Remove empty spaces
        res = re.sub(r"^<b>\s+</b>\n","",str(res)) #Remove empty spaces
        res = re.sub(r"^\s*(en|pt|es|la)\s*\n",r'@\1',str(res)) 
        res = re.sub(r";\n",";",str(res))
        res = re.sub(r"^ *\d+ *\n","",str(res))
        res = re.sub(r"V\n","",str(res))
        res = re.sub(r"ocabulario\n","",str(res))
        res = re.sub(r"</page>\n","",str(res))
        res = re.sub(r'<page .+>\n',"",str(res))
        res = re.sub(r'<fontspec .+/>\n',"",str(res))
        res = re.sub(r'^; *\n',"",str(res))
        newlines+=res

newlines = re.sub(r"(###R .*\n)==============================\n(###R .*\n)",r'\1\2', str(newlines))
newlines = re.sub(r"(###R .*\n)==============================\n(###R .*\n)",r'\1\2', str(newlines))
newlines = re.sub(r"(###C .*)\n==============================\n###R (.*\n)",r'\1\2', str(newlines))
newlines = re.sub(r"(###SV .*)\n###SV (.*\n)",r'\1\2', str(newlines))
newlines = re.sub(r"(<i>.*)</i>\n<i>\s+(\S.*</i>)",r"\1\2",str(newlines))
newlines = re.sub(r"[ \t]+(==============================\n)",r"\1",str(newlines))
print(newlines)




