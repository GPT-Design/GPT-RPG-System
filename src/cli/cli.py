import sys

def main():
    print("🎲 Welcome to GPT-RPG CLI!")
    print("Type 'help' for a list of commands.")
    
    while True:
        command = input("> ").strip().lower()
        
        if command in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif command == "help":
            print("Available commands: help, start, exit")
        elif command == "start":
            print("Starting a new game...")
            # Placeholder for game initialization
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
