import requests as re 
import json 


class lnbot:
	def __init__(self, token: str):
		self.api = "https://api.telegram.org/bot"+token+"/"
		print("Bot Started ....... For Live Counting")
			
	def edit(self,
	       chat_id: str, 
	       message_id : int , 
	       text : str ,
	       disable_webpage : bool= None,
	       parse_mode :str = None  ):
	        	edit_api = self.api +"editMessageText"
	        	data = {
	        	"chat_id": chat_id,
	        	"message_id" : message_id,
	        	"text": text,
	        	"parse_mode" : parse_mode,
	        	"disable_web_page_preview" : disable_webpage	        	
	        	}
	        	response = re.post(edit_api,data)
	        	
	        	
	
	def count(self , chat_id: str):
		 count_api = self.api +"getChatMembersCount"
		 data = { "chat_id": chat_id
		 }
		 res = re.post(count_api,data)
		 value = res.json()
		 return value["result"]
