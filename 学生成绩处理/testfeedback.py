import csv
import xlrd

"""
scorezonea = input("请输入优秀学生最低分\n")
scorezonetexta = str(input("请输入此分数段对应文案\n"))
scorezoneb = input("请输入良好学生最低分\n")
scorezonetextb = str(input("请输入此分数段对应文案\n"))
scorezonec = input("请输入中等学生分数段\n")
scorezonetextc = str(input("请输入此分数段对应文案\n"))
scorezonetextd = str(input("请输入差等生对应文案\n"))
"""
with open('学生成绩.xlsx', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('反馈文案.xlsx','r') as x:
	feed_back_text = csv.reader(x)
	back_text = list(feed_back_text)
	scorezonea = back_text[0][0]
	scorezonetexta = str(back_text[0][1])
	scorezoneb = back_text[1][0]
	scorezonetextb = str(back_text[1][1])
	scorezonec = back_text[2][0]
	scorezonetextc = str(back_text[2][1])
	scorezoned = back_text[3][0]
	scorezonetextd = str(back_text[3][1])
for line in texts:
	if line[1] > scorezonea:
		print(scorezonetexta.replace('姓名',line[0]).replace('成绩',line[1]))
	elif line[1] > scorezoneb:
		print(scorezonetextb.replace('姓名',line[0]).replace('成绩',line[1]))
	elif line[1] > scorezonec:
		print(scorezonetextc.replace('姓名',line[0]).replace('成绩',line[1]))
	else:
		print(scorezonetextd.replace('姓名',line[0]).replace('成绩',line[1]))

