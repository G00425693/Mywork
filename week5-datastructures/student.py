# messing with lists and dictionary
# program should store students name, list of her courses and grades in a dict and print out her data
# Author: Audrey Fitzgerald

student = { "name":"Mary","modules": [
        [{"courseName":"Programming", "grade": 45},
        {"courseName":"History", "grade":99}]}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
