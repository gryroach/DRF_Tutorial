from snippets.views import SnippetViewSet, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += [
    path('', include(router.urls))
]



