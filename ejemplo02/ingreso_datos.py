from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club
from genera_tablas import Jugador

from configuracion import cadena_base_datos

import csv

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo_club = open('data/datos_clubs.txt', 'r', encoding='utf-8')
archivo_jugador = open('data/datos_jugadores.txt', 'r', encoding='utf-8')

club_json = csv.reader(archivo_club, delimiter=';')
jugador_json = csv.reader(archivo_jugador, delimiter=';')
for c in club_json:
    print(c)
    c = Club(nombre=c[0], deporte=c[1], fundacion=int(c[2]))
    for j in jugador_json:
        print(j)
        j = Jugador(club=c, posicion=j[1], dorsal=int(j[2]), nombre=j[3])
        session.add(j)
    session.add(c)

session.commit()
