import argparse, json, sqlite3
from pathlib import Path
DB=Path(__file__).with_name('data.sqlite3')
TABLE='appointments'
def connect(path=DB):
 c=sqlite3.connect(str(path)); c.row_factory=sqlite3.Row; c.execute("CREATE TABLE IF NOT EXISTS appointments(id INTEGER PRIMARY KEY, customer TEXT NOT NULL, service TEXT NOT NULL, starts_at TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'booked')"); return c
def add(values,path=DB):
 with connect(path) as c:
  cur=c.execute("INSERT INTO appointments(customer,service,starts_at,status) VALUES(?,?,?,?)",values); return cur.lastrowid
def listing(path=DB):
 with connect(path) as c:return [dict(r) for r in c.execute('SELECT * FROM appointments ORDER BY id DESC')]
def main():
 p=argparse.ArgumentParser(description='Book and track customer appointments.'); s=p.add_subparsers(dest='cmd',required=True); a=s.add_parser('add');
 a.add_argument('--customer',required=True); a.add_argument('--service',required=True); a.add_argument('--starts-at',required=True); a.add_argument('--status',required=True)
 s.add_parser('list'); x=p.parse_args()
 if x.cmd=='add': print(json.dumps({'id':add([x.customer, x.service, x.starts_at, x.status])}))
 else: print(json.dumps(listing(),indent=2))
if __name__=='__main__': main()
