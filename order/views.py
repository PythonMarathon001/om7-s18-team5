from django.shortcuts import render, redirect
from order.forms import OrderForm
from django.views.generic import ListView
from .forms import OrderForm
from order.models import Order
from rest_framework import generics, permissions
from .serializers import *


class OrderView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderList(ListView):

    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"

    def get(self, request, *args, **kwargs):

        self.order_by = []
        data = request.GET

        self.end_at = data['end_at'] if 'end_at' in data else 'asc'
        self.order_by.append('end_at' if self.end_at == 'asc' else '-end_at')

        self.plated_end_at = data['plated_end_at'] if 'plated_end_at' in data else 'asc'
        self.order_by.append(
            'plated_end_at' if self.plated_end_at == 'asc' else '-plated_end_at')

        return ListView.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(OrderList, self).get_context_data(**kwargs)
        context['title'] = 'Список замовлень'
        context['content_title'] = 'Адміністрування бібліотеки / Замовлення'
        context['orders_by'] = {'end_at': self.end_at,
                                'plated_end_at': self.plated_end_at}

        return context

    def get_queryset(self):

        queryset = Order.get_all(self.order_by)

        return queryset


def index(request):

    return render(request, 'order/index.html', {'title': 'Order...'})


def order_by_id(request, order_id):

    book_by_id = Order.get_by_id(order_id)
    if book_by_id:
        return render(request, 'order/element.html', {'title': f'Замовлення №{order_id}', 'content_title': f'Деталі замовлення №{order_id}', 'content': book_by_id})
    else:
        return redirect('order')
    #


# ##### new


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def order_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(instance=order)
        return render(request, 'order/order_create.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('list')


def order_delete(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('/order/list')
