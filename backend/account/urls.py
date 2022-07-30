from django.conf.urls import url
from django.urls import path
from backend.account.restful import auth, signup
from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()

urlpatterns = urlpatterns.format_suffix_patterns([
    # Auth
    url(r'^login/$', auth.Login.as_view(), name='login'),
    url(r'^validate/$', auth.Validate.as_view(), name='validate'),
    url(r'^signout/$', auth.SignOut.as_view(), name='sign_out'),
    path(r'signup/', signup.Signup.as_view(), name='signup'),
    path(r'update_user/<str:user_id>/', signup.Signup.as_view(), name='update_user'),
])
