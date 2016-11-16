import sqlite3
con = sqlite3.connect('db1.db')
cur = con.cursor()
import json

def browse(p_id):
	query = "select * from persons where id={0}".format(p_id)
	cur.execute(query)
	p_data = cur.fetchall()
	p_data = json.dumps(p_data)
	return p_data
def main():
	pass
if __name__ == "__main__":
	main()