import signal
import ffmpeg  
from pyrogram import Client, filters
from pytgcalls import GroupCall
import youtube_dl
ADMIN = 923943045
API_ID = "5506621"
API_HASH = "5a8fd4a251594493d8ff2e1960f99ce2"
SESSION_NAME = "BQBS3pLb688arsVZ_ROjeMdyu2wsQsnfq0q6UcU3ag0bq47xl9aWXOqKaA8La9m07Gg68sN3dtPFePxxgLaWaT6IUpVo7gQsDr_q4laqIzSu0tBZFoPjguNtNBXj57oPxK9BG44UYwDuf8q4KQRKQedSy5GUlkb0hSaElH9pZjSe2-_ocb0yMzuMdqX7nmplTO9UQ-JkZ7_aq_aga5PxomCorrN3qkxgMdYJUYP_UIjEffba0ZhhRgFTMVO5jYx7fEPXHQPpjRls7zMkP3uajKGedGqPmmE8RHxEdPljPUpZL2xNqYlaoj3gBet15cJIoP2sJ6GI8wtQf39FkOFArKcMNUAQA"


app = Client(SESSION_NAME, API_ID, API_HASH)

HELP =""" Radio stations:

1. https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8

2. https://filmymirchihdliv-lh.akamaihd.net/i/FilmyMirchiHDLive_1_1@336266/master.m3u8


To start replay to this message with command /play <ID>
To stop use /stop command"""


GROUP_CALLS = {}
FFMPEG_PROCESSES = {}

@app.on_message( filters.user(ADMIN) & filters.command('help',prefixes='!'))
async def help(client,message):
 await message.reply_text(HELP)


@app.on_message( filters.user(ADMIN) & filters.command(["play"]))
async def start(client,message):
       input_filename = f'radio-{message.chat.id}.raw'
       group_call = GROUP_CALLS.get(message.chat.id)
       if group_call is None:
           group_call = GroupCall(client, input_filename, path_to_log_file='')
           GROUP_CALLS[message.chat.id] = group_call
       process = FFMPEG_PROCESSES.get(message.chat.id)
       if process:
       	process.send_signal(signal.SIGTERM)
       try:
       	ydl_opts = {}
       	url = message.text.split('/play')[1].replace(" ", "")
       	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       		meta = ydl.extract_info(url, download=False)
       		formats= meta.get('formats', [meta])[:1]
       		for f in formats:
       			url = f['url']
       except:
       	return
       station_stream_url = url 
       await group_call.start(message.chat.id)
       process = ffmpeg.input(station_stream_url).output( input_filename, format='s16le', acodec='pcm_s16le', ac=2, ar='48k'  ).overwrite_output().run_async()
       FFMPEG_PROCESSES[message.chat.id] = process
       await message.reply_text('Radio is playing...')

@app.on_message( filters.user(ADMIN) & filters.command(["stop"]))
async def stop(client,message):
    group_call = GROUP_CALLS.get(message.chat.id)
    if group_call:
     await group_call.stop()
    process = FFMPEG_PROCESSES.get(message.chat.id)
    if process:
     process.send_signal(signal.SIGTERM)
   

app.run()
