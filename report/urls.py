from django.urls import path

from report import views


urlpatterns = [
    path("user-report/", views.UserReportView.as_view(), name="user-report"),
]
