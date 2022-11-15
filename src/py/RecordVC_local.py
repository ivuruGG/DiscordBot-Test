import discord
from pydub import AudioSegment

intents = discord.Intents().all()
bot = discord.Bot(intents=intents)

Token=""

@bot.slash_command()
async def start_record(ctx:discord.ApplicationContext):

        # コマンドを使用したユーザーのボイスチャンネルに接続
        try:
            vc = await ctx.author.voice.channel.connect()
            await ctx.respond("録音開始...")
        except AttributeError:
            await ctx.respond("ボイスチャンネルに入ってください。")
            return
        
        # 録音開始。mp3で帰ってくる。wavだとなぜか壊れる。
        ctx.voice_client.start_recording(discord.sinks.MP3Sink(), finished_callback, ctx)

@bot.slash_command()
async def stop_recording(ctx:discord.ApplicationContext):
        # 録音停止
        ctx.voice_client.stop_recording() 
        await ctx.respond("録音終了!")
        await ctx.voice_client.disconnect()

# 録音終了時に呼び出される関数
async def finished_callback(sink:discord.sinks.MP3Sink, ctx:discord.ApplicationContext):
    # 録音したユーザーの音声を取り出す
    for user_id, audio in sink.audio_data.items():
        # mp3ファイルとして書き込み。その後wavファイルに変換。
        song = AudioSegment.from_file(audio.file, format="mp3")
        song.export(f"./{user_id}.wav", format='wav')


bot.run(Token)
