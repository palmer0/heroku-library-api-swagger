from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from api_books import views


# Define the URLs
router = DefaultRouter(trailing_slash=False)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
