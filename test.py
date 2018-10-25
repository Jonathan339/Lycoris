import os
import logging
from pathlib import Path
import pdb
logger = logging.getLogger(__name__)
#C:\Users\x\.Driver
path = os.path.normpath(str(Path.home()) + '\.Driver')
print(path)
print(logger.warning('voasvb'))

 
# (...)
 


import sqlite3 as dbapi
 
bbdd = dbapi.connect("bbdd.dat")
 
cursor = bbdd.cursor()
cursor.execute("""create table agenda (nombre text, telefono text, ciudad text)""")
cursor.execute("""insert into agenda values ('Santi', '12345678', 'Valencia')""")
bbdd.commit()
cursor.execute("""select * from agenda where ciudad='Valencia'""")
 
for row in cursor.fetchall():
   print( row)
 
cursor.close()
bbdd.close()