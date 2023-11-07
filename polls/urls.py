from django.urls import path
from . import views
urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('<int:pk>/atualizar', views.QuestionUpdateView.as_view(), name="question-update"),
    path('pergunta/<int:pk>/alternativa/add', views.ChoiceCreateView.as_view(), name="choice_add"),
    path('alternativa/<int:pk>/edit', views.ChoiceUpdateView.as_view(), name="choice_edit" ),
    path('alternativa/<int:pk>/delete', views.ChoiceDeleteView.as_view(), name="choice_delete" ),
    path('pergunta/<int:question_id>/vote', views.vote, name="poll_vote"),
] 