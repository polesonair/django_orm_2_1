from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name='students')
    # Создали связь Многие-Ко-Многим. Связываемся с моделью Teacher.
    # Из Teacher сможем связаться с Student через 'students'
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class StudentPosition(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='positions')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='positions')
