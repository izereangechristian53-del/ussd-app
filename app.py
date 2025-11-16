from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    text = request.values.get("text", "")

    if text == "":
        response = "CON Welcome to Mineral Test Lab\n1. Request Test\n2. Get Results\n3. Training\n4. Contact Us"
    else:
        response = "END Thank you for using our service."

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run()
