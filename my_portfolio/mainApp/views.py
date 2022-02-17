from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import MyProject
from django.core.mail import send_mail
# Create your views here.


class HomePage(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects']=MyProject.objects.all()
        return context


def processing_contact(request):
    if request.method == "POST":
        email=request.POST.get('client_email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        send_mail(
            subject,
            message,
            email,
            ['aengrhenry@gmail.com']
        )
        context={
             "msg":'thanks email sent successfully! Henry will respond shortly'
         }
        return render(request, "index.html", context)



class ProjectDetail(DetailView):
    model=MyProject
    template_name='details.html'
   