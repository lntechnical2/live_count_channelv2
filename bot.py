from telegram import lnbot
import os
import time
TOKEN =os.environ.get("TOKEN", "") "1862725270:AAHE_xMHgkI2Ox0BqzWtrvhD0cFuUcDpu-8"
app = lnbot(TOKEN)

CHAT_ID = os.environ.get("CHAT_ID", "")
MG_ID = os.environ.get("MG_ID", "")


ch1 = []
ch2 = []
ch3 = []
ch4 = []
ch5 = []
ch6 = []
ch7 = []
ch8 = []

count1 = app.count("@cwprojects")
count2 = app.count("@InFoTel14")
count3 = app.count("@mwkbots")
count4 = app.count("@HeimanSupports")
count5 = app.count("@lntechnical")
count6 = app.count("@BX_Botz")
count7 = app.count("@EKBOTZ_UPDATE")
count8 = app.count("@spechlde")

ch1.append(count1)
ch2.append(count2)
ch3.append(count3)
ch4.append(count4)
ch5.append(count5)
ch6.append(count6)
ch7.append(count7)
ch8.append(count8)


	
while True:
	time.sleep(3)
	count_1 = app.count("@cwprojects")
	count_2 = app.count("@InFoTel14")
	count_3 = app.count("@mwkbots")
	count_4 = app.count("@HeimanSupports")
	count_5 = app.count("@lntechnical")
	count_6 = app.count("@BX_Botz")
	count_7 = app.count("@EKBOTZ_UPDATE")
	count_8 = app.count("@spechlde")
	
	
	
	if ch1[0] != count_1:
			del ch1[0]
			ch1.append(count_1)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
		  
	if ch2[0] != count_2:
			del ch2[0]
			ch2.append(count_2)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
		  
		  
	if ch3[0] != count_3:
			del ch3[0]
			ch3.append(count_3)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
		  
		  
		  
	if ch4[0] != count_4:
			del ch4[0]
			ch4.append(count_4)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
	
	if ch5[0] != count_5:
			del ch5[0]
			ch5.append(count_5)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
		  
		  
	if ch6[0] != count_6:
			del ch6[0]
			ch6.append(count_6)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
		  
	if ch7[0] != count_7:
	      	del ch7[0]
	      	ch7.append(count_7)
	      	app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
       	
       	
       	
       	
	if ch8[0] != count_8:
			del ch8[0]
			ch8.append(count_8)
			app.edit(chat_id = CHAT_ID ,message_id=MG_ID ,text = f"""
  Telegram Channel Live Subscriber Counting .... 🎉🎉
  
   [CW Projects](https://t.me/cwprojects) - {ch1[0]}
   [InFoTel](https://t.me/InFoTel14) - {ch2[0]} 
   [🇮🇳 Shrimadhav U K ✔️](https://t.me/SpEcHlDe) - {ch8[0]}
   [Mwk | links & Projects](https://t.me/mwkbots) - {ch3[0]}
   [Heiman TG Update](https://t.me/HeimanSupports) - {ch4[0]}
   [LN Technical](https://t.me/lntechnical) - {ch5[0]}
   [Bx Bots Updates](https://t.me/BX_Botz) - {ch6[0]}
   [Ek Botz Projects](https://t.me/EKBOTZ_UPDATE) - {ch7[0]}
       
    """, disable_webpage = True, parse_mode = "Markdown")
             	
