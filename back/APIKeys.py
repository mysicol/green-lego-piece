import os
import dotenv

class APIKeys:
    def set_var(variable):
        if variable in os.environ:
            del os.environ[variable]
        dotenv.load_dotenv()
        
    def get_key(variable):
        return os.environ[variable]