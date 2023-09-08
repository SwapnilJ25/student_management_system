from django.shortcuts import redirect, render, HttpResponse

def HOME(request):
    return render(request,'Staff/staff_home.html')