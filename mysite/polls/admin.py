from django.contrib import admin
from .models import Question
from .models import Choice, Question

class ChoiceInline(admin.TabularInline): #untuk tampilan lebih ringkas
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline] 
    list_display = ["question_text", "pub_date", "was_published_recently"] #tampilan kolom di daftar admin
    list_filter = ["pub_date"] #untuk fiilter tanggal publikasi
admin.site.register(Question, QuestionAdmin)