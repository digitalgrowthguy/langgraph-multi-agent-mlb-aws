import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Configuration ---
# IMPORTANT: Replace "YOUR_TELEGRAM_BOT_TOKEN" with the token you get from BotFather.
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" 

# IMPORTANT: Replace "YOUR_WEB_APP_URL" with the HTTPS URL where you host your moon_mission_tapper.html file.
WEB_APP_URL = "YOUR_WEB_APP_URL" 

# --- Logging Setup ---
# This sets up logging to see errors and bot activity in your console.
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# --- Command Handlers ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handler for the /start command.
    Sends a welcome message and explains how to play the game.
    """
    welcome_message = (
        "🚀 Welcome to Moon Mission Tapper! 🚀\n\n"
        "Get ready to fly to the moon with $COSMO!\n\n"
        "Type /play to start your mission and climb the leaderboards!"
    )
    await update.message.reply_text(welcome_message)


async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handler for the /play command.
    Sends a message with an inline keyboard button that launches the Mini App.
    """
    # This creates the button. The WebAppInfo object tells Telegram to open your game.
    keyboard = [
        [InlineKeyboardButton("🚀 Launch Mission! 🚀", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Click the button below to start your mission to the moon!",
        reply_markup=reply_markup
    )


# --- Main Bot Function ---

def main() -> None:
    """
    Initializes and runs the Telegram bot.
    """
    logger.info("Starting bot...")
    
    # Create the Application instance with your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register the command handlers.
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("play", play_command))

    # Start the bot. It will keep running until you stop it (e.g., with Ctrl+C).
    logger.info("Bot started and polling for updates.")
    application.run_polling()


if __name__ == "__main__":
    main()
