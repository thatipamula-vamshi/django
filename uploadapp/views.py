from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFile

# Create your views here.
def uploadimages(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            context= {'saved_object':saved_object, }
            return render (request,'uploadapp/add_image.html',context)
    else:
        form = UploadForm()
    context = {'form': form, }
    return render (request,'uploadapp/add_image.html',context)

def uploadfile(request):
    if request.method == 'POST':
        form = UploadFile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            context= {'saved_object':saved_object, }
            return render (request,'uploadapp/add_file.html',context)
    else:
        form = UploadFile()
    context = {'form': form, }
    return render (request,'uploadapp/add_file.html',context)

