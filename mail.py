from http import cookies
from ssl import SSL_ERROR_SSL
import requests
import time

class GuerillaMail:
    def __init__(self) -> None:
        self.baseurl="http://api.guerrillamail.com/ajax.php"
    
    def make_request(self, action:str, method:str,  parameter:dict=None, headers:dict=None, cookies:dict=None):
        param_str = ""
        print(parameter)
        if parameter is not None:
            for k,v in parameter.items():
                param_str+=f"&{k}={v}"
        if method=="GET":
            res = requests.get(url=f"{self.baseurl}?f={action}{param_str if param_str != '' else ''}", headers=headers, cookies=cookies)
            return res
        elif method=="POST":
            res = requests.post(url=f"{self.baseurl}?f={action}{param_str if param_str != '' else ''}", headers=headers, cookies=cookies)
            return res

    def get_email_address(self):
        return self.make_request(action="get_email_address", parameter={"lang":"en"}, method="GET")
    
    def check_email(self, sid):
        return self.make_request(action="check_email", method="GET", cookies={"PHPSESSID":sid})

gm = GuerillaMail()
def email_address():
    email = gm.get_email_address().json()["email_addr"]
    print(email)
    return email
