from django.urls import path

from agency.views import categories
from agency.views import news

urlpatterns = [
    path('', categories),
    path('news/<int:category_id>', news),
]