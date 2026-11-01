# Fitness & Nutrition Tracker

O aplicație desktop (PyQt6 + SQLite/SQLAlchemy + Matplotlib) care creează un plan personalizat de antrenament și nutriție, monitorizează activitățile cu un temporizator Start/Stop și generează grafice cu progresul tău. Include teme vizuale deschisă (Light) și întunecată (Dark).

## Funcționalități

- Înregistrare, autentificare, deconectare, expirare a sesiunii la inactivitate; parole securizate cu hash PBKDF2 și salt
- Chestionar de configurare inițială (dietă, sex, vârstă, înălțime, greutate, timp disponibil, obiectiv)
- Motor de recomandări (BMR Mifflin-St Jeor, calorii ajustate în funcție de obiectiv, macronutrienți, program săptămânal de antrenament, sugestii de mese adaptate dietei)
- Înregistrare manuală a alimentelor și a activităților trecute
- Monitorizare Start/Stop: evenimentele sub **5 minute sunt ignorate**; evenimentele valide primesc un calcul al caloriilor (MET x greutate x ore) și un scor (durată x ponderea activității)
- Sumar zilnic: calorii consumate/arse, calorii nete, timp activ, scor
- Analize: grafice cu scorul zilnic și caloriile nete, adaptate temei vizuale active
- Comutator Temă Întunecată/Deschisă (starea este reținută între lansări)

## Structura proiectului

```

fitness_app/
├── main.py
├── requirements.txt
├── pytest.ini
├── database/   # engine, sessions, seed data
├── models/     # SQLAlchemy models + enums
├── services/   # business logic (no GUI imports)
├── ui/         # PyQt6 views, widgets, theme (QSS)
├── utils/      # security, validators
└── tests/
```

## Configurare (linie de comandă)

Necesită Python 3.10+.

```bash
git clone <url-ul-repo-ului-tău>
cd fitness_app
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Configurare (PyCharm)
File > Open și selectează folderul clonat fitness_app.

File > Settings > Project > Python Interpreter > Add Interpreter > Add Local Interpreter > Virtualenv Environment > New, interpreter de bază Python 3.10+.

Deschide requirements.txt; dă click pe Install requirements din bara notificării (sau rulează pip install -r requirements.txt în terminalul PyCharm).

Dă click dreapta pe main.py > Run 'main'.

## Teste

```bash
pytest
```

## Locația datelor
Baza de date este creată la ~/.fitness_tracker/fitness.db. Setează variabila de mediu FITNESS_TRACKER_DB pentru a folosi o altă cale. Șterge fișierul pentru a reseta aplicația.
