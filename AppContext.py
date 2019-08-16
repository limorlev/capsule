import json
import settings

class AppContext(object):
    def __init__(self):
        pass
    
    def get_environment(self):
        result = settings.DEFAULT_ENVIRONMENT
        try:
            with open(settings.CONFIGURATION_FILE) as input_json_file:
                configuration_content = input_json_file.read()
                configuration = json.loads(configuration_content)
            result = configuration['environment']
        except:
            pass
        return result
    