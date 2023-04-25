import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'energy_dx_gui.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from energy_dx_gui.models import User


username = 'admin3'
password = 'admin3'
hashed_password = make_password(password)

user = User.objects.create(username=username, password=hashed_password)
