import requests
import json
import re
import base64
import dotenv
import time
from datetime import datetime, timedelta

dotenv.load_dotenv()


def hash(userpass):
   return base64.b64encode(userpass.encode('ascii'))


def getSession():
  url = dotenv.get_key(".env","URL")
  username = dotenv.get_key(".env","USERNAME")
  password = dotenv.get_key(".env","PASSWORD")
  user_token = hash(username+":"+password).decode('utf-8')
  header = {'Authorization' : "Basic {}".format(user_token)}

  req = requests.get(url,headers=header,allow_redirects=False)
  resp = req.headers.get('location')
  parse_token = re.search('comreseaugesskolae:/oauth2redirect#access_token=(.*)&token_type=bearer',resp)
  token = parse_token.group(1)
  return token


def getProfile():
  url = "https://api.kordis.fr/me/profile"
  req = requests.get(url,headers=header)
  return req.text


def getAgenda():
  today = datetime.today()
  start = today.replace(day=1)
  end = start.replace(month=today.month + 2)
  start = int(start.timestamp()) * 1000
  end = int(end.timestamp()) * 1000
  url = "https://api.kordis.fr/me/agenda?start={0}&end={1}".format(start, end)
  req = requests.get(url,headers=header)
  return req.text

def getBanner():
  url = "https://api.kordis.fr/me/news/banners"
  req = requests.get(url,headers=header)
  return req.text


def getNews(page):
  url = "https://api.kordis.fr/me/news?page={}".format(page)
  req = requests.get(url,headers=header)
  return req.text


def getGrades(years):
  url = "https://api.kordis.fr/me/{}/grades".format(years)
  req = requests.get(url,headers=header)
  return req.text


def getAbsences(years):
  url = "https://api.kordis.fr/me/{}/absences".format(years)
  req = requests.get(url,headers=header)
  return req.text


def getTeachers(years):
  url = "https://api.kordis.fr/me/{}/teachers".format(years)
  req = requests.get(url,headers=header)
  return req.text


def getClasses(years):
  url = "https://api.kordis.fr/me/{}/classes".format(years)
  req = requests.get(url,headers=header)
  return req.text


def getClassesStudents(classe_id):
  url = "https://api.kordis.fr/me/classes/{}/students".format(classe_id)
  req = requests.get(url,headers=header)
  return req.text


def getStudents(student_id):
  url = "https://api.kordis.fr/me/students/{}".format(student_id)
  req = requests.get(url,headers=header)
  return req.text


def getCourses(years):
  url = "https://api.kordis.fr/me/{}/courses".format(years)
  req = requests.get(url,headers=header)
  return req.text


def getClassesID():
  classes = json.loads(getClasses("2022"))
  for classe in classes["result"]:
    return classe["puid"]


def getStudentID():
  students = json.loads(getProfile())
  return students["result"]["uid"]


def parseTeachers():
  teachers = json.loads(getTeachers("2022"))
  for teacher in teachers["result"]:
    print(teacher["email"])
    print(teacher["firstname"])
    print(teacher["lastname"])
    for information in teacher["links"]:
      if information["rel"] == "photo":
        print(information["href"])


def parseClassesStudents(classe_id):
  students = json.loads(getClassesStudents(classe_id))
  for student in students["result"]:
    print(student["email"])
    print(student["firstname"])
    print(student["lastname"])
    for information in student["links"]:
      if information["rel"] == "photo":
        print(information["href"])


def parseStudents(student_id):
  student = json.loads(getStudents(student_id))
  print(student["result"]["email"])
  print(student["result"]["firstname"])
  print(student["result"]["lastname"])
  print(student["result"]["_links"]["photo"]["href"])


def parseAgenda():
  courses = json.loads(getAgenda())
  for course in courses["result"]:
    print(course["type"])
    print(course["modality"])
    print(course["start_date"])
    print(course["end_date"])
    print(course["name"])
    if course["rooms"] != None:
      print(course["rooms"][0]["name"])
      print(course["rooms"][0]["floor"])
      print(course["rooms"][0]["campus"])
    if course["discipline"] != None:
      print(course["discipline"]["teacher"])
      print(course["discipline"]["trimester"])


header = {'Authorization' : "Bearer {}".format(getSession())}
print(parseAgenda())