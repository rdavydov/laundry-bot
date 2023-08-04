# Contents of start_bot.py (Script to start the Telegram bot and web application)

from bot.bot import updater
from web_ui.app import app

if __name__ == "__main__":
    # Start the Telegram bot
    updater.start_polling()

    # Start the Flask web application
    app.run(debug=True)
