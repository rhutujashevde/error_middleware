from django.conf.urls import url
from .views import ErrorStackAPI

urlpatterns = [
    url('error_stack/', ErrorStackAPI.as_view(), name='error_stack'),
]