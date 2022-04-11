from django.shortcuts import render, redirect
from order.models import Order
from authentication.models import CustomUser
from django.db.models.functions import Now
from django.db.models import Q
from django.views.generic import ListView
from .forms import CustomUserForm
from .models import CustomUser
from rest_framework import generics
from .serializers import *
from order.serializers import *


class UserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer


class UserOrderListView(generics.ListCreateAPIView):
    serializer_class = UserOrderSerializer
    def perform_create(self, serializer):
        serializer.save(user=CustomUser.objects.get(pk=self.kwargs['user_id']))
    def get_queryset(self):
        filter = {}
        data = self.kwargs
        if data['user_id']:
            filter['user__id'] = data['user_id']
            
        queryset = Order.objects.filter(**filter)
        return queryset


class UserOrderDetailView(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserOrderSerializer
    def perform_update(self, serializer):
        serializer.save(user=CustomUser.objects.get(pk=self.kwargs['user_id']))
    def get_queryset(self):       
        filter = {}
        data = self.kwargs
        if data['pk']:
            filter['pk'] = data['pk']        
        if data['user_id']:
            filter['user__id'] = data['user_id']
            
        queryset = Order.objects.filter(**filter)
 
        return queryset
    
    

    # class UserList(ListView):
    #
    #     model = CustomUser
    #     template_name = "authentication/index.html"
    #     context_object_name = "users"
    #
    #     def get(self, request, *args, **kwargs):
    #
    #         return ListView.get(self, request, *args, **kwargs)
    #
    #
    #     def get_context_data(self, **kwargs):
    #
    #         context = super(UserList, self).get_context_data(**kwargs)
    #         context['title'] = 'Список читачів'
    #         context['content_title'] = 'Адміністрування бібліотеки / Читачі'
    #
    #         return context
    #
    #     def get_queryset(self):
    #
    #         queryset = CustomUser.get_all()
    #
    #         return queryset
    #


def overdue(request):

    users = CustomUser.objects.filter(
        Q(order__plated_end_at__lte=Now()) & Q(order__end_at__isnull=True))

    context = {}
    context['title'] = 'Список читачів'
    context['content_title'] = 'Адміністрування бібліотеки / Читачі'
    context['users'] = users

    return render(request, 'authentication/index.html', context)


# new


def user_list(request):
    context = {'user_list': CustomUser.objects.all()}
    return render(request, 'authentication/user_list.html', context)


def user_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomUserForm()
        else:
            user = CustomUser.objects.get(pk=id)
            form = CustomUserForm(instance=user)
        return render(request, 'authentication/user_create.html', {'form': form})
    else:
        if id == 0:
            form = CustomUserForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=id)
            form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('order_list')


def user_delete(request, id):
    user = CustomUser.objects.get(pk=id)
    user.delete()
    return redirect('order_list')
