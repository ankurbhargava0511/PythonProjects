import json
records=[]
class FileManger(object):
    def savedata(self, webpage, name, password):
         if len(records) == 0:
            for record in self.getAlldata():
                records.append(record)
         new_record= dict(webpage=webpage, user_name=name, user_password=password)
         records.append(new_record)
         with open('records.json', 'a+') as f:
             f.seek(0)
             json.dump(records, f)
             f.truncate()


    def getAlldata(self):
        try:
            with open('records.json', 'r+') as openfile:
                json_object = json.load(openfile)
        except:
            return []
        else:
            return list(json_object)
    def getdata(self, web):
        if len(records) == 0:
            for record in self.getAlldata():
                records.append(record)


        for i in records:
            if i["webpage"] == web:
                selected_record=i
                break;
        return selected_record

    def upload_data(self, file_type, full_file_path):
        pass

    def download_data(self, file_type, file_name):
        pass


    def write_to_xml(self):
        import xml.etree.ElementTree as ET

        # create the file structure
        employee = ET.Element('employee')
        details = ET.SubElement(employee, 'details')
        first = ET.SubElement(details, 'firstname')
        second = ET.SubElement(details, 'lastname')
        third = ET.SubElement(details, 'age')
        first.text = 'Shiv'
        second.text = 'Mishra'
        third.text = '23'

        # create a new XML file with the results
        mydata1 = ET.ElementTree(employee)
        # myfile = open("items2.xml", "wb")
        # myfile.write(mydata)
        with open("new_sample.xml", "wb") as files:
            mydata1.write(files)


    def read_from_xml(self):
        tree = etree.parse("Sample-employee-XML-file.xml")

        root = tree.getroot()
        columns = ["firstname", "lastname", "title", "division", "building", "room"]

        datatframe = pd.DataFrame(columns=columns)

        for node in root:
            firstname = node.find("firstname").text

            lastname = node.find("lastname").text

            title = node.find("title").text

            division = node.find("division").text

            building = node.find("building").text

            room = node.find("room").text

            datatframe = datatframe.append(
                pd.Series([firstname, lastname, title, division, building, room], index=columns), ignore_index=True)