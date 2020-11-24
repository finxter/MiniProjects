from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='./myapp/templates')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sum', methods=['GET'])
def sum():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except:
        return render_template('invalid_input.html')

    result = a + b
    #return jsonify(result)
    return render_template('result.html', data=result)


@app.route('/mult', methods=['GET'])
def mult():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except:
        return render_template('invalid_input.html')

    result = a * b
    #return jsonify(result)
    return render_template('result.html', data=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')