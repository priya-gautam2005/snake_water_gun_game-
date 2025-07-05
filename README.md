# 🎮 Snake-Water-Gun Game in Python 🐍💧🔫

A fun and interactive terminal-based game built using Python, inspired by the classic "Rock-Paper-Scissors" game — but with a twist!  
Challenge the computer using your wit and see who wins — the snake, the water, or the gun! 😄

---

## 📌 Table of Contents
- [About the Game](#about-the-game)
- [Game Rules](#game-rules)
- [Demo Gameplay](#demo-gameplay)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Code Explanation](#code-explanation)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)

---

## 🧠 About the Game

This is a terminal-based **Python mini-game** where you play **Snake-Water-Gun** against the computer.  
The computer picks randomly, and your goal is to outsmart it by choosing the winning option.

It's a great beginner-friendly project to practice:
- `if-else` conditions
- `random` module
- Dictionaries
- User input and output

---

## 📜 Game Rules

| Your Choice | Computer's Choice | Outcome       |
|-------------|-------------------|---------------|
| Snake 🐍     | Water 💧           | ✅ You Win     |
| Snake 🐍     | Gun 🔫             | ❌ You Lose    |
| Water 💧     | Gun 🔫             | ✅ You Win     |
| Water 💧     | Snake 🐍           | ❌ You Lose    |
| Gun 🔫       | Snake 🐍           | ✅ You Win     |
| Gun 🔫       | Water 💧           | ❌ You Lose    |
| Same         | Same              | ⚖️ Draw        |

---

## 🕹️ Demo Gameplay

```bash
Enter your choice in s, g, w where s = snake, g = gun, w = water: g
You chose g and computer chose s
🎉 You Win!

✅ Concepts used:

random.choice() to select random computer move

Dictionary mapping for easy comparison

Clean if-else logic for win/lose/draw

🗂️ Project Structure
snake-water-gun-game/
│
├── game.py          # Main Python script
├── README.md        # Project documentation

🧰 Technologies Used
Language: Python 3

Concepts: Random module, Conditional logic, Dictionaries, Input/Output

