import requests , getmac , typing
from datetime import datetime

GIVEACCESSBOT = "GiveAccessBot"

class BackendManager(object):
    def __init__(self,Domain:str,*args,**kwargs) -> None:
        self.Domain = Domain

    def send_get_access_request(self,msg:str=None):
        bot_url = requests.get(f"{self.Domain}/api/bot-url/{GIVEACCESSBOT}").json()['url']
        for chatinfo in requests.get(f"{self.Domain}/api/api-chats/{GIVEACCESSBOT}").json()['response']:
            params = {
                'chat_id': chatinfo.get('chat_id') ,
                'text': f"Please {chatinfo.get('chat_name')}\n\nGiveAccess Request\n\nMacAddress : {getmac.get_mac_address()}\n\n{'' if msg == None else msg}\n\n{datetime.now()}",
            }
            requests.get(
                url = bot_url ,
                params = params ,
            )
        
    def isValid(self)-> bool:
        response = requests.get(f"{self.Domain}/api/api-check-exist/{getmac.get_mac_address()}").json()
        return response.get("response").get("isExist",False)

    def bots_list(self)->typing.List[str]:
        bots = requests.get(f'{self.Domain}/api/api-list-bots/')
        return [bot.get('name') for bot in bots.json() ]

    def bot_url(self,bot_name:str)->typing.Optional[dict]:
        response = requests.get(f'{self.Domain}/api/bot-url/{bot_name}').json()
        if 'url' in response.keys():
            return response
        else :
            return None








