from django.shortcuts import render
from django.views.generic import TemplateView
from mailer import send_mail

# Create your views here.

class Index(TemplateView):
    template_name = "notify/index1.html"

def get_alert(request):

    return render(request,"notify/email_template.html")

   