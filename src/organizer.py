# src/organizer.py
import shutil
import time
from pathlib import Path

DOWNLOADS = Path(r"C:\Users\Shristi\Desktop\demo-downloads")


FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Music": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".json", ".ts"],
    "Others": []
}

def create_folders():
    for folder in FILE_TYPES:
        folder_path = DOWNLOADS / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)

def move_file(file_path):
    try:
        ext = file_path.suffix.lower()
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                dest = DOWNLOADS / folder / file_path.name
                shutil.move(str(file_path), str(dest))
                return folder
        # default
        dest = DOWNLOADS / "Others" / file_path.name
        shutil.move(str(file_path), str(dest))
        return "Others"
    except Exception as e:
        print(f"Failed to move {file_path.name}: {e}")
        return None

def organize_once():
    for item in list(DOWNLOADS.iterdir()):
        if item.is_file():
            folder = move_file(item)
            if folder:
                print(f"Moved: {item.name} -> {folder}/")

def auto_watch(interval=10):
    print(f"Watching Downloads: {DOWNLOADS}")
    print("Press Ctrl+C to stop.")
    create_folders()
    while True:
        organize_once()
        time.sleep(interval)

if __name__ == "__main__":
    create_folders()
    organize_once()

