This repository contains **10 beginner–intermediate Python programming exercises**.  
Each task focuses on a specific concept (variables, loops, functions, file I/O, etc.) and can be run individually.

---

## 📋 Task List

### 1. Temperature Converter
- **Concepts:** variables, input/output, conditionals  
- Ask the user for a temperature and its unit (`C`, `F`, or `K`).  
- Convert it into the other two units and display results.  
- Show an error if the unit is invalid.  

---

### 2. Simple Tip Calculator
- **Concepts:** arithmetic, formatted strings  
- Prompt for a bill amount and a tip percentage.  
- Compute the tip and total, rounding to 2 decimals.  
- Repeat until the user types `quit`.  

---

### 3. Shopping-List Tracker
- **Concepts:** lists, loops  
- Start with an empty list.  
- User can:
  - Add an item  
  - Remove `<item>`  
  - Type `view` to print the list  
  - Type `done` to exit  
- Prevent duplicates and handle invalid removals gracefully.  

---

### 4. Word Frequency Counter
- **Concepts:** dictionaries, string methods, functions  
- Define a function `word_counts(text)` that counts word frequencies (ignores punctuation and case).  
- Input a paragraph and print the 5 most common words with their counts.  

---

### 5. Caesar Cipher Encoder/Decoder
- **Concepts:** modular arithmetic, functions  
- Implement `encode(msg, shift)` and `decode(msg, shift)`.  
- Works only on `A–Z` letters (case-insensitive); leaves other characters unchanged.  
- User chooses mode and shift (`-25 … 25`).  

---

### 6. Student Gradebook Analyzer
- **Concepts:** nested loops, dicts with lists  
- Accept multiple students with grades (e.g., `Ali 87 73 92`).  
- Store as `{name: [grades]}`.  
- Print:
  - Class average  
  - Each student’s average  
  - Names of students above the class average  

---

### 7. Mini Hangman (Text)
- **Concepts:** loops, lists, conditionals  
- Pick a random word from a list.  
- Show underscores for unknown letters.  
- Track guessed letters and allow up to 6 wrong guesses.  
- Update display after each guess and declare win/lose.  

---

### 8. Tic-Tac-Toe Move Validator
- **Concepts:** 2D lists, functions  
- Represent a `3 × 3` board as a list of lists.  
- Alternate between players taking row/column inputs.  
- Validate moves (in-bounds and empty space).  
- Detect wins or draws with helper functions.  

---

### 9. Basic CSV Stats (No Pandas)
- **Concepts:** file I/O, string splitting, dictionaries  
- Read a CSV file named `expenses.csv` in the form:  


# Task 10 – Text-Based Maze Navigator

## 📝 Description
This task is a **text-based maze game** where the player navigates through rooms modeled as a dictionary.  
The objective is to reach the `"treasure room"` starting from the `"entrance"` by typing commands.

## 🎯 Concepts Practiced
- Nested dictionaries  
- Loops (`while`)  
- Functions for handling commands  
- Basic text-based game design  

