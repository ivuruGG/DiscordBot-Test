import os
import token
from discord import Client, Intents, Interaction, ui
from discord.app_commands import CommandTree
from discord.ui import View, Button
from amida import get_amida_result
import asyncio


class AmidaView(View):
    def __init__(self, number: int):
        super().__init__()
        self.number = number

    @ui.button(label="begin")
    async def begin_amida(self, interaction: Interaction, button: Button):
        result = get_amida_result([f"{i+1}" for i in range(self.number)])
        self.clear_items()
        await interaction.response.edit_message(view=self)

        for i in range(1, len(result)):
            await asyncio.sleep(0.25)
            await interaction.edit_original_response(content="\n".join(result[: i + 1]))


class MyClient(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        commands = await self.tree.sync()
        print(commands)

    async def on_ready(self):
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        print("------")


intents = Intents.default()
client = MyClient(intents=intents)


@client.tree.command()
async def amida(interaction: Interaction, number: int):
    view = AmidaView(number)
    await interaction.response.send_message(f"{number}'s amida kuji", view=view)


client.run(os.getenv(token)) # type: ignore