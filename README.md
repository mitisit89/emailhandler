
# how to run

```bash
sudo apt install redis
```
```python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
daphne -b 0.0.0.0 -p 8001 emails.asgi:application
```

## Attention
You need create app password for each email account
