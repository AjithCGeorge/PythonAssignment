from urllib.request import urlopen
from xml.etree.ElementTree import parse

var_url = urlopen('https://www.w3schools.com/xml/simple.xml')
xmldoc = parse(var_url)

root=xmldoc.getroot()
data={}
itemNo=1
for j in root:
    data['Item {}'.format(itemNo)]={'Name':j[0].text,'Price':j[1].text}
    itemNo+=1
    # data[j[0].text]= j[1].text
for i in data:
    print(data[i])