from django.shortcuts import render
from django.views import View
from bookstore.forms import BookForm

# Create your views here.
class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=BookForm()
        return render(request,"book_add.html",{"form":form_instance})

