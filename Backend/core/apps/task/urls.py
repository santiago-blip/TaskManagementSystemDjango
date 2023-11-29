from django.urls import path,include
from .views.TaskView import TaskView
from .views.StatusView import StatusView
from .views.TaskConnections import TaskStatusView, TaskCategoryView
from .views.CategoryView import CategoryView

urlpatterns = [
    path('',TaskView.as_view()),
    path('<int:pk>',TaskView.as_view(),name='task-detail'),
    path('status/',StatusView.as_view()),
    path('status/<int:pk>',StatusView.as_view(),name='status-detail'),
    path('manage-status/',TaskStatusView.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>',CategoryView.as_view(),name='status-detail'),
    path('manage-category/',TaskCategoryView.as_view()),
]