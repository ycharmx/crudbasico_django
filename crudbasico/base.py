import os
import json

from django.core.exceptions import ImproperlyConfigured
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LoadConfig:
    

    def __init__(self, config_file_name):
        with open(os.path.join(BASE_DIR,config_file_name)) as f:
            self.configs = json.loads(f.read())

    def get_env_var(self, setting):
        try:
            val = self.configs[setting]
            if val == 'True':
                val = True
            elif val == 'False':
                val = False
            return val
        except KeyError:
            error_msg = "ImproperlyConfigured: Set {0} environment      variable".format(setting)
            raise ImproperlyConfigured(error_msg)