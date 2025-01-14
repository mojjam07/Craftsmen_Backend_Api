
from django.urls import path
from .views import UserView, CraftsmanView, ApprenticeView, CategoryView, OrderView, JobView

urlpatterns = [
    
    path('users/', UserView.as_view(), name='user-list'),  
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'), 
    path('craftsmen/', CraftsmanView.as_view(), name='craftsman-list'),  
    path('craftsmen/<int:pk>/', CraftsmanView.as_view(), name='craftsman-detail'),  
    path('apprentices/', ApprenticeView.as_view(), name='apprentice-list'),  
    path('apprentices/<int:pk>/', ApprenticeView.as_view(), name='apprentice-detail'),  
    path('categories/', CategoryView.as_view(), name='category-list'),  
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),
    path('orders/', OrderView.as_view(), name='order-list'),  
    path('orders/<int:pk>/', OrderView.as_view(), name='order-detail'),  
    path('jobs/', JobView.as_view(), name='job-list'),  
    path('jobs/<int:pk>/', JobView.as_view(), name='job-detail'),  
]