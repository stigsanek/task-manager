from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.ListStatusView.as_view(), name='list'),
    path('create/', views.CreateStatusView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateStatusView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete'),
]
