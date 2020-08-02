from django.shortcuts import render
from .models import Job, Category
from django.core.paginator import Paginator

# Create your views here.   

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)
    
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    context = {'job' : job_detail}
    return render(request, 'job/job_detail.html', context)

def category_list(request):
    category_list = Category.objects.all()
    context = {'category' : category_list}
    return render(request, 'job/category_list.html', context)