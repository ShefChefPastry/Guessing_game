# 🐍 Terminal Number Guessing Game

<p align="center">
  <img src="https://api.boot.dev/v1/users/public/02c99808-216a-4b68-b455-bc3140d2303b/thumbnail" >
</p>

A dynamic, interactive command-line application built in Python that challenges players to guess a randomly generated number within a range determined by chosen difficulty tiers.

This project was built to practice Python fundamentals including functions, loops, conditionals, input validation, random number generation, and tracking program state.

---

## 🚀 Key Features

### 🎯 Dynamic Difficulty Levels

Players can choose from three difficulty tiers:

- **Easy:** 1–100
- **Medium:** 1–500
- **Hard:** 1–1000

Each difficulty generates a random secret number within the selected range.

---

### 🔢 Limited Attempts System

Players have a maximum number of guesses per game.

The game tracks:

- Attempts used
- Attempts remaining
- Win/loss conditions

Players receive feedback after each guess:

- Too High
- Too Low
- Correct Guess

---

### 📊 Game Statistics

The game tracks player performance across multiple rounds:

- Total games played
- Attempts per game
- Total attempts
- Average attempts
- Best winning score

---

### 🛡️ Robust Input Handling

Includes validation systems to prevent crashes and incorrect inputs:

- Handles non-integer values
- Prevents guesses outside the allowed range
- Validates difficulty selection

---

### 🔁 Replay System

Players can continue playing multiple games without restarting the program.

---

## 🛠️ How to Run Locally

Ensure you have Python 3 installed.

Clone the repository:

```bash
git clone https://github.com/ShefChefPastry/Guessing_game.git
