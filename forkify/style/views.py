from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.views.generic.edit import CreateView
# Create your views here.

class Styling(CreateView):
    template_name = "style/index.html"
    # model = Book
    # fields ="__all__"
    form_class = BookForm    
    success_url =reverse_lazy("radio")
