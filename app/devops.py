from flask import Flask
from flask import request
from flask import jsonify
from datetime import date

app = Flask(__name__)

@app.route("/get_details", methods=["GET"])
def get_my_ip():
    return jsonify(
        {'visitor ip': request.remote_addr},
        #{'engine': request.flask._version_}
        #{'host ip': request.environ['SERVER_ADDR']},
        {'date': date.today()}
    ), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)