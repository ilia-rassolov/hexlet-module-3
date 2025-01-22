import random

from faker import Faker

SEED = 1234


def generate_courses(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(1, users_count))
    random.seed(SEED)
    random.shuffle(ids)

    courses = []

    for i in range(users_count - 1):
        courses.append({
            'id': ids[i],
            'name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.free_email(),
        })

    return courses
