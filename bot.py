import random

import discord
from discord.ext import commands

TOKEN = "BOT TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!", intents=intents, description="Bot to randomly generate weather."
)


async def weather_pic(temp: int):
    if temp <= 32:
        snow = random.randint(1, 10)
        if snow <= 5:
            return discord.File(
                fp="images/snow.png", filename="weather.png", description="snowy"
            )
        else:
            return discord.File(
                fp="images/sunny.png", filename="weather.png", description="sunny"
            )
    weather_random = random.randint(1, 12)
    if weather_random == 1:
        return discord.File(
            fp="images/rain.png", filename="weather.png", description="rainy"
        )
    if weather_random >= 2 and weather_random <= 4:
        return discord.File(
            fp="images/cloudy.png", filename="weather.png", description="cloudy"
        )
    if weather_random >= 5 and weather_random <= 7:
        return discord.File(
            fp="images/partly-sunny.png",
            filename="weather.png",
            description="partly sunny",
        )
    if weather_random >= 8:
        return discord.File(
            fp="images/sunny.png", filename="weather.png", description="sunny"
        )


@bot.event
async def on_ready():
    print("Logged in as", bot.user)


@bot.command(name="weather")
async def test(ctx: commands.Context):
    await ctx.message.delete()
    temp_f = random.randint(-32, 100)
    temp_c = round((temp_f - 32) / 1.8, 1)
    wind_speed_mph = random.randint(0, 50)
    if wind_speed_mph == 0:
        wind_speed = "calm"
    else:
        wind_dir = random.choice(
            ["WNW", "NNW", "NNE", "ENE", "ESE", "SSE", "SSW", "WSW", "N", "S", "E", "W"]
        )
        wind_speed = f"{wind_dir} at {wind_speed_mph} mph ({round(wind_speed_mph*1.6093, 1)} kph)"
    pic = await weather_pic(temp_f)
    embed = discord.Embed(title="Your Weather Report!")
    embed.add_field(
        name=f"{temp_f}°F ({temp_c}°C) with {pic.description} conditions.",
        value=f"Winds are {wind_speed}.",
    )
    embed.set_image(url="attachment://weather.png")
    await ctx.send(file=pic, embed=embed)


bot.run(TOKEN)
