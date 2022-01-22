from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
import stripe


# Create your views here.
@login_required
def basket_view(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    # Add Stripe Secret Key
    stripe.api_key = ''
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {
        'client_secret': intent.client_secret
    })
