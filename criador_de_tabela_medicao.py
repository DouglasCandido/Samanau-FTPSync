# Author: Douglas Cândido

import sqlite3

conectar = sqlite3.connect("Medicoes.db")

navegador = conectar.cursor()

navegador.execute("""
CREATE TABLE Medicao (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  id_estacao INTEGER NOT NULL,
  lat_g REAL NOT NULL,
  lat_m REAL NOT NULL,
  lat_p REAL NOT NULL,
  lat_s REAL NOT NULL,
  long_g REAL NOT NULL,
  long_m REAL NOT NULL,
  long_p REAL NOT NULL,
  long_s REAL NOT NULL,
  temp REAL NOT NULL,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  foreign key(id_estacao) references Estacao(id)
  )
""")

print "Tabela criada"

conectar.commit()

conectar.close()
