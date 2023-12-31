from django.shortcuts import render, redirect
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm
    
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print('valid form')  
            # print(subscribe_form.cleaned_data)
            # email = subscribe_form.cleaned_data['email']
            # first_name = subscribe_form.cleaned_data['first_name']  
            # last_name = subscribe_form.cleaned_data['last_name']  
            # print(email)
            # subscribe = Subscribe(first_name=first_name,last_name=last_name,email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))
    context={'Form':subscribe_form,}
    return render(request,'subscribe/subscribe.html', context)
    

def thank_you(request):
    context= {}
    return render(request,'subscribe/thank_you.html',context)