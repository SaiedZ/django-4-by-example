from decimal import Decimal

from django.conf import settings
from shop.models import Product
from coupons.models import Coupon


class Cart:

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})

        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        # Initialize the cart item if it doesn't exist, otherwise update it
        cart_item = self.cart.setdefault(
            product_id, {'quantity': 0, 'price': str(product.price)}
        )

        if update_quantity:
            cart_item['quantity'] = quantity
        else:
            cart_item['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        # TODO: check if this is necessary because seems
        # already done in __setitem__
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity'] for item in self.cart.values()
        )

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        if not self.coupon_id:
            return None
        try:
            return Coupon.objects.get(id=self.coupon_id)
        except Coupon.DoesNotExist:
            return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()