import configparser
config = configparser.RawConfigParser()
config.read('Configurations/config.ini')

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getUerEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        userpassword = config.get('common info', 'password')
        return userpassword
