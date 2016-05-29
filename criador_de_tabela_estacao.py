# Author: Douglas Cândido

import sqlite3

conectar = sqlite3.connect("Medicoes.db")

navegador = conectar.cursor()

navegador.execute("""
CREATE TABLE Estacao (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(30) NOT NULL,
  cidade TEXT NOT NULL,
  uf VARCHAR(2) NOT NULL)
""")

print "Tabela criada"

conectar.commit()

conectar.close()

