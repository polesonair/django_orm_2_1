from django.contrib import admin

from .models import Student, Teacher, StudentPosition

class StudentPositioninline(admin.TabularInline):
    model = StudentPosition
    # выстраиваем модель для StudentPosition
    extra = 0
    #Количество позиций товаров в таблице отображения в заказе


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentPositioninline, ]
    # Добавлять преподавателям студентов


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentPositioninline,]
    # Добавлять студентам преподавателей.


