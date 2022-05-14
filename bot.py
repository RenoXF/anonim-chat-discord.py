import discord

client = discord.Client()

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="modmail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[Anonim Chat]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("" + mod_message)


client.run('ODg3NTk0MTc3Njc4OTQyMjc4.GXSTyC.JlzF8k3B1eui6ICf2kJJvBrzzDZD8Isa4l63Kk')
