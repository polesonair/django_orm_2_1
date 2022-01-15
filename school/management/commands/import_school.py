import json
from django.core.management.base import BaseCommand
from school.models import Teacher, Student

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('school.json')as f:
            templates = json.load(f)

        for i in templates:
            if i.get('model') == 'school.teacher':
                Teacher.objects.create(id=i.get('pk'), name=i.get('fields').get('name'), subject=i.get('fields').get('subject'))

        for i in templates:
            if i.get('model') == 'school.student':
                Student.objects.create(id=i.get('pk'), name=i.get('fields').get('name'), group=i.get('fields').get('group'), teacher_id=i.get('fields').get('teacher'))


