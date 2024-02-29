# Opis aplikacji
## 1. Wymagania
- python 3.10+
- dajngo min 5.0
- paczka Pillow
- silnik bazy sqlite3

## 2. Uruchomienie projektu
Wykonywanie polecenia
Dla Windows
```sh
python -m venv venv
```
Dla Unixa
```sh
python3 -m venv venv
```

Uruchomienie wirtualnej zmiennej środowiskowej (venv)
Dla Windows 
```sh
.\venv\Scripts\activate
```
lub (GIT bash)

```sh
source venv/Scripts/activate
```
Instalacja Django
```sh
pip install django
```
Instalacja Pillow
```sh
pip install Pillow
```
(Opcjnalnie jeżeli jest pusta baza to)
```sh
python manage.py migrate
```
oraz stworzenie superusera

```sh
python manage.py createsuperuser
```

W przyadku używania silnika sqlite3 z repo dane do logowania

```sh
login: JK_Maverick
password: QwErTy123@
```

Uruchomienia serwera
```sh
python manage.py runserver
```