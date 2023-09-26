from django.urls import path
from . import views
urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('<int:pk>/atualizar', views.QuestionUpdateView.as_view(), name="question-update")
] 