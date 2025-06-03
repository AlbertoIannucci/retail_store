from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    # Metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sistemazione
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()

        # Calcolo Total Spent se mancante
        mask = df_sistemato['Total Spent'].isna() & df_sistemato['Price Per Unit'].notna() & df_sistemato['Quantity'].notna()
        df_sistemato.loc[mask, 'Total Spent'] = df_sistemato.loc[mask, 'Price Per Unit'] * df_sistemato.loc[mask, 'Quantity']

        # Calcolo Price Per Unit se mancante
        mask = df_sistemato['Price Per Unit'].isna() & df_sistemato['Total Spent'].notna() & df_sistemato['Quantity'].notna()
        df_sistemato.loc[mask, 'Price Per Unit'] = df_sistemato.loc[mask, 'Total Spent'] / df_sistemato.loc[mask, 'Quantity']

        # Calcolo Quantity se mancante
        mask = df_sistemato['Quantity'].isna() & df_sistemato['Total Spent'].notna() & df_sistemato['Price Per Unit'].notna()
        df_sistemato.loc[mask, 'Quantity'] = df_sistemato.loc[mask, 'Total Spent'] / df_sistemato.loc[mask, 'Price Per Unit']

        # Drop valori nan Total Spent e Quantity
        df_sistemato = df_sistemato.dropna(subset=["Total Spent", "Quantity"])

        # Conversione tipo Quantity
        df_sistemato["Quantity"] = df_sistemato["Quantity"].astype(int)

        # Sostituzione nan Discount Applied e Item
        variabili_categoriali = ["Discount Applied", "Item"]
        for col in df_sistemato.columns:
            if col in variabili_categoriali:
                df_sistemato[col] = df_sistemato.groupby("Category")[col].transform(
                    lambda x: x.fillna(x.mode()[0])
                )
        # Conversione Transaction Date
        df_sistemato["Transaction Date"] = pd.to_datetime(df_sistemato["Transaction Date"])

        # Rimappatura etichette
        df_sistemato = df_sistemato.rename(columns={
            "Transaction ID": "id_transaction",
            "Customer ID": "id_customer",
            "Category": "category",
            "Item": "item",
            "Price Per Unit": "price_per_unit",
            "Quantity": "quantity",
            "Total Spent": "total_spent",
            "Payment Method": "payment_method",
            "Location": "location",
            "Transaction Date": "transaction_date",
            "Discount Applied": "discount_applied"
        })

        # Inserimento colonne di codifica
        mappa_category = dict(zip(df_sistemato["category"].unique(), range(1, df_sistemato["category"].nunique() + 1)))
        df_sistemato["category_code"] = df_sistemato["category"].replace(mappa_category)

        mappa_payment_method = dict(zip(df_sistemato["payment_method"].unique(), range(1, df_sistemato["payment_method"].nunique() + 1)))
        df_sistemato["payment_method_code"] = df_sistemato["payment_method"].replace(mappa_payment_method)

        mappa_location = dict(zip(df_sistemato["location"].unique(), range(1, df_sistemato["location"].nunique() + 1)))
        df_sistemato["location_code"] = df_sistemato["location"].replace(mappa_location)

        return df_sistemato

# Estrazione dataset
modello = DatasetCleaner("../Dataset/dataset.csv")
# Traformazione
# Passo 1. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazioni= 12575; Variabili= 11; Tipi= object e float; Valori nan= presenti
# Passo 2. Analisi valori univoci
#modello.analisi_valori_univoci(modello.dataframe, ["Transaction ID", "Customer ID"])
# Transivtion ID -> ok
# Customer ID -> ok
# Category -> ok
# Item -> sistemazione valori nan -> moda raggruppata per Category
# Price Per Unit -> sistemazione valori nan
# Quantity -> sistemazione valori nan -> conversione tipo float a int
# Total Spent -> sistemazione valori nan
# Payment Method -> ok
# Location -> ok
# Transaction Date -> conversione tipi da object a date
# Discount Applied -> sistemazione valori nan -> moda raggruppata per Category
# Passo 3. Sistemazione attributi  Price Per Unit, Quantity e Total Spent
# Relazione che lega i tre attributi: Total Spent = Price Per Unit * Quantity
# Price Per Unit -> ok
# Totale Spent e Quantity -> presenza ancora di valori nan -> non sono disponibili entrambi gli altri due valori
# Passo 4. Drop valori nan Total Spent e Quantity
# Percentuale dataset perso = [(12574 - 11971) / 12574] * 100 = 4.7%
# Dataset perso meno del 5% -> ok
# Passo 5. Conversione tipo Quantity
# Passo 6. Sistemazione Discount Applied e Item
# Passo 7. Conversione Transaction Date
# Passo 8. Rimappatura etichette snake_case
# Passo 9. Inserisco colonne di codifica per agevolare l’implementazione di tabelle di decodifica all'interno di un database MySQL
# Colonne di codifica per: category, payment_method, location
modello.analisi_generali(modello.dataframe_sistemato)