![](https://ce.prograd.ufg.br/up/569/o/images.png?1533651349)
# Django | File Transfer

### Inicializando o container com Docker Run:

- Modo interativo:
    - `docker run --rm -ti -p 8000:8000 wsalles/django-file-transfer:latest`

- Modo daemon:
    - `docker run --rm -d -p 8000:8000 wsalles/django-file-transfer:latest`

### Acessando a plataforma pelo browser:*
- URL: http://IP_DO_SERVIDOR:8000
    - Usuário: admin
    - Senha: admin123

### Dica:

Para criar um **super user**, basta executar o comando abaixo com o container em execução:
```
docker exec -ti $(docker ps | grep "django-file-transfer" | awk '{print $1}') python3 manage.py createsuperuser
```

### Persistir os dados:
- Criar volume: `docker volume create fs_ft`
- Rode novamente:
```
docker run -ti \
    -p 8000:8000 \
    -v  fs_ft:/app \
    wsalles/django-file-transfer:latest
```



#### Autor:
Wallace Salles < [wallace_robinson@hotmail.com](mailto:wallace_robinson@hotmail.com) >

#### GitHub:
[https://github.com/wsalles/django-file-transfer](https://github.com/wsalles/django-file-transfer)