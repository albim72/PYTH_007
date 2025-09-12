import xml.etree.ElementTree as ET

try:
    tree = ET.parse('kraj_.xml')
    root = tree.getroot()

    for country in root.findall('country'):
        print(country.find('wartP').text)

    for child in root:
        print(child.tag, child.attrib)

    print(f"dane z konretnego węzła: {root[0]}")
    print(f"dane z konretnego węzła: {root[0][1]}")
    print(f"dane z konretnego węzła: {root[0][1].text}")
except FileNotFoundError:
    print("Nie znaleziono pliku")
