[README.md](https://github.com/user-attachments/files/29203933/README.md)
# 🎸 Band Tycoon Manager

> A text-based band management simulation game built with Python — grow your band from a local pub gig to a sold-out arena tour!

---

## 📌 About the Project

**Band Tycoon Manager** is a terminal-based strategy/simulation game where you take on the role of a music band manager.  
Starting with $1000 and 50 fans, your goal is to build a legendary band by making smart decisions:  
record singles, organize concerts, run social media campaigns — and survive random events along the way!

This project was developed for the **CENG113M Best Project Competition** (Spring 2025-2026) at İYTE.

---

## 🎮 Gameplay Features

- 🎵 **Studio Sessions** — Spend $200 to record a single and boost your popularity
- 🎤 **Concerts** — Choose between a low-risk Local Pub Gig or a high-reward City Arena show (requires 40+ popularity)
- 📱 **Social Media Campaigns** — Spend $100 on Instagram & TikTok ads to grow your fan base
- ⚡ **Random Events** — Unexpected events can hit at any time (viral TikTok? sick guitarist? forgotten $100 bill?)
- 💾 **Save & Load System** — Your progress is saved to a file and can be loaded anytime
- 📊 **Live Status Panel** — Track your budget, popularity (0–100), fan count and albums released every turn

---

## 🖥️ Screenshots

```
===================================
  Welcome to BAND TYCOON MANAGER
===================================
1. Start a New Journey (New game)
2. Continue from Last Save (Load Game)
3. Exit Game
===================================

=========================================
 BAND: The Lost Chords | Day: 5
=========================================
 -> Budget: $1450
 -> Popularity: 32/100
 -> Fan Base: 210 fans
 -> Albums Released: 2
=========================================
```

---

## 🚀 How to Run

### Requirements
- Python 3.x (no external libraries needed — only `random` and `os`)

### Run the Game

```bash
# Clone the repository
git clone https://github.com/sudegur/band-tycoon-manager.git

# Navigate into the folder
cd band-tycoon-manager

# Start the game
python main.py
```

---

## 📖 How to Play

```
1. Launch the game and select "Start a New Journey"
2. Enter your band's name
3. Each day, choose one action:
     [1] Enter the Studio    → costs $200, gains popularity
     [2] Organize a Concert  → earns money and fans
     [3] Run a Campaign      → costs $100, grows fan base
     [4] Save Progress       → writes your game to save_game.txt
     [5] Quit to Main Menu
4. After each successful action, a random event may occur!
5. Aim to reach maximum popularity (100/100) and build a massive fan base
```

> 💡 **Tip:** Unlock the City Arena concert (requires 40+ popularity) for massive income and fan growth!

---

## 💾 Save System

The game automatically saves your progress to a file called `save_game.txt` in the same directory.  
Select **"Continue from Last Save"** from the main menu to resume where you left off.

---

## 🗂️ Project Structure

```
band-tycoon-manager/
│
├── main.py          # Main game logic — all functions and game loop
└── save_game.txt    # Auto-generated save file (created after first save)
```

---

## 🛠️ Technical Details

| Feature | Implementation |
|---|---|
| Game state | Python dictionary (`game_state`) |
| Random events | `random.random()` with 25% trigger chance |
| Save / Load | File I/O with `open()`, `write()`, `read()` |
| Input validation | `while` loops for empty/invalid input |
| Popularity cap | Clamped to 0–100 range |

---

## 👤 Developer

**[Sude Gür]**  
İzmir Institute of Technology — CENG113M Spring 2025-2026
