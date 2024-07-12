# Development

## Base Django Project

```bash
make django-base
cd django-base
django-admin startproject config .
django-admin startapp app
rye init
rye add django

# 実行
rye run python manage.py makemigrations
rye run python manage.py migrate
rye run python manage.py createsuperuser
rye run python manage.py runserver
```

## pyproject.toml

```toml
[tool.rye.scripts]
server = { cmd = "python manage.py runserver" }
manage = { cmd = "python manage.py " }
```

## appの追加
