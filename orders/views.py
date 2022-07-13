import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


@login_required(login_url='/accounts/login/')
def charge(request):
    permission = Permission.objects.get(codename='special_status')
    user = request.user
    user.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')
