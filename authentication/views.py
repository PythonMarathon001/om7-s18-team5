from django.shortcuts import render, redirect
from order.models import Order
from authentication.models import CustomUser
from django.db.models.functions import Now
from django.db.models import Q
from django.views.generic import ListView
from .forms import CustomUserForm
from .models import CustomUser
from rest_framework import generics, permissions
from .serializers import *
from order.serializers import *


class UserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer


class UserOrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        id_from_url = self.request.path
        user = id_from_url.split('/')[4]
        queryset = Order.objects.filter(user=int(user))
        return queryset


class UserOrderDetailView(generics.ListAPIView):
    def get_queryset(self):
        id_from_url = self.request.path
        user = id_from_url.split('/')[4]
        id = id_from_url.split('/')[6]
        queryset = Order.objects.filter(pk=int(id),user = int(user))
        print(queryset)
        return queryset
    serializer_class = OrderDetailSerializer

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
