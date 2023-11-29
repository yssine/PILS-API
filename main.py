from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hardware/<uuid>")
def hardware_uuid(uuid):
    pass



@app.route("/hardware/<usn>")
def hardware_uuid(usn):
    pass


