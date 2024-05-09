import sqlite3 as sql


connection = sql.connect("Oquv_kursi.db")
cursor = connection.cursor()

# print(cursor.execute("SELECT*FROM ish_joy_kerak").fetchall() )   

def main():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kurs_qoshish (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomi VARCHAR(100),
                narxi INTEGER,
                full_data TEXT,
                teacher VARCHAR(100)
        )               
    """)

    connection.commit()

print(cursor.execute("SELECT*FROM kurs_qoshish").fetchall())  

def create_user(*args):
    """
    args - bu funksiya qabul qilayotgan foydalanuvchi ma'lumotlar to'plami
    """
    sql = '''INSERT INTO kurs_qoshish(nomi,narxi,full_data, teacher)
        VALUES(?, ?, ?, ?)
    '''
    cursor.execute(sql, args)

    connection.commit()

def get_data():
    return cursor.execute("SELECT nomi FROM kurs_qoshish").fetchall()
def get_info():
    data = cursor.execute("SELECT nomi, narxi, full_data, teacher FROM kurs_qoshish").fetchall()
    for row in data:
        print("Nomi:", row[0])
        print("Narxi:", row[1])
        print("Full ma'lumot:", row[2])
        print("O'qituvchi:", row[3])
        print("-----------------------")
def get_course_info(course_id):
    # Assuming you have a SQLite database connection and cursor already defined
    cursor.execute("SELECT nomi, narxi, full_data, teacher FROM kurs_qoshish WHERE id=?", (course_id,))
    course = cursor.fetchone()
    return course if course else None
if __name__=="__main__":
    main()