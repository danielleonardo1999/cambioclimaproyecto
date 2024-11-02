import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents, description="Este es un bot para calcular huellas de carbono")

carbon_data = {
    "automóvil": 0.24,  
    "vuelo": 0.15,      
    "alimento": 2.5,   
    "electricidad": 0.5,
    "bicicleta": 0.01,
    "tren": 0.04,
    "moto": 0.18,
    "barco": 0.12,
    "bus": 0.03,
    "lavadora": 0.08,
    "secadora": 0.09,
    "nevera": 0.07,
    "computadora": 0.2,
    "telefono": 0.05,
    "tablet": 0.04,
    "televisión": 0.1,
    "radio": 0.02,
    "bombilla": 0.003,
    "aire acondicionado": 0.3,
    "ventilador": 0.02,
    "microondas": 0.06,
    "horno": 0.1,
    "ducha": 0.12,
    "baño": 0.08,
    "secador de cabello": 0.04,
    "plancha": 0.05,
    "licuadora": 0.03,
    "aspiradora": 0.07,
    "impresora": 0.03,
    "proyector": 0.1,
    "router de internet": 0.01,
    "camara portatil": 0.02,
    "reloj inteligente": 0.005,
    "consola": 0.09,
    "lampara de escritorio": 0.004,
    "chocolatera": 0.03,
    "bombilla led": 0.001,
    "taladro": 0.02,
    "martillo neumático": 0.12,
    "lavamanos": 0.03,
    "lavado de autos": 0.08,
    "monitor": 0.04,
    "laptop": 0.15
}

@bot.event
async def on_ready():
    print(f"{bot.user} se ha conectado a Discord!")

@bot.command(name="objetos")
async def list_objects(ctx):
    message = "Lista de objetos disponibles para calcular la huella de carbono:\n"
    for item in carbon_data:
        message += f"- {item}\n"
    message += "\nEscribe `!calcular <objeto> <valor>` para ingresar un valor."
    await ctx.send(message)

@bot.command(name="calcular")
async def calculate_carbon(ctx, objeto: str, valor: float):
    objeto = objeto.lower()
    if objeto in carbon_data:
        huella_base = carbon_data[objeto]
        huella_total = huella_base * valor
        await ctx.send(f"La huella de carbono aproximada para {valor} unidades de {objeto} es {huella_total:.2f} kg CO2e.")
    else:
        await ctx.send("El objeto no está en la lista. Usa `!objetos` para ver los disponibles.")

bot.run("token")
