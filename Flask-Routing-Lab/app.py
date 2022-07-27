from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/product')
def index2():
    return render_template('product.html')
@app.route('/cart.html')
def index3():
    return render_template('cart.html')
 
if __name__ == '__main__':
    app.run(debug = True)