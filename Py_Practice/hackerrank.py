# n = 22
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and n >= 2 and n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and n >= 6 and n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")

# n = 3
# for i in range(0, n):
#     print(i**2)

# if (n % 2 != 0):
#         print("Weird")
#     else:
#         if n>=2 and n<=5:
#             print("Not Weird")
#         elif n<=20:
#             print("Weird")
#         else:
#             print("Not Weird")



# year = 1990

# if year % 100 == 0 and year % 400 == 0:
#     print(True)
# elif year % 100 == 0:
#     print(False)
# elif year % 4 == 0:
#     print(True)


# n = 5
# i = 0

# for i in range(1, n + 1):
#     print(i, end="")
# # 12345

# n = 5
# arr = [2,3,6,6,5]
# print(arr)
# arr_unique = list(dict.fromkeys(arr))
# print(arr_unique)
# arr_unique.sort()
# print(arr_unique)
# print(arr_unique[-2])



# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# students.sort(key=lambda l: l[1])
# print(students)

# def secondLowestMarks(students):
#     lowest_mark = min(students, key = lambda stu: stu[1])[1];
#     students = [stu for stu in students if stu[1] != lowest_mark]
#     #filter(lambda stu: stu[1] == lowest_mark, students);
#     second_lowest_mark = min(students, key = lambda stu: stu[1])[1];
#     return sorted([stu[0] for stu in students if stu[1] == second_lowest_mark]);

# def secondLowestMarks2(students):
#     "If there's a tie for lowest mark we include all."
#     students.sort();
#     picked_students = sorted(filter(lambda x: x[1] == students[1][1], students));
#     return [stu[0] for stu in picked_students];

# if __name__ == "__main__":
#     num_students = int(input());
#     students = [[input(),float(input())] for i in range(num_students)];
#     for student in secondLowestMarks(students):
#         print(student);
        