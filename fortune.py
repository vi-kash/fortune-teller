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
            "Your joy lights up the world — keep shining.",
            "You’re on a roll! Embrace the positivity.",
            "Good vibes are coming your way, stay cheerful!",
        ],
        "sad": [
            "Tough times don’t last, but tough people do.",
            "Let your tears water the seeds of your future happiness.",
            "It’s okay to feel down — brighter days are coming.",
            f"Stay strong, {name}. You're braver than you believe.",
            "A rainbow is just around the corner after this storm.",
        ],
        "neutral": [
            "Today is a perfect day to try something new.",
            "Keep moving forward. Something great is ahead.",
            "Not every day has to be exciting — steady wins too.",
            f"Hey {name}, sometimes peace is progress.",
            "Balance is beautiful. Embrace the calm.",
        ],
        "stressed": [
            "Take a deep breath. You’ve got this.",
            "Calm minds bring inner strength and self-confidence.",
            "Every breath is a step toward peace.",
            "You are capable of handling whatever comes your way.",
            f"Don’t worry, {name}. Relaxation is power too.",
        ]
    }

    if mood in fortunes:
        print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
    else:
        print("❓ I couldn't read your mood. Try happy/sad/neutral/stressed.")

if __name__ == "__main__":
    main()
