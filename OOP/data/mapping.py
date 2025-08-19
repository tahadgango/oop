from collections import defaultdict
import json

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
    progDict[str(len(progDict)+1)] = p

for p in subjects:
    subDict[str(len(subDict)+1)] = p

progToid = {v: k for k, v in progDict.items()}
subToid = {v: k for k, v in subDict.items()}


# subject -> program
subToProgs = defaultdict(list)

# assigning subject to prog (by id)
for p in EngineerProg + BusinessProg:
    subToProgs[subToid["calculus"]].append(progToid[p])

for p in EngineerProg:
    subToProgs[subToid["linear algebra"]].append(progToid[p])
    subToProgs[subToid["physics"]].append(progToid[p])

for p in BusinessProg:
    subToProgs[subToid["finance"]].append(progToid[p])
    subToProgs[subToid["accounting"]].append(progToid[p])

subToProgs[subToid["programming"]].append(progToid["software engineering"])
subToProgs[subToid["e-commerce"]].append(progToid["marketing"])
subToProgs[subToid["trading"]].append(progToid["international trade"])


s = defaultdict(list)
for p in EngineerProg:
    s["engineering"].append(p)
for p in BusinessProg:
    s["business"].append(p)
with open("data/departments.json", "w") as f:
    json.dump(s, f, indent=4)

s = {}
for id, p in progDict.items():
    s[id] = {"prog": p}
    if p in EngineerProg:
        s[id]["dept"] = "engineering"
    elif p in BusinessProg:
        s[id]["dept"] = "business"

with open("data/programs.json", "w") as f:
    json.dump(s, f, indent=4)


s = {}
for id, progs in subToProgs.items():
    s[id] = {"sub": subDict[id], "Pids": progs}

with open("data/subjects.json", "w") as f:
    json.dump(s, f, indent=4)
