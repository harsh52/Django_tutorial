from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory store for purchases, discounts, and carts
purchases = []
discounts = {}
carts = {}

ADMIN_TOKEN = 'your_admin_token_here'

def generate_discount_code(total_amount):
    if total_amount > 5:
        return 'DISCOUNT5'
    return None


@app.route('/api/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = int(data['user_id'])
    item = data['item']

    if user_id not in carts:
        carts[user_id] = []

    carts[user_id].append(item)
    return jsonify({'message': 'Item added to cart successfully'})


@app.route('/api/view-cart', methods=['GET'])
def view_cart():
    user_id = int(request.args.get('user_id'))
    if user_id not in carts or not carts[user_id]:
        return jsonify({'message': 'Cart is empty'})

    return jsonify({'cart_items': carts[user_id]})


@app.route('/api/checkout', methods=['POST'])
def checkout():
    data = request.json
    user_id = int(data['user_id'])

    if user_id not in carts or not carts[user_id]:
        return jsonify({'message': 'Cart is empty'})

    cart_items = carts[user_id]
    total_amount = len(cart_items) * 10

    # Apply discount if applicable
    discount_code = generate_discount_code(total_amount)
    if discount_code:
        discounts[discount_code] = total_amount * 0.1  # 10% discount

    purchases.append({
        'user_id': user_id,
        'items': cart_items,
        'total_amount': total_amount
    })

    # Clear the cart after checkout
    del carts[user_id]

    return jsonify({
        'message': 'Checkout successful',
        'total_amount': total_amount,
        'discount_code': discount_code
    })


@app.route('/api/purchase-statistics', methods=['GET'])
def purchase_statistics():
    if request.headers.get('Authorization') != f'Bearer {ADMIN_TOKEN}':
        abort(401)  # Unauthorized

    items_count = sum(len(p['items']) for p in purchases)
    total_amount = sum(p['total_amount'] for p in purchases)
    discount_stats = [{'code': code, 'amount': amount} for code, amount in discounts.items()]

    return jsonify({
        'items_count': items_count,
        'total_amount': total_amount,
        'discount_stats': discount_stats
    })


if __name__ == '__main__':
    app.run(debug=True)
