#DB: Sqlite3
import sqlite3

conn = sqlite3.connect('jobdb.db')

c = conn.cursor()

query = "Select * from job_postings"
results = c.execute(query)
conn.commit()

for row in results:
    print(results[0]['company'])

conn.close()

