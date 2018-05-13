import re

class check(object):
    def __init__(self,ip):
        self.ip = ip
    def check(self):
        try:
            if re.search(r'^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$',self.ip) != None:
                return True
            else:
                return False
        except:
            return False