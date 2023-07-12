from sqlalchemy import create_engine, text
import os

connection_string = os.environ["Database_connection"]
engine = create_engine(connection_string,
                       connect_args={'ssl': {
                         'ssl.ca': "/etc/ssl/cert.pem"
                       }})


def load_from_Db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.fetchall():
      jobs.append(dict(zip(result.keys(), row)))
  return jobs


def load_particular_job(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :id"),
                          {"id": id})

    row = result.fetchall()
    if not row:
      return None
    else:
      return dict(zip(result.keys(), row[0]))

def load_application(data):
  with engine.connect() as conn:
    conn.execute(
      text(
        "insert into user(name,email,linkedin) values (:name,:email,:linkedin)"
      ), {
        'name': data['name'],
        'email': data['email'],
        'linkedin': data['linkedin']
      })
