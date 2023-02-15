from django.urls import path
from . import views

app_name = 'stripeapp'

urlpatterns = [
    path('buy/<pk>', views.CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<pk>', views.ItemDisplayView.as_view(), name='item'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('webhooks/stripe/', views.stripe_webhook, name='stripe_webhook'),
]
