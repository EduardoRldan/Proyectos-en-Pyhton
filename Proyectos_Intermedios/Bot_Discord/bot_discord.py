import discord
from discord.ext import commands

# Configurar intents para recibir eventos
intents = discord.Intents.default()
intents.messages = True

# Crear el bot con prefijo !
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"🤖 {bot.user} está conectado y listo para usarse!")

# Comando simple de saludo
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿Cómo estás? 😊")

# Comando para repetir un mensaje
@bot.command()
async def repetir(ctx, *, mensaje):
    await ctx.send(mensaje)

# Iniciar el bot (Reemplaza "TU_TOKEN_AQUI" con tu token real)
bot.run("TU_TOKEN_AQUI")
