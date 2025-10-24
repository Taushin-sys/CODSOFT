# demo_cli.py
from studentbot.bot_core import StudentBot

def main():
    bot = StudentBot()
    print("Student Helper Bot — type 'exit' or 'quit' to end")
    print("Tip: Say 'my name is <yourname>' to let the bot remember your name for this session.")
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() in ('exit', 'quit'):
            print("Bot: Take care! Good luck with your studies.")
            break
        if user.lower() in ('session', 'status'):
            print("Bot (session):", bot.get_session_summary())
            continue
        response = bot.respond(user)
        print("Bot:", response)

if __name__ == "__main__":
    main()