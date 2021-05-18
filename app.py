from flask import Flask , render_template, request

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    a=request.form.get('exp')
    b=request.form.get('name')
    c=request.form.get('mail')
    d=request.form.get('phone_number')
    print(a,b,c,d)

    return render_template('thank.html')

app.run(debug=True)