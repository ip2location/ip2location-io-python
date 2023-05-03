class Configuration:
    
    VERSION = '1.0.0'
    
    def __init__(self,apikey):
        self.key = apikey
    
    def getapikey(self):
        return self.key
    
    def getmoduleversion(self):
        return Configuration.VERSION