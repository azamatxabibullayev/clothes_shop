from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from .models import CategoryProducts, Review, Clothes, Order
from .forms import AddReviewForm, UpdateReviewForm
from django.urls import reverse
from django.contrib import messages


class CategoryProductsListView(View):
    def get(self, request):
        categories = CategoryProducts.objects.all()
        return render(request, 'category_products.html', {'categories': categories})


class ClothesListView1(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list1.html'
    context_object_name = 'clothes'


class ClothesListView(View):
    def get(self, request, category_id):
        category = get_object_or_404(CategoryProducts, pk=category_id)
        clothes = Clothes.objects.filter(category=category)
        return render(request, 'clothes/clothes_list.html', {'clothes': clothes})


class ClothesDetailView(View):
    def get(self, request, pk):
        clothe = get_object_or_404(Clothes, pk=pk)
        reviews = Review.objects.filter(clothe=clothe)
        return render(request, 'clothes/clothes_detail.html', {'clothe': clothe, 'reviews': reviews})


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        clothe = get_object_or_404(Clothes, pk=pk)
        add_review_form = AddReviewForm()
        return render(request, 'clothes/add_review.html', {'clothe': clothe, 'add_review_form': add_review_form})

    def post(self, request, pk):
        clothe = get_object_or_404(Clothes, pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = add_review_form.save(commit=False)
            review.clothe = clothe
            review.user = request.user
            review.save()
            messages.success(request, "Your comment added successfully!")
            return redirect('clothes:clothes_detail', pk=pk)
        else:
            messages.error(request, "Failed to add your comment.")
            return render(request, 'clothes/add_review.html', {'clothe': clothe, 'add_review_form': add_review_form})


class ReviewDeleteView(View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        clothe_pk = review.clothe.pk
        review.delete()
        messages.success(request, "Your comment deleted successfully!")
        return redirect('clothes:clothes_detail', pk=clothe_pk)


class ReviewUpdateView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        update_form = UpdateReviewForm(instance=review)
        return render(request, 'clothes/update_review.html', {'form': update_form})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        update_form = UpdateReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Your comment updated successfully!")
            return redirect('clothes:clothes_detail', pk=review.clothe.pk)
        else:
            messages.error(request, "Failed to update your comment.")
            return render(request, 'clothes/update_review.html', {'form': update_form})


class SearchResultsView(View):
    template_name = 'clothes/clothes_list.html'

    def get(self, request):
        query = request.GET.get('q')
        clothes = Clothes.objects.filter(name__icontains=query)
        return render(request, self.template_name, {'clothes': clothes})


class PlaceOrderView(View):
    def post(self, request, pk):
        clothe = get_object_or_404(Clothes, pk=pk)
        username = request.POST.get('username')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            user=username,
            number=phone
        )

        messages.success(request, "You ordered successfully!")
        return redirect('clothes:clothes_detail', pk=pk)
