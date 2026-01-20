import shutil
import os
from datetime import datetime

SOURCE_FOLDER = "source_folder"
BACKUP_ROOT = "backups"


def backup_folder():
    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    if not os.path.exists(BACKUP_ROOT):
        os.mkdir(BACKUP_ROOT)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(BACKUP_ROOT, f"backup_{timestamp}")

    shutil.copytree(SOURCE_FOLDER, backup_path)

    print("Backup created at:", backup_path)


if __name__ == "__main__":
    backup_folder()
