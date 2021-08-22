import os
import signal
import ffmpeg  
from pyrogram import Client, filters
from pytgcalls import GroupCall
import youtube_dl
ADMIN = 923943045
API_ID = "5506621"
API_HASH = "5a8fd4a251594493d8ff2e1960f99ce2"
SESSION_NAME = "BQAXcmBjLhuqsl24XhSOeb03P4Nv6P6QBntr4S53L4151oaMqYYdX66BDdMeRabwY46EXjwT-hMF6pUMa_UYTp-h4KNQhjTaoPCiubXtgFwpdUOFn7RygXHS9UxsjGIzRsvRaL2nXxLKeoVFjxJgK29qhPLoVox0NavPoklp8QEVp5gX295AcyDDcXRL95l-oKKd1-eJCwgPwH41Kw9UIGSKBdBTfNXu08hncH1kvuarZGuvbtDQ2jLEMUdcusJaBXv1NcZH_iKQN-HB6MROGFUlxvv5YSM_e_cXnBd1hMO_jdQ4C-ywO_0TR40XJLfz6SLWLxVH8MqAGI1YizLLBuQPNxJAhQA"
ID = -1001401107958
YT_LINK ="https://youtu.be/3ZswT0i7KsI"
app = Client(SESSION_NAME, API_ID, API_HASH)

HELP =""" Radio stations:

1. https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8

2. https://filmymirchihdliv-lh.akamaihd.net/i/FilmyMirchiHDLive_1_1@336266/master.m3u8


To start replay to this message with command /play <ID>
To stop use /stop command"""


GROUP_CALLS = {}
FFMPEG_PROCESSES = {}

@app.on_message( filters.user(ADMIN) & filters.command('help',prefixes='.'))
async def help(client,message):
 await message.reply_text(HELP)


@app.on_message( filters.user(ADMIN) & filters.command("play",prefixes='.'))
async def start(client,message):
       input_filename = f'radio-{ID}.raw'
       group_call = GROUP_CALLS.get(ID)
       if group_call is None:
           group_call = GroupCall(client, input_filename, path_to_log_file='')
           GROUP_CALLS[ID] = group_call
       process = FFMPEG_PROCESSES.get(ID)
       if process:
        process.send_signal(signal.SIGTERM)
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        	meta = ydl.extract_info(YT_LINK, download=False)
        	formats= meta.get('formats', [meta])[:1]
        	for f in formats:
        		url = f['url']
        station_stream_url = url
        await group_call.start(ID)
        process = ffmpeg.input(station_stream_url).output( input_filename, format='s16le', acodec='pcm_s16le', ac=2, ar='48k'  ).overwrite_output().run_async()
        FFMPEG_PROCESSES[ID] = process
        print('........ playing..........')

@app.on_message( filters.user(ADMIN) & filters.command("stop",prefixes='.'))
async def stop(client,message):
    group_call = GROUP_CALLS.get(ID)
    if group_call:
     await group_call.stop()
    process = FFMPEG_PROCESSES.get(ID)
    if process:
     process.send_signal(signal.SIGTERM)
   

app.run()
