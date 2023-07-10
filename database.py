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
