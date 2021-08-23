from xml.etree import ElementTree

doc = ElementTree.parse('iris-mixed.xml')
root = doc.getroot()
irises = []
for iris in root.findall('iris'):
    iris_type = iris.attrib['type']
    sepal = iris.find('sepal')
    sepal_length = sepal.attrib['length']
    sepal_width = sepal.attrib['width']
    petal = iris.find('petal')
    petal_length = petal.attrib['length']
    petal_width = petal.attrib['width']
    irises.append([
        float(sepal_length),
        float(sepal_width),
        float(petal_length),
        float(petal_width),
        iris_type
    ])
print(f"{len(irises)} Datensätze importiert.")
print(irises[0])
print(irises[50])
print(irises[100])
