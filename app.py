from flask import Flask, render_template, request
import utils

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        open_ = request.form.get('open_')
        high = request.form.get('high')
        low = request.form.get('low')
        volume = request.form.get('volume') 

    prediction = utils.preprocessdata(open_, high, low , volume) 

    return render_template('predict.html', prediction=prediction) 
if __name__ == '__main__': 
    app.run(debug=True) 