import os

TOKEN = os.environ.get("MUNEEB706_TOKEN", "")

if __name__ == "__main__":
    print("Hello World", True if TOKEN else False)