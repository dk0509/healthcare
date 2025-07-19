from django.urls import path
from .views import MappingListCreateView, MappingDetailView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
     path('<int:id>/', MappingDetailView.as_view(), name='mapping-detail'),
]
