from django.contrib import admin
from .models import Pictures,YearOfExam,Announcements,DistinctionHolder
# Register your models here.

admin.site.register(Pictures)
admin.site.register(YearOfExam)
admin.site.register(Announcements)
admin.site.register(DistinctionHolder)
