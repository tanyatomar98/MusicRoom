from django.urls import path
from .views import (
    home_page_view,
    sign_in_view
                   )
app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name="pages"),
    path('signin/', sign_in_view, name="sign-in")
]