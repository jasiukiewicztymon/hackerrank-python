student, note, out = [], [], []
for _ in range(int(input())):
    name = input()
    grade = float(input())
    if grade not in note:
        note.append(grade)
    student.append([name, grade])
    
note.sort()
wanted = 0
for _ in note:
    if _ != note[0]:
        wanted = _
        break
    
for _ in student:
    if _[1] == wanted:
        out.append(_[0])
        
out.sort()
for _ in out:
    print(_)
