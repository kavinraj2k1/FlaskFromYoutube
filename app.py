from flask import Flask, render_template, jsonify
from database import load_from_Db, load_particular_job

app = Flask(__name__)


@app.route('/jobs/<id>')
def list_of_jobs(id):
  jobs = load_particular_job(id)
  return render_template('jobdescription.html', job=jobs)


@app.route("/")
def hello_jovian():
  jobs = load_from_Db()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_from_Db())


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
