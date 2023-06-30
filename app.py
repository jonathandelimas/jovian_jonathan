from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title':'Data Analyst',
    'location': 'Sydney, Australia',
    'salary': '$100,000'
  },
    {
    'id': 2,
    'title':'Data Engineer',
    'location': 'Melbourne, Australia',
    'salary': '$150,000'
  },
    {
    'id': 3,
    'title':'Power BI Analyst',
    'location': 'Ingleburn, Australia',
   
  },
    {
    'id': 4,
    'title':'Data Scientist',
    'location': 'Sydney, Australia',
    'salary': '$150,000'
  },
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                          jobs=JOBS,
                          company_name='JohnCorp')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  