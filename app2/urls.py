from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #here i had to close 1 path to account because it takes to another paths and i have changed the login fun name
    # from login to login1 v.v.i
    #path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='app2/password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='app2/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app2/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app2/password_reset_done.html'),
         name='password_reset_complete'),
    #path('reset_password/', auth_views.PasswordResetView.as_view()),
]







#these are the urls connected with above accounts urls
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']


#this is example
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('change-password/', auth_views.PasswordChangeView.as_view()),
# ]




