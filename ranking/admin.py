from django.contrib import admin

from  .models import  Theme, Category, Question, Answer

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id','name','weight','calculated_value')
    search_fields = ('id','name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent_theme','weight','calculated_value')
    search_fields = ('id','name')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question','parent_category','weight','map_to_field_1','scoring_method')
    search_fields = ('id','question')
    list_filter = ('parent_category',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','answer_choice','parent_question','weight','answer_types')
    search_fields = ('id','answer_choice')
    list_filter = ('parent_question','parent_question__parent_category')

admin.site.register(Theme, ThemeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)