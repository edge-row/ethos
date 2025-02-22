import discord
from discord.ext import commands
import json
import datetime
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def start_bot():
    token = os.getenv("API_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="/", intents=intents)

    def load_checkins():
        try:
            with open("checkins.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_checkins():
        with open("checkins.json", "w") as f:
            json.dump(user_checkins, f)

    user_checkins = load_checkins()

    @bot.event
    async def on_ready():
        await bot.tree.sync()
        print(f"{bot.user} has connected to Discord!")

    @bot.tree.command(name="check_in", description="Check in for today.")
    async def checkin(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        today = datetime.date.today().strftime("%Y-%m-%d")

        if user_id not in user_checkins:
            user_checkins[user_id] = {
                "username": interaction.user.display_name,
                "last_chckin": None,
                "yearly_count": 0,
            }

        if user_checkins[user_id]["last_checkin"] != today:
            user_checkins[user_id]["username"] = interaction.user.display_name
            user_checkins[user_id]["last_checkin"] = today
            user_checkins[user_id]["yearly_count"] += 1
            save_checkins()
            print(f"{user_checkins[user_id]['username']} has checked in.")
            await interaction.response.send_message(
                f"{interaction.user.mention} Checked in successfully! You have in total {user_checkins[user_id]['yearly_count']} check-ins this year."
            )
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention} You have already checked in today."
            )

    @bot.tree.command(
        name="yearly_check_in", description="See your total check ins this year."
    )
    async def yearly_checkins(interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        if user_id not in user_checkins:
            await interaction.response.send_message(
                f"{interaction.user.mention} You have no check-ins."
            )
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention} You have a total of {user_checkins[user_id]['yearly_count']} check-ins this year."
            )

    @bot.tree.command(name="ian_is_handsome", description="Ian is sooo handsome.")
    async def ianishandsome(interaction: discord.Interaction):
        await interaction.response.send_message(f"Holy shoot Ian is so handsome 🍆")

    @bot.tree.command(name="leaderboard", description="See the leaderboard list.")
    async def leaderboard(interaction: discord.Interaction):
        sorted_checkins = sorted(
            user_checkins.items(), key=lambda x: x[1]["yearly_count"], reverse=True
        )
        leaderboard_message = "Leaderboard:\n"
        for i, (user_id, data) in enumerate(sorted_checkins, start=1):
            leaderboard_message += (
                f"{i}. {data['username']} - {data['yearly_count']} check-ins\n"
            )
        await interaction.response.send_message(leaderboard_message)

    await bot.start(token)


asyncio.run(start_bot())

