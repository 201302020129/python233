"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
texts = []
calls = []
count_nums = []
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
for call in calls:
	count_nums.append(call[0])
	count_nums.append(call[1])
for text in texts:
	count_nums.append(text[0])
	count_nums.append(text[1])

print("There are {} different telephone numbers in the records.".format(len(set(count_nums))))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
