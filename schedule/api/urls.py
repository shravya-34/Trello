from django.urls import path
from . import views

urlpatterns = [
    path("authenticate/", views.Authenticate.as_view(), name="authenticate"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("scheduleuser", views.Schedule.as_view(), name="scheduleuser"),
    path("schedule/", views.ScheduleAll.as_view(), name="schedule"),
    path("column/", views.Columns.as_view(), name="column"),
    path("schedule/<int:pk>", views.EditCard.as_view(), name="edit")
]
