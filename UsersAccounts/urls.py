from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from UsersAccounts import views
from UsersAccounts.views import LoginView, UserView, LogoutView

urlpatterns = [
    path('register/', views.RegisterView().as_view(), name='register'),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('hello/', views.HelloView.as_view(), name='hello'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











# from django.urls import path
# from .views import RegisterView, LoginView
#
# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('login/', LoginView.as_view()),
#     path('user/', UserView.as_view()),
#     path('logout/', LogoutView.as_view()),
# ]