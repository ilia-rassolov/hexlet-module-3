import json
import sys
import uuid


class SchoolRepository:
    def __init__(self):
        self.schools = json.load(open("data/schools.json", 'r'))

    def get_content(self):
        return self.schools

    def find(self, id):
        try:
            for school in self.schools:
                if id == str(school['id']):
                    return school
        except KeyError:
            sys.stderr.write(f'Wrong post id: {id}')
            raise

    def save(self, new_school):
        # repository should know nothing about validation in outer layer
        if not (new_school.get('name')):
            raise Exception(f'Wrong data: {json.loads(new_school)}')
        # replace already existed user
        if new_school.get('id'):
            for current in self.schools:
                if new_school['id'] == current['id']:
                    self.schools.remove(current)
                    break
            self.schools.append(new_school)
        # or add new
        else:
            new_school['id'] = str(uuid.uuid4())
            self.schools.append(new_school)
        with open("data/schools.json", "w") as f:
            json.dump(self.schools, f)
        return new_school['id']

    def destroy(self, id):
        school = self.find(id)
        self.schools.remove(school)
        with open("data/schools.json", "w") as f:
            json.dump(self.schools, f)
