# app.py
from flask import Flask, request, jsonify,render_template
import json
app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/ip_log/',methods=['GET'])
def get_ip():
    return send_file('ip_log.json', as_attachment=True)


@app.route('/request/', methods=['POST'])
def post_something():
    param = request.form.get('link')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f" {param} this is a post request",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

#A welcome message to test our server
@app.route('/')
def index():
    #ip logging into ip_log.json
    with open("ip_log.json", "w") as outfile:

        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            outfile.write('\n'+str({'ip': request.environ['REMOTE_ADDR']}))
        
        else:
            outfile.write('\n'+str({'ip': request.environ['HTTP_X_FORWARDED_FOR']}))
    
    return render_template('index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)