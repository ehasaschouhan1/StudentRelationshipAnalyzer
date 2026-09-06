import sqlite3


class Database:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    # =========================================================
    # CREATE TABLES
    # =========================================================

    def create_tables(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll TEXT UNIQUE NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS relations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_a INTEGER NOT NULL,
                student_b INTEGER NOT NULL,
                UNIQUE(student_a, student_b),
                FOREIGN KEY(student_a)
                    REFERENCES students(id)
                    ON DELETE CASCADE,
                FOREIGN KEY(student_b)
                    REFERENCES students(id)
                    ON DELETE CASCADE
            )
        """)

        connection.commit()
        connection.close()

    # =========================================================
    # ADD STUDENT
    # =========================================================

    def add_student(self, name, roll):
        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO students (name, roll) VALUES (?, ?)",
                (name, roll)
            )

            connection.commit()

            student_id = cursor.lastrowid

            connection.close()

            return student_id

        except sqlite3.IntegrityError:
            connection.close()
            return None

    # =========================================================
    # GET ALL STUDENTS
    # =========================================================

    def get_students(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, roll
            FROM students
            ORDER BY id
        """)

        students = cursor.fetchall()

        connection.close()

        return students

    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(self, student_id):
        connection = self.connect()
        connection.execute("PRAGMA foreign_keys = ON")

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        connection.close()

    # =========================================================
    # ADD RELATION
    # =========================================================

    def add_relation(self, student_a, student_b):
        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO relations (student_a, student_b)
                VALUES (?, ?)
                """,
                (student_a, student_b)
            )

            connection.commit()

            relation_id = cursor.lastrowid

            connection.close()

            return relation_id

        except sqlite3.IntegrityError:
            connection.close()
            return None

    # =========================================================
    # GET ALL RELATIONS
    # =========================================================

    def get_relations(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                relations.id,
                students_a.name,
                students_a.roll,
                students_b.name,
                students_b.roll,
                relations.student_a,
                relations.student_b
            FROM relations
            JOIN students AS students_a
                ON relations.student_a = students_a.id
            JOIN students AS students_b
                ON relations.student_b = students_b.id
            ORDER BY relations.id
        """)

        relations = cursor.fetchall()

        connection.close()

        return relations

    # =========================================================
    # DELETE RELATION
    # =========================================================

    def delete_relation(self, relation_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM relations WHERE id = ?",
            (relation_id,)
        )

        connection.commit()
        connection.close()

    # =========================================================
    # CLEAR DATABASE
    # =========================================================

    def clear_all(self):
        connection = self.connect()
        connection.execute("PRAGMA foreign_keys = ON")

        cursor = connection.cursor()

        cursor.execute("DELETE FROM relations")
        cursor.execute("DELETE FROM students")

        connection.commit()
        connection.close()