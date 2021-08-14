# Setup

Install postgress and do the initial configuration for your system.
Remember to also start the database.

Create a new user with name `pforms_role` and password `12345`.
```
$ createuser --interactive
```

Create a new database called `pforms`.
```
$ createdb pforms
```

Install falsk-sqlalchemy
```
$ pip install flask-sqlalchemy
```

Now launch the setup scritp that will initalize the database.
```
$ python setup.py
```

# TODO

- scrivere documento di progetto
- impementare i modelli ORM per il database in SQLAlchemy
  - tabella questionario
  - tabella domande
  - tabella risposte
- implementare meccanismo di login sicuro
- implementare meccanismo di creazione questionario
- implementare meccanismo di risposte al questionario
- implementare tool di analisi statistica