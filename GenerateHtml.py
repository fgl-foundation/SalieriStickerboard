import os
from urllib.parse import unquote
index=open('index.html',"w", encoding='utf-8')

index.write(open('templates/header.html').read())

for i in os.listdir("src\\"):
        if (not os.path.isdir("src\\"+i)):
                index.write('<img src=\"src\\'+i+'\">')