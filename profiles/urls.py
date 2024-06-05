from django.urls import path
from profiles import views


# ProfileList is a class list so therefore we need to call it with as_view
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]