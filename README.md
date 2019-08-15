# estrategia-django

### Execução via Docker compose

```bash
# Instalação do docker
$ sudo apt-get install docker-ce docker-ce-cli containerd.io

# Execução do docker compose
$ docker-compose up --build

# Criação do superuser
$ docker exec -it estrategia-django_estrategia_django_1 python manage.py createsuperuser

# Acessar http://localhost:8080/
```

### Execução de testes via Docker compose

```bash
# Criação do superuser
$ docker exec -it estrategia-django_estrategia_django_1 python manage.py test cursos
```
