from decimal import Decimal
# from django.conf
from shop.models import Product

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})
        self.cart = cart

        # cart = self.session.get(settings.CART_SESSION_ID)
        # if not cart:
        #     cart = self.session[settings.CART_SESSION_ID] = {}
        # self.cart = cart

    def __iter__(self):
        products_ids = self.cart['cart'].keys()

        products = Product.objects.filter(id__in=products_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product # создает ключ объекта и сохраняет сам объект как значение

        for item in self.cart.values: #{'quantity': 0, 'price': str(product.price), 'product': product_obj}
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity'] # создаю еще один ключ который хранит колво*цену
            yield item

    def add_product(self, product, quantity=1, update_quantity=False):    # cart = {'1': {quantity: } }
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self_cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

