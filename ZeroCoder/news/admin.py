from django.contrib import admin

# Register your models here.
#Прописываем импорт класса.
from .models import News_post
#Прописываем команду регистрации новой таблицы внутри проекта.
admin.site.register(News_post)
