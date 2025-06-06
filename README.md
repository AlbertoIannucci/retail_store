# 🛍️ Retail Store Data Analysis & ETL Pipeline

Questo progetto mostra un processo completo di **data cleaning**, **trasformazione**, **caricamento in database relazionale** e **analisi strategica** a partire da un dataset retail reale.

## 📂 Contenuto del repository

- `extract_transform.py`: Script per il caricamento e la pulizia del dataset originale (CSV), con gestione dei missing values e trasformazioni.
- `load.py`: Script per il caricamento dei dati nel database MySQL, incluse le tabelle di decodifica e la tabella principale.
- `report_retail_store.pdf`: Report finale con insight e raccomandazioni strategiche basate sui dati.
- `db_schema.png`: Diagramma E-R.

## 🧰 Tecnologie utilizzate

- **Linguaggi**: Python
- **Librerie principali**: `pandas`, `pymysql`
- **Database**: MySQL
- **Strumenti analitici**: Segmentazione RFM, analisi di vendita, trend stagionali, ROI promozioni

## 🧪 Funzionalità principali

### 1. Data Cleaning (ET)
- Ricostruzione di colonne mancanti tramite relazioni logiche (`Total Spent`, `Quantity`, `Price per Unit`)
- Conversioni di tipo e gestione dei NaN
- Rimappatura colonne in snake_case
- Creazione di codifiche per chiavi esterne (categorie, location, metodi di pagamento)

### 2. Database Design (Modello Relazionale)
- Tabelle: `sale`, `category`, `location`, `payment_method`
- Relazioni gestite tramite foreign key

### 3. Data Loading (L)
- Inserimento automatico dei dati tramite `pymysql`
- Separazione tra dati principali e tabelle di decodifica

### 4. Report Analitico
- Insight strategici su: top prodotti, categorie, performance stagionali, sconti, segmentazione clienti (RFM)
- Raccomandazioni per ottimizzazione vendite, retention e gestione stagionale

## 📊 Risultati Chiave

- **Transazioni analizzate**: 11.971  
- **Fatturato totale**: €2.2M  
- **Scontrino medio**: €186  
- **Crescita YoY**: +15.3%  
- **Segmentazione clienti**: Champions, Loyal, At Risk  
- **ROI stimato**: x3.2 su 12 mesi

## 🔒 Licenza

Distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.


