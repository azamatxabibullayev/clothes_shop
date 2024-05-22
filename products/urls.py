from django.urls import path
from .views import ReviewDeleteView, ReviewUpdateView, ClothesListView, ClothesDetailView, AddReviewView, \
    CategoryProductsListView, SearchResultsView, ClothesListView1, PlaceOrderView

app_name = 'clothes'
urlpatterns = [
    path('clothes/', ClothesListView1.as_view(), name='clothes_list1'),
    path('products/detail/<int:pk>/', ClothesDetailView.as_view(), name='clothe_detail'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('categories/', CategoryProductsListView.as_view(), name='category_products'),
    path('categories/<int:pk>/', ClothesListView.as_view(), name='clothes_by_category'),
    path('products/clothes/<int:category_id>/', ClothesListView.as_view(), name='clothes_list'),
    path('place_order/<int:pk>/', PlaceOrderView.as_view(), name='place_order'),
]
