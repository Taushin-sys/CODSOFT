"""
demo_cli.py
-----------
Interactive demo for the Movie Recommendation System.
"""

from recommender import recommend

def main():
    print("\n🎬 Welcome to CineMatch — Your Movie Recommender 🎬")
    print("Type the name of a movie you like, and I'll suggest similar ones!")
    print("Type 'exit' to quit.\n")

    while True:
        title = input("You: ").strip()
        if title.lower() in ["exit", "quit"]:
            print("CineMatch: Thanks for exploring movies with me! 👋")
            break
        recommendations = recommend(title)
        print("\nCineMatch: Here are some movies you might enjoy:")
        for i, movie in enumerate(recommendations, start=1):
            print(f"  {i}. {movie}")
        print()

if __name__ == "__main__":
    main()