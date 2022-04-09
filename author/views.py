from django import views
from django.shortcuts import render, redirect
from django.views.generic import ListView
from order.models import Author
from .forms import AuthorForm
from .models import Author
from rest_framework import viewsets
from .serializers import AuthorSerializer


class AuthorViewAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

# class AuthorList(ListView):
#
#     model = Author
#     template_name = "author/index.html"
#     context_object_name = "authors"
#
#
#
#     def get_context_data(self, **kwargs):
#
#         context = super(AuthorList, self).get_context_data(**kwargs)
#         context['title'] = 'Список авторів'
#         context['content_title'] = 'Адміністрування бібліотеки / Автори книг'
#
#         return context
#
#     def get_queryset(self):
#
#         queryset = Author.get_all()
#
#         return queryset



# ##### new


def author_list(request):
    context = {'author_list':Author.objects.all()}
    return render(request,'author/author_list.html', context)

def author_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
        return render(request, 'author/author_create.html', {'form':form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form=AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
        return redirect('author_list')


def author_delete(request,id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('author_list')