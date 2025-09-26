import os, sys

from django.core.management import execute_from_command_line
from dotenv import load_dotenv


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    load_dotenv("/Users/wnowogorski/PycharmProjects/ChatAGH_UI/.env")
    main()
