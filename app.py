from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__, template_folder="static/templates")

with open("data/database.json", encoding="utf-8", mode="r") as f:
    data = json.load(f)
 
@app.route("/")
def render_index():
    return render_template("index.html")

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    constituency = request.args.get('constituency')
    if constituency:
        relevant_data = [profile for profile in data if profile['constituency'].lower() == constituency.lower()]
        return jsonify(relevant_data)
    return jsonify(data)


@app.route('/api/constituencies')
def get_wahlkreise():
    return jsonify(sorted(list(set([person["constituency"] for person in data]))))


@app.route('/constituency/<constituency>')
def constituency_page(constituency):
    return render_template("profile.html")


@app.route('/landtag')
def render_langtag():
    return render_template('landtag.html')

@app.route('/to-be-implemented')
def render_tbi():
    return render_template('to-be-implemented.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=True)
