from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost



Job_title = [
    "first job",
    "second job",
    "third job"
]

Job_description = [
    "first job description",
    "second job description",
    "Third job description"
]

class temp():
    x =5

# Create your views here.
#def hello(request):
    #return HttpResponse ('<h3>Hello World</h3>')

def hello(request):
    #template = loader.get_template('app/hello.html')
    list = ['Crazy','Stupid']
    is_authenticated = True
    temp_objecct = temp()
    context ={'name':'Django','age':25 ,'First_list': list, 'temp_o': temp_objecct, 'is_authenticated': is_authenticated }
    #return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)

def job_list(request):
    # list_jobs = '<ul>'
    # for j in Job_title:
    #     job_id = Job_title.index(j)
    #     backfun = reverse('details', args= (job_id,))
    #     list_jobs += f"<li><a href ='{backfun}'>{j}</a></li>"
    # list_jobs += '</ul>'   
    # return HttpResponse (list_jobs) 
    jobs = JobPost.objects.filter()
    context={'jobs':jobs}
    return render(request, 'app/index.html',context)



def job_details(request,id):
    print(type(id))
    try:
        if id == 0:
            return redirect (reverse('home'))
        # return_html = f"<h1>{Job_title[(id)]}</h1> <h3>{Job_description[(id)]}</h3>"
        # return HttpResponse (return_html)
        # context = {'Job_title':Job_title[id], 'Job_description':Job_description[id]}
        jobe = JobPost.objects.get(id=id)
        context ={'job':jobe}
        return render (request,'app/job_details.html', context)
    except:
        return HttpResponseNotFound('Not Found')
