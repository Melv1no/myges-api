
# Myges python api




## Installation

Reseigner vos identifiant Myges dans le fichier .env

```text
USERNAME=
PASSWORD=""
URL="https://authentication.kordis.fr/oauth/authorize?response_type=token&client_id=skolae-app"
```
Pour l'URL ne changer rien, sauf si vous savez ce que vous faite (: !


## Exemples d'utilisation

```python
from MyGesAPI import *

print(getProfile())
```
```python
from MyGesAPI import *

print(getAbsences("2022"))
```
Les fonctions renvoie du json, facilement 'parsable'.
(Fonction déjà présente dans MyGesAPI)
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


        Sa donne quelque chose comme ça
        x@x.x
        firstnameofyourteacher
        lastnameofyourteacher
        ppofyourteacher
```




## Listes des fonctions existante
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

Vous pouvez trouvez les paramètre de fonction ``studentID`` et ``ClasseID`` avec les fonctions getStudentID() & getClassesID()





