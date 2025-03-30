import xml.etree.ElementTree as ET

def get_test_data_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    
    for user in root.find("Login"):
        username = user.get("username")
        password = user.get("password")
        expected = user.get("expected")
        data.append((username, password, expected))
    
    return data
