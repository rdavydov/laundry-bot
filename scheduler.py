from apscheduler.schedulers.background import BackgroundScheduler
import shutil
import time
import os


def backup_db():
    current_time = time.strftime("%Y%m%d-%H%M%S")
    backup_file = f"laundry_backup_{current_time}.db.gz"
    shutil.copyfile("laundry.db", backup_file)


# Create a scheduler and schedule the backup job
scheduler = BackgroundScheduler()
scheduler.add_job(backup_db, trigger='interval', days=1)
scheduler.start()
