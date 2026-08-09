from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewset

router = DefaultRouter()
router.register(r'books',BookViewset,basename='book')

urlpatterns = [
    path('' ,include(router.urls)),

]