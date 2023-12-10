from flask import Flask, render_template, jsonify



app = Flask(__name__)

workshops = [{
    'id': 1,
    'name': 'Urban Dance',
    'date': '12th-dec',
    'timing': '4-6pm',
}, {
    'id': 2,
    'name': 'Bollywood',
    'date': '17th-dec',
    'timing': '5-6pm',
}, {
    'id': 3,
    'name': 'Upcoming Clg Fests!',
    'date': '1-Jan',
    'timing': '4-6pm',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', shops=workshops)


@app.route("/ws")
def list_job():
  return jsonify(workshops)


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
