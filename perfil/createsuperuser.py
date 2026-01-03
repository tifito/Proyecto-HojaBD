from django.contrib.auth.models import User

# Solo ejecuta si no existe un superusuario con ese username
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@correo.com',
        password='12345678'
    )
    print("Superusuario creado!")
else:
    print("Ya existe el superusuario")
