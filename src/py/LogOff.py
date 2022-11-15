import discord
import os, sys, datetime, json

class MyClient(discord.Client):

  #メッセージが書き込まれた時
  async def on_message(self, message):
  #送信者がbot自身の場合はコマンドを無効にする
  if message.author.bot:
    print("bot送信\n")
    return

  if ".logoff" in message.content:
    #ログオフ
    await self.Logoff(message)
    return

def main():
  #環境変数からtokenを取ってくる
  TOKEN = os.getenv("TOKEN")
  #すべての機能を使えるようにする
  intents = discord.Intents.all()
  #intentsは必須パラメータ
  client = MyClient(intents=intents)
  #Discord接続
  client.run(TOKEN)

if __name__ == "__main__":
    main()
