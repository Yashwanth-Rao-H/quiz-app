import sqlite3


def clear_questions():
    try:
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('drop table questions')
        conn.commit()
        print("All Questions from DB are deleted!!!")
    except Exception as e:
        print("Error Occured\n\n", e)


if __name__ == "__main__":
    clear_questions()
