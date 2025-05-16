from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def job_category(request):
    return render(request, 'job_category.html')


def job_detail(request):
    return render(request, 'job_detail.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')


def post_job(request):
    return render(request, 'post_job.html')


