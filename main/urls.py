from django.urls import path
from .views import TodoListView, TodoDetailView, GoalCreateView, GoalUpdateView, GoalDeleteView

app_name="todo"
urlpatterns = [
    path('', TodoListView.as_view(), name="home"),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name="goal-detail"),
    path('create/', GoalCreateView.as_view(), name="goal-create"),
    path('update/<int:pk>/', GoalUpdateView.as_view(), name="goal-update"),
    path('delete/<int:pk>/', GoalDeleteView.as_view(), name="goal-delete"),
]
