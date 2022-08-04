import json

class Environment:

    def __init__(self, environment):
        with open("secret.json", "r") as read_file:
            credentials = json.load(read_file)
            
        self.environment = environment
        if environment == 'production':
            self.server = credentials['server']
            self.database = credentials['db']
            self.username = credentials['username']
            self.password = credentials['password']
        elif environment == 'development':
            self.server = credentials['server']
            self.database = credentials['db']
            self.username = credentials['username']
            self.password = credentials['password']
        else:
            print('env does not exist')

    def Environment(self):
        return self.environment

    def Server(self):
        return self.server

    def Database(self):
        return self.database

    def Username(self):
        return self.username

    def Password(self):
        return self.password
    
