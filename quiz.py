#Review Quiz
#assumes csv format: Question, Possible answers (4 columns), Extra Info (chart, example, etc), Answer, Explanation
#For multiple choice, include a '.' if fewer than 4 answers exist
#For fill-in-the-blank questions, put '.' in all Possible answer columns


import random
import csv

stop = ' '
right = 0
wrong = 0

#Open and read csv file
myfile = r'/Users/your/path/here.csv'
with open(myfile) as datafile:
    datareader = csv.reader(datafile)
    data = []
    for row in datareader:
        data.append(row)      

while stop != 'exit':
    #Generate random number
    random_int = random.randint(1, len(data)-1)

    #Generate question
    row = data[random_int]
    question = row[0]
    answer = row[-2]
    explanation = row[-1]
    print(question)

    #Generate and shuffle answers
    answers = []
    ans_num = 0
    
    #1. Questions that include extra info
    if row[5] != '':
        extra_info = row[5]
        print(extra_info)
        print()
    #2. Questions that are T/F
    elif row[1] == 'TRUE':
        answers = ['TRUE', 'FALSE']
    #3. Questions that are MC or fill-in-the-blank
    else:
        for i in range(1, len(row)-3):
            if data[random_int][i] != '.':
                answers.append(data[random_int][i])
        random.shuffle(answers)
        
    for i, x in enumerate(answers):
        print(f'{i+1}: {x}')
        if x == answer:
            ans_num = str(i+1) #gets the number of the correct answer
    if ans_num == 0:
        print("Program error: no matching error found.  Check your answer key.")
            
    #Get user_answer
    print()
    user_ans = input()

    #Check answer
    if (user_ans == answer) or (user_ans == ans_num):
        print("Correct!")
        print()
        right +=1

    else:
        print("Wrong :(")
        print(explanation)
        print()
        wrong +=1

    stop = input("Hit Enter to continue, or 'exit' to quit: ")
    print()

#Calculate score
totalQs = right + wrong
pct_right = (right / totalQs)*100
print(f'You answered {totalQs} questions and scored {pct_right}%')
