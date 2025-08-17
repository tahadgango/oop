from datetime import date
from collections import defaultdict

#lists of programs
EngineerProg = ["software engineering", "civil engineering", "electrical engineering"]
BusinessProg = ["economy", "international trade", "marketing"]

#list of subjects
subjects = ["calculus", "linear algebra", "physics", "finance", "accounting", "programming", "e-commerce", "trading"]


# ids <-> programs
progDict = {}
progToid = {}

#ids <-> subjects
subDict = {}
subToid = {}


for p in EngineerProg + BusinessProg:
    progDict[len(progDict)+1] = p

for p in subjects:
    subDict[len(subDict)+1] = p

progToid = {v: k for k, v in progDict.items()}
subToid = {v: k for k, v in subDict.items()}


# subject -> program
subToProg = defaultdict(list)

# assigning subject to prog (by id)
for p in EngineerProg + BusinessProg:
    subToProg[subToid["calculus"]].append(progToid[p])

for p in EngineerProg:
    subToProg[subToid["linear algebra"]].append(progToid[p])
    subToProg[subToid["physics"]].append(progToid[p])

for p in BusinessProg:
    subToProg[subToid["finance"]].append(progToid[p])
    subToProg[subToid["accounting"]].append(progToid[p])

subToProg[subToid["programming"]].append(progToid["software engineering"])
subToProg[subToid["e-commerce"]].append(progToid["marketing"])
subToProg[subToid["trading"]].append(progToid["international trade"])


# count number of student in each (major, grade)
studentCounter = defaultdict(int)


class Depart:
    def __init__(self):
        self.students = []
        self.teachers = []
        super().__init__()

    def add(self, user):
        if isinstance(user, Student):
            self.students.append(user)
        else:
            self.teachers.append(user)

    def remove(self, user):
        if isinstance(user, Student):
            self.students.remove(user)
        else:
            self.teachers.remove(user)

class EngDepart(Depart):
    def __init__(self):
        super().__init__()
        
class BusDepart(Depart):
    def __init__(self):
        super().__init__()


eng = EngDepart()
bus = BusDepart()


class DepartRegistry:
    numOfDept = 0
    def __init__(self):
        DepartRegistry.numOfDept += 1

        self.departments = {
                        "engineering": eng,
                        "business": bus
                    }
        
        self.progToDept = {}

        for p in EngineerProg:
            self.progToDept[progToid[p]] = "engineering"


        for p in BusinessProg:
            self.progToDept[progToid[p]] = "business"

        super().__init__()

    def findDept(self, id):
        dept = self.progToDept[id]
        return self.departments[dept]

    

class RegistryStudent(DepartRegistry):
    def __init__(self):
        super().__init__()
 
    def register_student(self, student):
        self.findDept(student.program_id).add(student)

    def change_register(self, student, old_id):
        oldDept = self.findDept(old_id)
        if oldDept == self.findDept(student.program_id):
            return
        
        oldDept.remove(student)
        self.register_student(student)


class RegistryTeacher(DepartRegistry):
    def __init__(self):
        super().__init__()


    def register_teacher(self, teacher):
        progs = set()
        seen2 = set()

        for sub in teacher.subjects:
            progsOfsub = subToProg[sub]
                
            for prog in progsOfsub:    
                progs.add(prog)

        for p in progs:
            dept = self.findDept(p)

            if dept not in seen2:
                dept.add(teacher)

            seen2.add(dept)
            if len(seen2) == DepartRegistry.numOfDept:
                break
    

def yearOfStudy():
    y = date.today().year
    m = date.today().month

    if 0 < m <= 6:              # register at this period is in last year program
        return y - 1
    else: return y


def len3str(n):
    id = str(n)
    return "0"* (3 - len(id)) + id

class Student:
    numOfStus = 0
    registry = RegistryStudent()
    
    def __str__(self):
        return f"Student: {self.name}, major: '{progDict[self.program_id]}', Student Number: {self.studentNum}"

    def __init__(self, name = "", grade = 0, program = ""):

        Student.numOfStus += 1
        self.name = name
        self.grade = grade

        try:
            self.program_id = progToid[program]
        except KeyError:
            raise(f"invalid program name ({program})")

        cur_count = studentCounter[(self.program_id, grade)] + 1
        studentCounter[((self.program_id, grade))] = cur_count

        # student number: (year of program departure) + (program id) + (registration order)
        self.studentNum = int(str(yearOfStudy() - grade + 1) + len3str(self.program_id) + len3str(cur_count))
    
        Student.registry.register_student(self)
    
    def changeProg(self, newProg):
        old_id = self.program_id
        self.program_id = progToid[newProg]
        studentCounter[(old_id, self.grade)] -= 1
        studentCounter[(self.program_id, self.grade)] += 1
        self.studentNum = int(str(self.studentNum)[:4] + len3str(self.program_id) + len3str(studentCounter[(self.program_id, self.grade)]))
        Student.registry.change_register(self, old_id)
        
            
class Teacher:
    numOfTeas = 0
    registry = RegistryTeacher()

    def __str__(self):
        return f"Teacher: {self.name}, salary: {[subDict[s] for s in self.subjects]}"

    def __init__(self, name = "", salary = 0, subjects = []):

        Teacher.numOfTeas += 1

        self.name = name
        self.salary = salary
        self.subjects = [subToid[subject] for subject in subjects]
        
        Teacher.registry.register_teacher(self)

    

s1 = Student("Taha", 1, "software engineering")
s2 = Student("Marwan", 3, "software engineering")
s3 = Student("saad", 1, "economy")
s4 = Student("abdo", 1, "software engineering")

t1 = Teacher("abdul", 100000, ["programming", "physics"])
t2 = Teacher("bu", 20, ["linear algebra", "calculus"])
t3 = Teacher("xiao", 10, ["trading", "e-commerce"])

print(t1.subjects)

for s in bus.students:
    print(s, end = ' ')
for s in eng.students:
    print(s, end = ' ')

print("\n")

for t in bus.teachers:
    print(t, end = ' ')

for t in eng.teachers:
    print(t, end = ' ')

print("\n")

s1.changeProg("economy")
print(s1)