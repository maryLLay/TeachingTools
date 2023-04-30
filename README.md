# TeachingTools

Package of tools for those teaching or those being taught.

Quiz.py
This program will quiz you on whatever questions you place in the quiz bank.  
Acceptable question types are multiple choice, fill-in-the-blank, and True/False.  Multiple choice questions will have randomly-sorted answers.

Proper formatting of the .csv file containing the quiz material is essential.
This program assumes the following format:
First row = column headers
Remaining rows:
Question, Possible answers (4 columns), Extra information, Answer, Explanation

The "Extra information" column may include situational context, a sample program, or other example information relating to the question.


Troubleshooting:

If answers appear blank:
1. apple
2.    
3. banana

-then '.' is required in the answer columns of the .csv file


If the following message appears: "Program error: no matching answer found.  Check your answer key."
-then the item in the answer column does not match any of the possible answers.  This is most likely due to a spelling or capitalization error.  
I should be able to fix some of these errors later, but ideally your answer column should be a copy and paste from the Possible answers columns.
