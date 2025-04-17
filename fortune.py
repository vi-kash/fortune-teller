def main():
    name = "Vikash Kumar"
    admission_no = "21JE1044"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("🌧️ Your fortune: Tough times don’t last, but tough people do. Stay strong. 🌈")
    elif mood == "neutral":
        print("🌤️ Your fortune: Today is a perfect day to try something new. Go for it! 💡")
    else:
        print("❓ I couldn't read your mood. Try happy/sad/neutral.")

if __name__ == "__main__":
    main()
