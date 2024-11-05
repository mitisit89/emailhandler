
# how to run
install redis

```python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations emails
python manage.py migrate
daphne -b 0.0.0.0 -p 8001 emails.asgi:application
```
