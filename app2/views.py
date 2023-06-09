from django.shortcuts import render

# Create your views here.
def PasswordResetView(request):
    return render (request,'app2/password_reset.html')