import random

def main():
    name = "Vikash Kumar"
    admission_no = "21JE1044"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "Happiness is contagious. Spread it around!",
        ],
        "sad": [
            "Tough times don’t last, but tough people do.",
            "Let your tears water the seeds of your future happiness.",
        ],
        "neutral": [
            "Today is a perfect day to try something new.",
            "Keep moving forward. Something great is ahead.",
        ],
        "stressed": [
            "Take a deep breath. You’ve got this.",
            "Calm minds bring inner strength and self-confidence.",
        ]
    }

    if mood in fortunes:
        print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
    else:
        print("❓ I couldn't read your mood. Try happy/sad/neutral/stressed.")

if __name__ == "__main__":
    main()
