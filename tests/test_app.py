import tempfile, unittest
from pathlib import Path
import app
class Tests(unittest.TestCase):
 def test_add_and_list(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'test.sqlite3'; app.add(["Ada","Consultation","2026-11-01 10:00","booked"],p); self.assertEqual(len(app.listing(p)),1)
if __name__=='__main__': unittest.main()
