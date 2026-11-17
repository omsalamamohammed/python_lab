from config import APP_NAME, VERSION
from utils import greet, add

def main():
    print(greet(APP_NAME))
    print(f"Version: {VERSION}")
    print(add(2, 3))

if __name__ == "__main__":
    main()
