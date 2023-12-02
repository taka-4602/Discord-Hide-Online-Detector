import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)

TOKEN = 'Botのトークンをここに'

@client.event
async def on_message(message: discord.Message):  

    if message.author.bot:
        return
    if "offline" in message.author.status:
        embed = discord.Embed(title="⚠️オフラインを検出しました⚠️", description=message.author.display_name,color=discord.Colour.red())
        try:
            embed.set_thumbnail(url=message.author.display_avatar.url)
        except:
            None
        await message.channel.send(embed=embed)

    if message.content=="spo!":
        member=message.author
        try:
            if member.activity.title:
                embed = discord.Embed(title="Spotify", description=f"### [{member.activity.title}]({member.activity.track_url})\n{member.activity.artist}",color=discord.Colour.green())
                embed.set_thumbnail(url=member.activity.album_cover_url)
                try:          
                    embed.set_footer(text=member.display_name,icon_url=member.display_avatar.url)
                except:
                    None
                await message.channel.send(embed=embed)
        except:
            await message.channel.send("あなたはSpotifyを聴いていません")

@client.event
async def on_ready():
    print(f'Thank you for running! {client.user}')
    
client.run(TOKEN)