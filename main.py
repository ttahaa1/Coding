import subprocess
import asyncio
from pyrogram import Client, filters
from pyromod import listen, helpers
from pyrogram.types import Message

# APIS
from ReverseEngineeringSectionScripts.apk_decompiler import ApkReverseEngineering
from ReverseEngineeringSectionScripts.binaries_to_cpp import PseudocodeHandler
from ReverseEngineeringSectionScripts.binary_modifier import ModifyBinaries
from ReverseEngineeringSectionScripts.dumping_handler import DumperHandler
from ReverseEngineeringSectionScripts.crc32_changer import Crc32ChangerAPI
from ReverseEngineeringSectionScripts.game_aes_keys import AESKeysAPI

from GeneralSectionScripts.google_drive_courses import GoogleDriveScraper
from KeySectionScripts.key_generator_and_validator import KeysHandler
from HackingSectionScripts.combos_generator import CombosGenerator

# Variables
from global_variables import GlobalVariables
from Utils.utils import Utilities

# Function-based async program (to increase readability and reliability)
__APP = Client(
    name=f"free_beta_bot_{GlobalVariables.BOT_VERSION.value}",
    api_id=GlobalVariables.BOT_API_ID.value,
    api_hash=GlobalVariables.BOT_API_HASH.value,
    bot_token=GlobalVariables.BOT_API_TOKEN.value,
)

apk_reversing_api: ApkReverseEngineering = ApkReverseEngineering(app=__APP)
google_drive_api: GoogleDriveScraper = GoogleDriveScraper(app=__APP)
combos_generator_api: CombosGenerator = CombosGenerator(app=__APP)
pseudocode_api: PseudocodeHandler = PseudocodeHandler(app=__APP)
binary_modifiers_api: ModifyBinaries = ModifyBinaries(app=__APP)
dumping_section_api: DumperHandler = DumperHandler(app=__APP)
crc_changer_api: Crc32ChangerAPI = Crc32ChangerAPI(app=__APP)
key_section_api: KeysHandler = KeysHandler(app=__APP)
game_aes_keys_api: AESKeysAPI = AESKeysAPI(app=__APP)
utilities_api: Utilities = Utilities(app=__APP)


async def run_commands():
    # Clone the radare2 repository
    subprocess.run(["git", "clone", "https://github.com/radare/radare2"])

    # Move into the radare2 directory
    subprocess.run(["cd", "radare2"])

    # Run the sys/install.sh script
    subprocess.run(["sys/install.sh"])

async def start_bot():
    # Start the bot
    print("Bot is running")

async def main():
    # Run the commands to setup radare2
    await run_commands()

    # Start the bot after setup
    await start_bot()

# Register commands

@__APP.on_message(filters.command(["start", "help"]))
async def start_help(client: Client, message: Message) -> None:
    """
    Description:
    Sends a welcome message and a help menu when the user sends /start or /help command.

    Parameters:
    - client (Client): The Pyrogram Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /start or /help command.
    Example usage:
    /start
    """

    await utilities_api.increment_in_usage_file()
    keyboard = helpers.ikb(GlobalVariables.HELP_KEYBOARD_MENU.value)
    await utilities_api.send_text_message(client=client,
                                          message=message,
                                          text=GlobalVariables.WELCOME_MESSAGE.value,
                                          reply_markup=keyboard)


@__APP.on_message(filters.command(["generate_key"]))
async def generate_key(client: Client, message: Message) -> None:
    """
    Description:
    Generates a new key for use in the bots functionalities.

    Parameters:
    - client (Client): The Pyrogram Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /generate_key command.
    Example usage:
    /generate_key
    """

    await utilities_api.increment_in_usage_file()
    await key_section_api.generate_new_key(client=client, message=message)


@__APP.on_message(filters.command(["set_key"]))
async def register_key(client: listen.Client, message: Message) -> None:
    """
    Description:
    Registers a new key provided by the user for specific functionalities.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /set_key command.
    Example usage:
        /set_key key_value
    """

    await utilities_api.increment_in_usage_file()
    await key_section_api.register_new_key(client=client, message=message)


@__APP.on_message(filters.command(["time_left"]))
async def key_expiring_time(client: Client, message: Message) -> None:
    """
    Description:
    Calculates the remaining time for an active key.

    Parameters:
    - client (Client): The Pyrogram Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /time_left command.
    Example usage:
    /time_left
    """

    await utilities_api.increment_in_usage_file()
    await key_section_api.calculate_key_remaining_time(client=client, message=message)


@__APP.on_message(filters.command(["dump"]))
async def dumping_binaries(client: listen.Client, message: Message) -> None:
    """
    Description:
    Handles the process of dumping binary files.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /dump command.
    Example usage:
    /dump dumping_option
    """
    
    await utilities_api.increment_in_usage_file()
    await dumping_section_api.dumping_binary_files(client=client, message=message)


@__APP.on_message(filters.command(["pseudocode"]))
async def decompile_binaries(client: listen.Client, message: Message) -> None:
    """
    Description:
    Decompiles binary files into pseudocode.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /pseudocode command.
    Example usage:
    /pseudocode lib.so
    """

    await utilities_api.increment_in_usage_file()
    await pseudocode_api.decompile_cpp_file(client=client, message=message)


@__APP.on_message(filters.command(["decompile_apk"]))
async def reverse_engineer_apks(client: listen.Client, message: Message) -> None:
    """
    Description:
    Reverse engineers APK files.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /decompile_apk command.
    Example usage:
    /decompile_apk apk_file.apk
    """

    await utilities_api.increment_in_usage_file()
    await apk_reversing_api.decompile_apk_file(client=client, message=message)


@__APP.on_message(filters.command(["mod_lib"]))
async def mod_lib(client: listen.Client, message: Message) -> None:
    """
    Description:
    Modifies libraries using brute force.

    Note:
    This is specifically made for pubg-mobile game of unreal-engine-4

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /mod_lib command.
    Example usage:
    /mod_lib lib.so
    """

    await utilities_api.increment_in_usage_file()
    await binary_modifiers_api.modify_binaries_by_brute_force(client=client, message=message)


@__APP.on_message(filters.command(["crc32_changer"]))
async def crc32_changer(client: listen.Client, message: Message) -> None:
    """
    Description:
    Changes CRC32 values for binaries.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /crc32_changer command.
    Example usage:
    /crc32_changer
    """

    await utilities_api.increment_in_usage_file()
    await crc_changer_api.crc32changer(client=client, message=message)


@__APP.on_message(filters.command(["aes_keys"]))
async def aes_keys(client: listen.Client, message: Message) -> None:
    """
    Description:
    Manages AES keys for the game.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /aes_keys command.
    Example usage:
    /aes_keys
    """

    await utilities_api.increment_in_usage_file()
    await game_aes_keys_api.aes_key(client=client, message=message)


@__APP.on_message(filters.command(["gen_combo"]))
async def combos_generator(client: listen.Client, message: Message) -> None:
    """
    Description:
    Generates combinations for specific purposes.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /gen_combo command.
    Example usage:
    /gen_combo
    """

    await utilities_api.increment_in_usage_file()
    await combos_generator_api.generate_combos(client=client, message=message)


@__APP.on_message(filters.command(["courses"]))
async def courses_fetcher(client: listen.Client, message: Message) -> None:
    """
    Description:
    Scrapes Google Drive for available courses.

    Parameters:
    - client (listen.Client): The Pyrogram Listen Client instance.
    - message (Message): The Pyrogram Message object.

    Returns:
    None: This function does not return anything.

    Usage:
    This function is triggered when the user sends /courses command.
    Example usage:
    /courses
    """

    await utilities_api.increment_in_usage_file()
    await google_drive_api.scrape_google_drive(client=client, message=message)


print("Bot is running")
__APP.run()
