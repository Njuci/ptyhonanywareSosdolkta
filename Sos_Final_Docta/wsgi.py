    
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sos_Final_Docta.settings')

application = get_wsgi_application()
app=application