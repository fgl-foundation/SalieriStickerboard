import os
from urllib.parse import unquote
index=open('index.html',"w", encoding='utf-8')

index.write(open('templates/header.html').read())

groups={'.\\':[]}

def GenHtmlStick(dir=".\\"):
        for i in os.listdir("src\\"+dir):
                if (not os.path.isdir("src\\"+dir+i)):
                        if (dir!=".\\"):
                                code=dir+'.'+i
                        else:
                                code=i
                        groups[dir].append('<div class=block>\n<span>:'+'.'.join(code.split('.')[0:-1:1])+':</span>\n<img onclick="copyToClipboardСode(\''+code+'\')" src=\"src\\'+dir+"\\"+i+'\">\n<a onclick=copyToClipboard("http://sg.salieri.me/assets/stickers/'+dir+'/'+i+'")>Copy url</a></div>\n')
                else:
                        groups[i]=[]
                        GenHtmlStick(i)

GenHtmlStick()

for group in groups:
        if group == ".\\":
                t="Общее"
        else:
                t=group
        index.write("<details > <summary>"+t+" </summary>\n<div>\n")
        for i in groups[group]:
                index.write(i)
        print(group)
        index.write("</div>\n</details>\n")

index.write(open('templates/footer.html',encoding='utf-8').read())