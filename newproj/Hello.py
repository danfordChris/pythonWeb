from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello creator!' 


@app.route('/success/<name>')
def success(name):
    return render_template('login.html', name = name)

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest = name))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('uname')
        return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.debug = True
    app.run()