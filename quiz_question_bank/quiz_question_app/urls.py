from django.urls import path
from .views import (
    create_question,
    get_questions,
    get_question,
    delete_question,
    delete_all_questions,
    update_question
)

urlpatterns = [
    path('create-question/', create_question, name='create_question'),
    path('get-questions/', get_questions, name='get_questions'),
    path('get-question/<str:question_id>/', get_question, name='get_question'),
    path('delete-question/<str:question_id>/', delete_question, name='delete_question'),
    path('delete-all-questions/', delete_all_questions, name='delete_all_questions'),
    path('update-question/<str:question_id>/', update_question, name='update_question'),
]