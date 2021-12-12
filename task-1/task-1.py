import json
import xml.etree.cElementTree as et
import os
import imghdr

class IDeserializer:
    def __init__(self):
        pass

    def deserialize(self, file_name):
        raise Exception("NotImplementedException")

class IPath:
    def __init__(self):
        pass

    def full_path(self, file_name):
        raise Exception("NotImplementedException")

class IFormat:
    def __init__(self):
        pass

    def define_format(self, file_name):
        raise Exception("NotImplementedException")

class Students(IDeserializer, IPath, IFormat):
    def deserialize(self, file_name):
        students_open = open(file_name, )
        students_json = json.load(students_open)
        return students_json

    def full_path(self, file_name):
        return os.path.abspath(file_name)

    def define_format(self, file_name):
        return imghdr.what(file_name)

class Rooms(IDeserializer, IPath, IFormat):
    def deserialize(self, file_name):
        rooms_open = open(file_name, )
        rooms_json = json.load(rooms_open)
        return rooms_json

    def full_path(self, file_name):
        return os.path.abspath(file_name)

    def define_format(self, file_name):
        return imghdr.what(file_name)

def group_students_serializer_json(student_list, rooms_list, result_file):
    grouped_list = []
    for students_data in student_list:
        student_room = students_data["room"]
        grouped_list = [student_room].append(students_data)
    for rooms_data in rooms_list:
        rooms_data["students"] = grouped_list[rooms_data["id"]]
        with open(result_file, 'w') as write_file:
            return json.dump(grouped_list, write_file)

def group_students_serializer_xml(student_list, rooms_list, result_file):
    grouped_list = []
    for students_data in student_list:
        student_room = students_data["room"]
        grouped_list = [student_room].append(students_data)
    for rooms_data in rooms_list:
        rooms_data["students"] = grouped_list[rooms_data["id"]]
        grouped_list_xml = et.tostring(grouped_list)
        with open(result_file, 'w') as write_file:
            return write_file.write(grouped_list_xml)