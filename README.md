# 🎮 Shuffle and Recall - Memory Card Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A classic memory card matching game built with Python**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [How to Play](#-how-to-play) • [Documentation](#-documentation)

</div>

---

## 📖 About

**Shuffle and Recall** is a console-based memory card game that tests your memory and concentration skills. Match all 8 pairs of cards by remembering their positions to win the game!

The game features:
- 🃏 16 cards (8 pairs) arranged in a 4×4 grid
- 🎲 Fisher-Yates shuffle algorithm for fair randomization
- 📊 Score tracking and performance statistics
- ✨ Beautiful ASCII art interface
- 🎯 Input validation and error handling

---

## ✨ Features

### 🎨 **Beautiful UI**
- Clean ASCII art interface with emoji support
- Color-coded card states (hidden, revealed, matched)
- Real-time score and attempts counter

### 🧠 **Smart Game Logic**
- Fisher-Yates shuffle algorithm ensures truly random card distribution
- Robust input validation prevents invalid moves
- Automatic game state tracking

### 📈 **Performance Analytics**
- Total score calculation (10 points per match)
- Attempts counter
- Accuracy percentage at game end

### 🏗️ **Clean Code Architecture**
- Object-Oriented Programming (OOP) design
- Modular functions for maintainability
- Well-documented code with comments

---

## 🎬 Demo

```
═══════════════════════════════════════
        🎮 SHUFFLE AND RECALL 🎮        
═══════════════════════════════════════
Score: 30  |  Attempts: 5
---------------------------------------
[✓A] [✓A] [ ? ] [ ? ] 
[ E ] [ ? ] [ ? ] [✓B] 
[ ? ] [ ? ] [ G ] [✓B] 
[ ? ] [ ? ] [ ? ] [ ? ] 
═══════════════════════════════════════
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/litha-octa/Game-Resuffle-and-Recall.git
cd shuffle-and-recall
```

2. **Run the game**
```bash
py resuffle_and_recall.py
```

That's it! No external dependencies required. 🎉

---

## 🎮 How to Play

1. **Start the Game**
   - Run the program and the board will be displayed with all cards face-down ([ ? ])

2. **Select Cards**
   - Choose two cards by entering their position (1-16)
   - Cards will be revealed temporarily

3. **Match Cards**
   - If cards match: ✅ They stay revealed ([✓X]) and you earn 10 points
   - If cards don't match: ❌ They flip back after 2 seconds

4. **Win the Game**
   - Match all 8 pairs to complete the game
   - View your final statistics: Score, Attempts, and Accuracy

### 💡 Tips
- Memorize card positions as they're revealed
- Start from corners and edges for better organization
- Aim for the highest accuracy by minimizing attempts!

---

## 📂 Project Structure

```
shuffle-and-recall/
│
├── resuffle_and_recall.py                 # Main game file
├── README.md              # This file
```

---

## 🛠️ Technical Details

### Algorithm: Fisher-Yates Shuffle
The game uses the **Fisher-Yates shuffle algorithm** to ensure truly random card distribution:

```python
for i in range(15, 0, -1):
    j = random.randint(0, i)
    self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

### Game State Management
The game tracks three arrays to manage card states:
- `cards[]` - Stores card values (A-H)
- `revealed[]` - Tracks which cards are currently visible
- `matched[]` - Tracks which cards have been successfully matched

---

## 📊 Code Statistics

| Metric | Value |
|--------|-------|
| Lines of Code | ~120 |
| Functions/Methods | 7 |
| Classes | 1 |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

---

## 🎓 Learning Outcomes

This project demonstrates understanding of:

✅ **Data Structures**
- Arrays/Lists for card storage
- Boolean arrays for state tracking

✅ **Algorithms**
- Fisher-Yates shuffle
- Game loop logic
- Pattern matching

✅ **Programming Concepts**
- Object-Oriented Programming (OOP)
- Error handling with try-except
- Input validation
- User experience design

✅ **Control Structures**
- While loops for game flow
- For loops for iterations
- If-else for conditional logic

---

### Key Classes and Methods

#### `ShuffleAndRecall` Class

| Method | Description |
|--------|-------------|
| `__init__()` | Initialize game state and variables |
| `initialize_game()` | Shuffle cards using Fisher-Yates algorithm |
| `display_board()` | Render the 4×4 game board |
| `select_card()` | Handle card selection with validation |
| `check_match()` | Compare two selected cards |
| `check_game_over()` | Verify if all pairs are matched |
| `play()` | Main game loop |

---

## 🎯 Future Enhancements

Potential improvements for future versions:

- [ ] Add difficulty levels (Easy: 3×4, Medium: 4×4, Hard: 4×6)
- [ ] Implement timer and time-based scoring
- [ ] Add high score leaderboard with persistent storage
- [ ] Create GUI version using Tkinter or Pygame
- [ ] Add sound effects for matches and mismatches
- [ ] Implement replay option without restarting
- [ ] Add multiplayer mode (2-player turn-based)
- [ ] Create themed card sets (animals, flags, etc.)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👥 Authors
- Litha Octa Delistia

**Course:** Dasar Pemrograman  
**Institution:** Universitas Siber Asia  

---

## 🙏 Acknowledgments

- Inspired by classic memory card games
- Fisher-Yates shuffle algorithm by Ronald Fisher and Frank Yates
- ASCII art for beautiful console interface
- Python community for excellent documentation

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python

[Back to Top](#-shuffle-and-recall---memory-card-game)

</div>
