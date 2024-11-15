# GPA (grade point average)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gpa = [0,0,0,0,0]
# К сожалению, самостоятельно с циклами в Пайтоне разобраться не удалось, подожду видео
gpa[0] = sum(grades[0])/len(grades[0])
gpa[1] = sum(grades[1])/len(grades[1])
gpa[2] = sum(grades[2])/len(grades[2])
gpa[3] = sum(grades[3])/len(grades[3])
gpa[4] = sum(grades[4])/len(grades[4])
alpha=list(students)
alpha.sort()
dict = {alpha[0] : gpa[0],
        alpha[1] : gpa[1],
        alpha[2] : gpa[2],
        alpha[3] : gpa[3],
        alpha[4] : gpa[4],}
print(dict)