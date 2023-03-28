# django-scheulde

Uruchomienie :

Wygeneruj secert key
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

skopiuj wygenerowany klucz

stwórz plik .env następnie dodaj scieżke
SECRET_KEY = 'wygenerowan secert key'

>
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
