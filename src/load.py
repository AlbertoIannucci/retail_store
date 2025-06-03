from extract_transform import modello
import pymysql

# Funzione per ottenere la stringa di connessione
def _getconnection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="retail_store_db"
    )

# Funzione per il caricamento dei dati nel db (per tabelle di decodifica)
def load_decodifica(df):
    with _getconnection() as connection:
        with connection.cursor() as cursor:
            # Conservo solo i valori univoci relativi a ciascun attributo da inserire
            categorie_uniche = df["category"].unique()
            valori_category = [(cat,) for cat in categorie_uniche]

            location_uniche = df["location"].unique()
            valori_location = [(loc,) for loc in location_uniche]

            payment_method_unici = df["payment_method"].unique()
            valori_payment_method = [(pm,) for pm in payment_method_unici]

            # Caricamento dati nelle diverse tabelle
            cursor.executemany("INSERT INTO category(name) VALUES (%s)", valori_category)
            cursor.executemany("INSERT INTO location(name) VALUES (%s)", valori_location)
            cursor.executemany("INSERT INTO payment_method(name) VALUES (%s)", valori_payment_method)

            connection.commit()
            print("Dati caricati con successo")

# Funzione per il caricamento dei dati nella main table
def load(df):
    with _getconnection() as connection:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO sale (id_transaction, id_customer, fk_id_category, item, price_per_unit,
                                                quantity, total_spent, fk_id_payment_method, fk_id_location, transaction_date, discount_applied)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
            # Preparo una lista di tuple con i dati da inserire
            valori = [
                (
                    row["id_transaction"],
                    row["id_customer"],
                    row["category_code"],
                    row["item"],
                    row["price_per_unit"],
                    row["quantity"],
                    row["total_spent"],
                    row["payment_method_code"],
                    row["location_code"],
                    row["transaction_date"],
                    row["discount_applied"]
                )
                for _, row in df.iterrows()
            ]

            cursor.executemany(sql, valori)
            connection.commit()
            print("Dati caricati con successo")

# load_decodifica(modello.dataframe_sistemato)
# load(modello.dataframe_sistemato)

