from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import ObtainJSONWebToken
from django.urls import path

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('', ObtainJSONWebToken.as_view()),
] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
