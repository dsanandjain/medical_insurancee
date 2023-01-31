
from flask import Flask, jsonify, render_template, request
import calculation

app = Flask(__name__)

@app.route('/')
def hello_flask():
    # print("Welcome to Flask")
    # return "Hello Python"
    return render_template("index.html")


#################################################################################
################################### Home API ####################################
#################################################################################

@app.route('/test')
def test():
    print("This is Testing API")
    return jsonify({"Message" : "Tested Successfully"})

#################################################################################
################################### Addition API ################################
#################################################################################

@app.route('/addition')
def add():
    x = 100
    y = 200
    result = calculation.get_Addition(x,y)
    return jsonify({"Result" : f"Addition of {x} and {y} is {result}"})

#################################################################################
################################### addition2 API ###############################
#################################################################################

@app.route('/addition2')
def addition2():
    input_data = request.form
    print("Input Data -->\n",input_data)
    x = eval(input_data['a'])
    y = eval(input_data['b'])
    result = calculation.get_Addition(x,y)
    return jsonify({"Result" : f"Addition of {x} and {y} is {result}"})

#################################################################################
################################### Multiplication API ##########################
#################################################################################

@app.route('/multiplication')
def mult():
    input_data = request.json
    print("Input Data -->\n",input_data)
    x = input_data['a']
    y = input_data['b']
    result = calculation.get_Multiplication(x,y)
    return jsonify({"Result" : f"Multiplication of {x} and {y} is --> {result}"})


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= 5000, debug=True)