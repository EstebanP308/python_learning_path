# 🧠 Adaptive Math Trainer (Python)

An interactive CLI game that challenges your mental math skills with adaptive difficulty, time limits, and a persistent High Score system.

## 🚀 Features
- **Adaptive Difficulty:** As you level up, numbers get larger and new operations (+, -, *, /, Equations) are unlocked.
- **Time Pressure:** Each level has a specific time limit.
- **Persistence:** Your highest score is saved in a `highscore.txt` file.
- **Modular Logic:** Uses Python's `random`, `time`, and `os` libraries.

## 🛠️ Lessons Learned & Challenges
During the development of this project, I faced several logical challenges that helped me improve my debugging skills:

1. **Indentation & Scope:** Initially, I struggled with placing the game logic outside the `while` loop, which caused the game to run only once. I learned how Python uses indentation to define scope.
2. **Type Matching:** I had errors comparing `input()` (strings) with mathematical results (integers). I solved this by implementing consistent type casting.
3. **Double Input Bug:** At one point, the program asked for the answer twice. I refactored the conditional blocks to ensure only one `input()` call per turn.
4. **Persistent Data:** I learned how to use the `os` library to check for existing files and handle I/O operations for the High Score system.

## 🕹️ How to Play
1. Run the script: `python math_trainer.py`
2. Solve 3 problems in a row to level up.
3. Don't let the timer hit zero or lose all your lives!

