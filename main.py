import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method == 'GET':
        secrite_number = request.cookies.get('secrite_number')

        response = make_response(render_template('index.html'))
        if not secrite_number:
            new_number = random.randint(1,5)
            response.set_cookie('secrite_number', str(new_number))
        
        return response

    if request.method == 'POST':
        spejimas = int(request.form.get('spejimas'))
        secrite_number = int(request.cookies.get('secrite_number'))

        if spejimas == secrite_number:
            message = 'Sveikinu, slaptas skaicius yra: {0}'.format(int(secrite_number))
            response = make_response(render_template('rezultatai.html', message = message))
            response.set_cookie('secrite_number', str(random.randint(1,5)))
            return response

        elif spejimas > secrite_number:
            message = 'Maziau'

            return render_template('rezultatai.html', message = message)

        elif spejimas < secrite_number:
            message = 'Daugiau'

            return render_template('rezultatai.html', message = message)


if __name__ == '__main__':
    app.run(debug=True)


