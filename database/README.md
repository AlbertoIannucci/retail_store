## 🗄️ Cartella `database/` – Progettazione del Database Relazionale

Questa cartella contiene gli asset relativi al **modello relazionale** utilizzato per ospitare i dati del progetto nel database MySQL.

### 📁 Contenuto

| File | Descrizione |
|------|-------------|
| `retail_store_db.sql` | Script SQL per la creazione delle tabelle (`sale`, `category`, `location`, `payment_method`) e delle relative chiavi primarie/esterne |
| `db_schema.png` | Diagramma ER (Entity-Relationship) del database per una comprensione visiva della struttura |

### 🧱 Struttura del database

Il database è progettato in modo **relazionale e normalizzato**, con l'obiettivo di:
- Separare le tabelle di decodifica (es. `category`, `payment_method`) da quella principale (`sale`)
- Minimizzare la ridondanza
- Favorire integrità referenziale e performance nelle query

### 🔗 Relazioni principali

- `sale.fk_id_category` → `category.id`
- `sale.fk_id_payment_method` → `payment_method.id`
- `sale.fk_id_location` → `location.id`
