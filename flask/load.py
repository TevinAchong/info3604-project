import csv, sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
"""
cur.execute("CREATE TABLE t (review, sentiment, translated, trini_translation);") # use your column names here

with open('data.csv','r', encoding="utf-8") as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['review'], i['sentiment'], i['translated'], i['trini_translation']) for i in dr]

cur.executemany("INSERT INTO t (review, sentiment, translated, trini_translation) VALUES (?, ?, ?, ?);", to_db)
"""
cur.execute("SELECT COUNT(*) FROM t WHERE translated='1'")
cur.execute("Select trini_translation from t where translated='1'")
test = cur.fetchall()
print(test)
con.commit()
con.close()