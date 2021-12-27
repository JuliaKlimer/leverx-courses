import imghdr
import os
import xml.etree.cElementTree as et
import mysql.connector
from mysql.connector import Error
import json


class IDeserializer:
    def __init__(self):
        pass

    def deserialize(self, file_name):
        raise Exception("NotImplementedException")

class ISerializerJson:
    def __init__(self):
        pass

    def serialize_json(self, file_name, result_file):
        raise Exception("NotImplementedException")

class ISerializerXML:
    def __init__(self):
        pass

    def serialize_xml(self, file_name, result_file):
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

class Students(IDeserializer, ISerializerJson, ISerializerXML, IPath, IFormat):
    def deserialize(self, file_name):
        students_open = open(file_name, )
        students_json = json.load(students_open)
        return students_json

    def serialize_json(self, file_name, result_file):
        grouped_list = []
        for rooms_data in file_name:
            rooms_data["students"] = grouped_list[rooms_data["id"]]
            with open(result_file, 'w') as write_file:
                return json.dump(grouped_list, write_file)

    def serialize_xml(self, file_name, result_file):
        grouped_list = []
        for rooms_data in file_name:
            rooms_data["students"] = grouped_list[rooms_data["id"]]
            grouped_list_xml = et.tostring(grouped_list)
            with open(result_file, 'w') as write_file:
                return write_file.write(grouped_list_xml)

    def full_path(self, file_name):
        return os.path.abspath(file_name)

    def define_format(self, file_name):
        return imghdr.what(file_name)

class Rooms(IDeserializer, ISerializerJson, ISerializerXML, IPath, IFormat):
    def deserialize(self, file_name):
        rooms_open = open(file_name, )
        rooms_json = json.load(rooms_open)
        return rooms_json

    def serialize_json(self, file_name, result_file):
        grouped_list = []
        for rooms_data in file_name:
            rooms_data["students"] = grouped_list[rooms_data["id"]]
            with open(result_file, 'w') as write_file:
                return json.dump(grouped_list, write_file)

    def serialize_xml(self, file_name, result_file):
        grouped_list = []
        for rooms_data in file_name:
            rooms_data["students"] = grouped_list[rooms_data["id"]]
            grouped_list_xml = et.tostring(grouped_list)
            with open(result_file, 'w') as write_file:
                return write_file.write(grouped_list_xml)


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("localhost", "root", "")

def add_rooms(args, data):
    connect, cursor = create_connection(args)
    with connect:
        for i in data:
            try:
                cursor.execute("INSERT Rooms(RoomID) VALUES ({});".format(int(i)))
            except Error as e:
                print(f"The error '{e}' occurred")
            connect.commit()

def add_students(args, data):
    connect, cursor = create_connection(args)
    query = "INSERT Students(StudentID, sex, name, birthday, RoomID) VALUES (%s, %s, %s, %s, %s);"
    with connect:
        for i in data:
            try:
                cursor.execute(query, [i["id"],i["sex"],i["name"],i["birthday"],i["room"]])
            except Error as e:
                print(f"The error '{e}' occurred")
            connect.commit()

def top_5_minimum_average_age(args):
    connect, cursor = create_connection(args)
    query =  '''SELECT rooms.RoomID, avg(datediff(CURDATE(), students.birthday)) as Age
              FROM rooms JOIN students
              ON rooms.RoomID = students.RoomID 
              GROUP BY rooms.RoomID
              ORDER by Age ASC
              LIMIT 5'''
    with connect:
        cursor.execute(query)
        student_list = cursor.fetchall()
    return student_list

def top_5_maximum_different_age(args):
    connect, cursor = create_connection(args)
    query = '''SELECT rooms.RoomID, datediff(max(students.birthday), min(students.birthday)) as Difference 
              FROM rooms join students
              ON rooms.RoomID = students.RoomID 
              GROUP BY rooms.RoomID
              ORDER by Difference DESC
              LIMIT 5'''
    with connect:
        cursor.execute(query)
        student_list = cursor.fetchall()
    return student_list

def different_sex(args):
    connect, cursor = create_connection(args)
    query = '''SELECT rooms.RoomID, count(DISTINCT students.sex) AS Counter
              FROM rooms JOIN students
              ON rooms.RoomID = students.RoomID
              GROUP BY rooms.RoomID
              HAVING Counter > 1'''
    with connect:
        cursor.execute(query)
        student_list = cursor.fetchall()
    return student_list