from item.models import Item

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_cart')
        if 'session_cart' not in request.session:
            cart = self.session['session_cart'] = {}

        self.cart = cart


    def add(self, item, quantity):
        product_id = str(item.id)
        product_qty = str(quantity)


        if product_id in self.cart:
            pass
            # self.cart[product_id] = 1 
        else:
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True

    def get_item(self):
        product_ids = self.cart.keys()
        products = Item.objects.filter(id__in=product_ids)

        return products
    
    def get_qty(self):

        return self.cart

    def remove(self, item_id):
        product_id = str(item_id)
        # delete from cart dictionary
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True

    
    def update(self, item, quantity):
        product_id = str(item.id)
        product_qty = int(quantity)

        cart = self.cart
        cart[product_id] = product_qty
        self.session.modified = True

        res = self.cart
        return res
    
    def __len__(self):
        cart = self.cart
        # res = 0
        # for x,y in cart.items():
        #     res += y

        return len(cart)