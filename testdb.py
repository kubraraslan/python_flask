from test import db,Human

"""
db.create_all()
human1 = Human('kubs',28)
human2 = Human('hizs',34)

db.session.add_all([human1,human2])
db.session.commit()

print(human1.id)
print(human2.id)
"""
""" READ
all_human = Human.query.all()
humin = Human.query.get(2)
print(all_human)
print(humin)"""
""" UPDATE
hum = Human.query.get(1)
hum.age = 29
db.session.add(hum)
db.session.commit()

print(hum)"""
"""SİLME
hums = Human.query.get(1)
db.session.delete(hums)
db.session.commit()
"""