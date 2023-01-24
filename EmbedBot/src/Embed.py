import discord

client = discord.Client()
@client.event
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageメソッドでユーザー入力に反応するときも仕様は同じになります。
async def on_ready():
    embed = discord.Embed( # Embedを定義する
                          title="Example Embed",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          description="Example Embed for Advent Calendar", # Embedの説明文 必要に応じて
                          url="https://example.com" # これを設定すると、タイトルが指定URLへのリンクになる
                          )
    embed.set_author(name=client.user, # Botのユーザー名
                     url="https://repo.exapmle.com/bot", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                     icon_url=client.user.avatar_url # Botのアイコンを設定してみる
                     )

    embed.set_thumbnail(url="https://image.example.com/thumbnail.png") # サムネイルとして小さい画像を設定できる

    embed.set_image(url="https://image.example.com/main.png") # 大きな画像タイルを設定できる

    embed.add_field(name="フィールド１",value="値１") # フィールドを追加。
    embed.add_field(name="フィールド２",value="値２")

    embed.set_footer(text="made by nashiroaoi", # フッターには開発者の情報でも入れてみる
                     icon_url="https://dev.exapmple.com/profile.png")

    channel = client.get_channel(CHANNEL_ID)

    await channel.send(embed=embed) # embedの送信には、embed={定義したembed名}

client.run(TOKEN)
