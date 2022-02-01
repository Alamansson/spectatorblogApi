from django.urls import path

from spectatorblog.account.views import RegisterView, ActivationView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),

    ]
