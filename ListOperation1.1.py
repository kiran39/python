#Given the names and grades for each student in a clas of N students, store them in a nested the names of any students
#having the second lowest grade
# Note:- If there are multiple students with the second lowest grade order their names alphabetically print each name on new
#line

#Example: records = [["Chi", 20.0], ["beta", 50.0], ["alpha", 50.0]] second lowest score is 50.0 and there are
#two students with that score ["beta", "alpha"]

#o\p
#alpha
#beta

if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        d[name] = grade
    marks = d.values()
    secondLeast = sorted(list(set(marks)))[1]
    secondLowest = []
    for key, value in d.items():
        if value == secondLeast:
            secondLowest.append(key)
    secondLowest.sort()
    for name in secondLowest:
        print(name)