import psycopg2
from psycopg2.extras import NamedTupleCursor
from dataclasses import dataclass
from typing import Optional

conn = psycopg2.connect(dbname='hexlet', user='user')


def commit(conn):
    conn.commit()


def save_course(conn, course):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        if course.id is None:
            cur.execute(
                "INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;",
                (course.name, course.description)
            )
            course.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE courses SET name = %s, description = %s WHERE id = %s;",
                (course.name, course.description, course.id)
            )
    return course.id


def find_course(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses WHERE id = %s;", (course_id,))
        result = cur.fetchone()
        if result:
            return Course(
                id=result.id,
                name=result.name,
                description=result.description
                )
    return None


def get_all_courses(conn):
    courses = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses;")
        for row in cur.fetchall():
            courses.append(Course(
                    id=row.id,
                    name=row.name,
                    description=row.description
                    ))
        return courses


@dataclass
class Course:
    name: str
    description: str
    id: Optional[int] = None


@dataclass
class Lesson:
    name: str
    text: str
    course_id: int
    id: Optional[int] = None

# BEGIN (write your solution here)
def save_lesson(conn, lesson):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        if lesson.id:
            curs.execute("UPDATE lessons SET name = %s, text = %s, course_id = %s);",
                         (lesson.name, lesson.text, lesson.course_id))
        else:
            curs.execute("INSERT INTO lessons (name, text, course_id) VALUES (%s, %s, %s)) RETURNING id;",
                         (lesson.name, lesson.text, lesson.course_id))
            lesson['id'] = curs.fetchone().id
            return lesson['id']


def find_lesson(conn, lesson_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute("SELECT * FROM lessons WHERE id = %s", (lesson_id,))
        result = curs.fetchone()
        return Lesson(id=result.id, name=result.name, text=result.text, course_id=result.course_id)

def get_course_lessons(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute("SELECT * FROM lessons WHERE course_id =%s",
                     (course_id,))
        result = curs.fetchall()
        return list(map(lambda lesson: Lesson(id = lesson.id, name=lesson.name, text=lesson.text,
                                         course_id=lesson.course_id), result))

# END

print(find_lesson(conn, 4))
print(get_course_lessons(conn, 7))