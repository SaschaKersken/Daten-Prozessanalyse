import csv
import json

csv_file = open('iris.csv', 'r')
csv_reader = csv.reader(csv_file)
iris_xml = '<?xml version="1.0" encoding="utf-8" ?>\n'
iris_xml += '<irises>\n'
for line in csv_reader:
    #iris_xml += '  <iris>\n'
    #iris_xml += f'    <type>{line[4]}</type>\n'
    #iris_xml += f'    <sepal-length>{line[0]}</sepal-length>\n'
    #iris_xml += f'    <sepal-width>{line[1]}</sepal-width>\n'
    #iris_xml += f'    <petal-length>{line[2]}</petal-length>\n'
    #iris_xml += f'    <petal-width>{line[3]}</petal-width>\n'
    #iris_xml += '  </iris>\n'
    iris_xml += f'  <iris type="{line[4]} sepal-length="{line[0]}" sepal-width="{line[1]}" petal-length="{line[2]} petal-width="{line[3]}" />\n'
iris_xml += '</irises>'
print(iris_xml)
