import discord
import discord.ext

bot = discord.Bot()

suggestionchannel1ID = 701192633044697220
suggestionchannel2ID = 734093978357596241
bugchannelID = 604468189325295642

@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")

@bot.slash_command(description='Replys with pong.')
async def ping(ctx):
  await ctx.respond("Pong!")

@bot.slash_command(description='Create a suggestion.')
async def suggest(
  ctx,
  suggestion_title: discord.Option(discord.SlashCommandOptionType.string, 'The title for your Suggestion'),
  suggestion: discord.Option(discord.SlashCommandOptionType.string, 'Your Suggestion')
):
  if ctx.channel == bot.get_channel(suggestionchannel1ID) or ctx.channel == bot.get_channel(suggestionchannel2ID):
    if len(f'{suggestion_title}') <= 100:
      thread = await ctx.channel.create_thread(name=f"{suggestion_title}", message=None, auto_archive_duration=10080, type=discord.ChannelType.public_thread, reason="New Suggestion")
      await ctx.respond('Suggestion Added!', delete_after=5, ephemeral=True)
      msgtopin = await thread.send(f'Suggestion: {suggestion}')
      await msgtopin.pin()
    else:
      await ctx.respond('Your title is too long!', delete_after=5, ephemeral=True)
  else:
    await ctx.respond('You can\'t make suggestions in this channel!', delete_after=5, ephemeral=True)


@bot.slash_command(description='Report a bug.')
async def report(
  ctx,
  bug_title: discord.Option(discord.SlashCommandOptionType.string, 'The title for your Bug Report'),
  bug: discord.Option(discord.SlashCommandOptionType.string, 'Your Bug Report')
):
  if ctx.channel == bot.get_channel(bugchannelID):
    if len(f'{bug_title}') <= 100:
      thread = await ctx.channel.create_thread(name=f"{bug_title}", message=None, auto_archive_duration=10080, type=discord.ChannelType.public_thread, reason="New Bug")
      await ctx.respond('Bug Report Added!', delete_after=5, ephemeral=True)
      msgtopin = await thread.send(f'Bug: {bug}')
      await msgtopin.pin()
    else:
      await ctx.respond('Your title is too long!', delete_after=5, ephemeral=True)
  else:
    await ctx.respond('You can\'t make bug reports in this channel!', delete_after=5, ephemeral=True)


bot.run("OTkyNTAyNjM0NjE3NTAzODM2.GmL1P7.FPcPkS2psgAKPUoL9uc7fJy-j9uACkA3XCezNI")