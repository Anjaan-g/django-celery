import os
from decouple import config
from .base import *

ENVIRONMENT = config('ENVIRONMENT')
if ENVIRONMENT=='LOCAL':
    from .local import *
elif ENVIRONMENT=='PRODUCTION':
    from .production import *
elif ENVIRONMENT=='STAG':
    from .stag import *
else:
    print("Invalid Env")