


import sys
sys.path.append('./')

from functions_plot import *
from class_cryptos import *
import sqlite3
from functions_plot import *
import json
import pandas as pd
import time


def list_tables_and_counts(db_file="SQL_database/crypto.db"):
    # Establish connection to the database
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Get the list of tables in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # For each table, retrieve the count of rows
    tables_with_counts = {}
    for table in tables:
        table_name = table[0]
        cur.execute(f"SELECT COUNT(*) FROM '{table_name}';")
        count = cur.fetchone()[0]
        tables_with_counts[table_name] = count

    # Close the connection
    con.close()

    return tables_with_counts

def print_list_of_tables_and_count():
    tables_counts = list_tables_and_counts()
    for table, count in tables_counts.items():
        print(f"Table '{table}' contains {count} rows.")

def iterate_ada_table(db_file="SQL_database/crypto.db"):
    # Establisher la connexion à la base de données
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Sélectionner toutes les lignes de la table "ADA"
    cur.execute("SELECT * FROM ADA")
    
    # Itérer sur les résultats de la requête
    for row in cur.fetchall():
        # row est un tuple contenant les valeurs de chaque colonne dans la ligne actuelle
        # Vous pouvez accéder aux valeurs individuelles par leur index dans le tuple
        # Par exemple, row[0] pour la première colonne, row[1] pour la deuxième, et ainsi de suite
        # Faites ce que vous avez besoin de faire avec chaque valeur
        print(row)  # Par exemple, ici, nous imprimons simplement la ligne
    
    # Fermer la connexion
    con.close()

    return row

def get_last_index(table_name, db_file="SQL_database/crypto.db"):
    # Établir la connexion à la base de données
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Exécuter une requête SQL pour obtenir le nombre total de lignes dans la table spécifiée
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")

    # Récupérer le nombre total de lignes
    total_rows = cur.fetchone()[0]

    # Fermer la connexion
    con.close()

    return total_rows - 1

def get_row_at_index(table_name, index, db_file="SQL_database/crypto.db"):
    # Établir la connexion à la base de données
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    # Exécuter une requête SQL pour sélectionner la ligne à l'indice spécifié dans la table spécifiée
    cur.execute(f"SELECT * FROM {table_name} LIMIT 1 OFFSET ?", (index,))

    # Récupérer la ligne à l'indice spécifié
    row = cur.fetchone()

    # Fermer la connexion
    con.close()

    return row

def plot_from_json(json_data):
    # Charger les données JSON dans un DataFrame pandas
    df = pd.DataFrame(json_data, columns=['time', 'value_USDC'])

    # Convertir les timestamps en objets de date/heure
    df['time'] = pd.to_datetime(df['time'], unit='ms')

    # Tracer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['value_USDC'], color='blue', label='Price (USD)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('ADA Price History')
    plt.legend()
    plt.grid(True)
    plt.show()








