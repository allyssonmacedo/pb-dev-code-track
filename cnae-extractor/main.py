import connect as db

# db.create_tables(False)

db.query('SELECT * FROM company.Municipios;', True)