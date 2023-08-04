# laundry-bot

Laundry room reservation bot for Telegram

Install the required packages using `pip install -r requirements.txt`.

Run the scheduler.py script in the background to handle daily backups using `python scheduler.py &`.

Start the Telegram bot and web application by running the start_bot.py script using `python start_bot.py`.

The bot should now be up and running, and users can interact with it through Telegram. The web application should be accessible at <http://localhost:5000/> in your browser, allowing users to view and edit reservation data.

# Design Document

Steps you need to take to create such a bot. Keep in mind that this is a high-level overview, and you'll need to implement the details accordingly.

1. **Setting up the Telegram Bot:**
   - Create a new Telegram bot using the BotFather on Telegram. Obtain the bot token.
   - Create a new group or channel where the bot will operate and get the chat ID of the group/channel.

2. **Development Environment Setup:**
   - Set up a development environment with a programming language that supports Telegram bot development (Python, Node.js, etc.).
   - Install necessary libraries for working with Telegram APIs, SQLite, and web framework (e.g., Flask).

3. **User Registration and Data Storage:**
   - On the first launch, ask users to enter their room number and phone and store this information in the SQLite database along with their chat ID.
   - Maintain a separate table for reservations (date, time, user_id, status) to store the reservation data.

4. **Reservation System:**
   - Create a date/time selection control in the Telegram bot to allow users to reserve a time slot, not more than 1 hour.
   - Implement checks to ensure a user can't reserve overlapping time slots.
   - Send notifications to users before the reservation starts and ends based on their preferences.

5. **Web UI:**
   - Develop a web UI using the chosen web framework to show reservation data.
   - Provide a login system for users and admin.
   - Users should be able to view and manage their reservations.
   - Admin should be able to view all data and make edits for any user.

6. **Backup System:**
   - Set up a scheduled task or cron job to automatically create backups of the SQLite database in gzipped format regularly. The frequency should be configurable.

7. **Telegram Bot and Web UI Integration:**
   - Use the Telegram Bot API to enable users to interact with the bot through the web UI if Telegram is down.

8. **Deploy and Hosting:**
   - Deploy the Telegram bot and web application on a server with necessary configurations.
   - Secure the web application with SSL to ensure data privacy.

9. **Testing and Improvements:**
   - Thoroughly test the bot and web UI to identify and fix any bugs or issues.
   - Consider adding additional features, user experience improvements, and security enhancements as needed.

Please note that creating this entire system is a complex task that requires a good understanding of programming, web development, and database management. You may also need to explore various libraries and tools for implementing specific features. Additionally, remember to follow Telegram's Bot API terms of service and privacy guidelines while building and deploying the bot.
