import xml.etree.ElementTree as ET

raiz = ET.parse('documento.xml')
meses = raiz.getroot()


for mes in meses:
    print(mes.attrib['nombre'])