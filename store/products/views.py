from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from .models import Basket, Products


class HomeView(TemplateView):
    template_name = 'products/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        return context


class ProductsView(ListView):
    model = Products
    template_name = 'products/products.html'
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'products'
    paginate_by = 6


class CategoriesView(ListView):
    model = Products
    template_name = 'products/categoriesview.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['slug'])


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    redirect_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(redirect_url)


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id, user=request.user)
    basket.delete()
    profile_url = reverse('profile', kwargs={'pk': request.user.pk})
    return redirect(profile_url)
