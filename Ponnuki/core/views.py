from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from . import models
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login


# Create your views here.
import os
def index(request):
    return render(request, 'core/index.html')
def main(request):
    return render(request, 'core/main.html')
def shop(request):
    return render(request,'core/shop.html')
def contact(request):
    return render(request,'core/contact.html')
def testimonial(request):
    return render(request,'core/testimonial.html')
def index(request):
    return render(request,'core/index.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('main')  
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('login')
        
        else:
            return render(request, 'registration/sign_up.html', {'form': form})
        
    else:
        form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})


'''def login(request):
    customer_data=models.Customer.objects.all()
    customer_context={'customers':customer_data}
    return render(request,'core/login.html',context=customer_context)'''

'''def my_view(request):
    images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
    images_list = [f for f in os.listdir(images_dir) if f.endswith('.png') or f.endswith('.jpg')]
    context = {'images': images_list}
    return render(request, 'core/main.html', context)  
class GenericPageView(TemplateView):
    template_name = "" '''

#def get_template_names(self):
#        return [self.template_name]

                      
