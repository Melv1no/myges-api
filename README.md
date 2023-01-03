
# Myges python api




## Setup

To setup this project provide your .env file

```text
USERNAME=
PASSWORD=""
URL="https://authentication.kordis.fr/oauth/authorize?response_type=token&client_id=skolae-app"
```
don't touch to URL


## Usage/Examples

```python
from MyGesAPI import *

print(getProfile())
```
```python
from MyGesAPI import *

print(getAbsences("2022"))
```
All return is in Json, you can easly parse like this

(issued of parseTeachers() function)
```
def parseTeachers():
  teachers = json.loads(getTeachers("2022"))
  for teacher in teachers["result"]:
    print(teacher["email"])
    print(teacher["firstname"])
    print(teacher["lastname"])
    for information in teacher["links"]:
      if information["rel"] == "photo":
        print(information["href"])


        THIS return you 
        x@x.x
        firstnameofyourteacher
        lastnameofyourteacher
        ppofyourteacher
```




## function
getAgenda\
getProfile\
getBanner\
getNews\
getGrades\
getAbsences\
getTeachers\
getClasses\
getClassesStudents\
getStudents\
getCourses\
getClassesID\
getStudentID\
parseTeachers\
parseClassesStudents\
parseStudents\
parseAgenda\

You can obtains ``years`` by self define and ``studentID``,``ClassesID`` with getStudentID() & getClassesID()





