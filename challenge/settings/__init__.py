try:
    from challenge.settings.active import *
except ImportError:
    from challenge.settings.production import *
