import pandas as pd
import sqlite3

def add_question():
    questions = pd.read_csv('questions.csv')
    if questions.isnull().sum().sum() != 0:
        print("All Columns and Rows should be Filled in the excel File.")
        return
    else:
        try:

            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS questions(question text, op1 text, op2 text, op3 text, op4 text, ans text, lvl int)')
            try:
                for ind in questions.index:
                    question = questions['question'][ind]
                    op1 = str(questions['op1'][ind])
                    op2 = str(questions['op2'][ind])
                    op3 = str(questions['op3'][ind])
                    op4 = str(questions['op4'][ind])
                    ans = str(questions['ans'][ind])
                    lvl = int(questions['lvl'][ind])
                    create.execute("INSERT INTO questions VALUES (?,?,?,?,?,?,?)",(question, op1, op2, op3, op4, ans, lvl)) 
            except Exception as e:
                print(f"Error Occured Adding Question : \nQuestion: {question}\nOption 1: {op1}\nOption 2: {op2}\nOption 3: {op3}\nOption 4: {op4}\nAns: {ans}\nLevel: {lvl}" )
            conn.commit()
            print("All Questions have been added !!!")
        except Exception as d:
            print(f"Error Occured : \n{d}")

if __name__ == "__main__":
    try:
        add_question()
    except Exception as e:
        print(e)
    finally:
        x = input("Enter any key to continue...")