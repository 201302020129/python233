stu_names = input("stu_name: \n").split(",")
stu_homeworks = input("stu_homework: \n").split(",")
stu_greads = input("stu_gread: \n").split(",")

massage = "Hi {},\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date."
for stu_name,stu_homework,stu_gread in zip(stu_names,stu_homeworks,stu_greads):
	print(massage.format(stu_name,stu_homework,stu_gread,int(stu_homework) * 2 + int(stu_gread)))
