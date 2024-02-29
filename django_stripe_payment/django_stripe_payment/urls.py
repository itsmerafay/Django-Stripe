
from django.contrib import admin
from django.urls import path
from products.views import CreateCheckoutSessionView, ProductLandingPageView, CancelView, SuccessView,stripe_webhook, StripeIntentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-checkout-session/<int:pk>', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('', ProductLandingPageView.as_view(), name="landing-page"),        
    path('create-payment-intent/<int:pk>', StripeIntentView.as_view(), name="create-payment-intent"),    
    path('success/', SuccessView.as_view(), name="success"),    
    path('cancel/', CancelView.as_view(), name="cancel"),
    path('webhooks/stripe', stripe_webhook, name="stripe-webhook")     # no need of trailing slash

]
