import csv
import time
import random

start_time = time.time()

print("[1/4] - "+str(round(int(time.time()-start_time),3))+" | Importing the file")

questions = []
answers = []
wins = []
totals = []
values = []

with open('Culture Générale/questions.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    next(csvreader)
    for row in csvreader:
        question, answer, win, total = row
        questions.append(question)
        answers.append(answer)
        wins.append(int(win))
        totals.append(int(total))
