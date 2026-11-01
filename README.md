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

