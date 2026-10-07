# Exercises & Problems — Full Problem Statements

Every exercise and project so far, written out in full so you can **re-attempt any of them from
scratch** for revision. Each has: the problem, clear requirements, example output, and **concept
tags**. No solutions here — see the actual `.py` files for those, and `README.md` for the theory.

> **Best revision method:** pick one, open a blank file, and solve it without looking at your old
> code. Re-solving from memory (not re-reading) is what actually cements a skill.

**Tag legend:** `variables` `strings` `f-strings` `math` `type-conversion` `conditionals`
`loops` `while` `lists` `dicts` `functions` `return` `error-handling` `input-validation`
`slicing` `string-methods` `sets` `dict-counter` `comprehensions` `tuples` `unpacking`
`random` `enumerate` `aliasing` `hash-map` `Big-O` `game-logic` `AI/agent` `data`

---

# Part 1 — Lesson Exercises

Short drills tied to each lesson (originally done in `main.py` / `toolkit.py`).

## Exercise 1 — Variables & `print()`
Tags: `variables` `strings`

Create variables describing yourself and print them:
1. `my_name` with your name (a string).
2. `my_age` with your age (a number).
3. `favorite_language` set to `"Python"`.
4. Print each — at least once using the multi-argument form, e.g. `print("My name is:", my_name)`.

## Exercise 2 — Strings & Numbers
Tags: `math` `f-strings` `type-conversion`

1. Create two number variables, e.g. `a = 17`, `b = 5`.
2. Print their sum, difference, product, and remainder (`%`) — each with a label, using **f-strings**,
   e.g. `print(f"{a} + {b} = {a + b}")`.
3. Create `first_name` and `last_name`, combine them into `full_name`, and print a greeting like
   `Hello, Raj Kumar!` using an f-string.
4. **Bonus:** given `year_str = "2026"` (text), print what year it'll be 5 years later as a number
   (you'll need `int(...)`).

## Exercise 3 — Conditionals
Tags: `conditionals`

1. Create `number = 17` (any number). Use `if`/`else` to print whether it's **even or odd**
   (hint: `number % 2 == 0`).
2. Create `score = 82`. Using `if`/`elif`/`else`, print a grade: 90+ → "A", 80–89 → "B",
   70–79 → "C", below 70 → "Fail". (Watch the boundaries — `>=`.)
3. **Bonus:** create `age` and `has_ticket = True`. Print `"Welcome!"` only if age is 18 or older
   **and** they have a ticket; otherwise `"Entry denied"`.

## Exercise 4 — Loops
Tags: `loops` `while`

1. Use a `for` loop to print the numbers **1 through 10**.
2. Use a loop to print only the **even** numbers from 1 to 10.
3. Use a `while` loop to count down from 5, printing `5, 4, 3, 2, 1`, then print `"Liftoff!"` once.
4. **Bonus:** loop through the string `"Python"` and print each character on its own line.

## Exercise 5 — Lists
Tags: `lists` `loops`

Given `scores = [85, 92, 78, 90, 65]`:
1. Print how many scores there are with `len()`.
2. Print the **first** and **last** score (use index `0` and `-1`).
3. Add `88` to the end with `.append()`, then print the whole list.
4. Loop over the list and print each score with a label, e.g. `Score: 85`.
5. **Bonus:** loop and print whether each score is a pass or fail (pass = 70+).

## Exercise 6 — Functions
Tags: `functions` `return`

1. `square(n)` — **returns** `n * n`. Test with a couple of numbers.
2. `is_even(n)` — **returns** `True`/`False`. Test `is_even(4)` and `is_even(7)`.
3. `greet(name, language)` — returns a greeting in the requested language: `"spanish"` → `"Hola, {name}!"`,
   `"french"` → `"Bonjour, {name}!"`, else `"Hello, {name}!"`. Handle an invalid language too.
4. **Bonus:** `average(numbers)` — takes a **list** and returns the average (use `sum()` and `len()`).
   Test with `average([85, 92, 78, 90, 65])` → `82.0`.

## Exercise 7 — Dictionaries
Tags: `dicts` `loops`

1. Create a `book` dict with keys `"title"`, `"author"`, `"year"`. Print a sentence using its values.
2. Add a `"genre"` key; change `"year"`; print the whole dict.
3. Use `.get()` to safely look up a missing key (e.g. `"price"`) with a default, showing it doesn't crash.
4. Loop over `book` with `.items()`, printing each `key: value`.
5. **Bonus:** make a **list of 3 student dicts** (`"name"`, `"grade"`); loop and print each; then compute
   and print the **average grade** (reuse `average` from Ex. 6).

## Exercise 8 — Error Handling
Tags: `error-handling`

1. Call `average([])` inside a `try`/`except` and print a friendly message instead of the
   `ZeroDivisionError` crash.
2. Try to access a missing list index (e.g. `nums[99]`) and catch the `IndexError`.
3. Do `int("not a number")` and catch the `ValueError`.
4. **Bonus:** `safe_divide(a, b)` — returns `a / b`, but if `b == 0`, catches `ZeroDivisionError`
   and returns `"undefined"`. Test `safe_divide(10, 2)` and `safe_divide(10, 0)`.

## Exercise 9 — Slicing & String Methods
Tags: `slicing` `string-methods`

1. Given `s = "programming"`, use slicing to print: first 4 chars; last 3 chars; everything except
   the first and last char (`s[1:-1]`); the string reversed.
2. Given `word = "racecar"`, print `True`/`False` for whether it's a **palindrome** (compare it to its reverse).
3. Given `sentence = "  Learning Python is fun  "`: strip & print; print uppercase; split into a word
   list & print it; print the number of words.
4. **Bonus:** given `"hello world foo"`, reverse the **word order** → `"foo world hello"`
   (`.split()` → `[::-1]` → `.join()`).

## Exercise 10 — Sets & the Dict-Counter Pattern
Tags: `sets` `dict-counter`

1. Given `nums = [4, 2, 7, 2, 4, 9, 4]`: print it with duplicates removed (`set`), and print how many
   **unique** numbers there are.
2. `has_duplicates(items)` — returns `True` if any value repeats, else `False`
   (hint: compare `len(items)` to `len(set(items))`).
3. Given `text = "mississippi"`, build a dict counting each **letter** and print it
   (use the `counts.get(letter, 0) + 1` one-liner).
4. **Bonus:** from #3's counts, find and print the **most frequent** letter.

---

# Part 2 — Projects & Games

Larger builds. Each is written as a spec you can implement fresh.

## `quiz.py` — Trivia Quiz Game
Tags: `dicts` `loops` `functions` `conditionals` `f-strings`

Build a quiz that asks several questions, scores the answers, and grades the result.
1. Store questions as a **list of dicts**, each `{"question": ..., "answer": ...}` (keep answers lowercase).
2. `run_quiz(questions)` — start `score = 0`, loop the questions, show each and read the user's answer;
   if correct, say so and `+1`, else reveal the right answer. **Return** the final score.
3. Compute the percentage: `score / len(questions) * 100`.
4. `get_grade(percentage)` — returns a letter: 90+ → "A", 75–89 → "B", 50–74 → "C", below 50 → "F".
5. Print a final summary: score out of total, percentage (1 decimal), grade, and a message per grade.

Example:
```
You scored 3 out of 4 (75.0%) — Grade: B
Good effort!
```

## `todo.py` — To-Do List (v1, string tasks)
Tags: `lists` `functions` `while` `input-validation`

A menu-driven to-do list where each task is a **string**.
1. Keep tasks in a list. Print a welcome once.
2. `add_task(task)` — append and confirm.
3. `view_tasks()` — if empty, say "No tasks yet"; else print each task **numbered from 1**.
4. A `while True` menu loop: 1 = add (ask for text), 2 = view, 3 = quit (`break`); anything else → "invalid".

## `todo2.py` — To-Do List (v2, list of dicts + status)
Tags: `lists` `dicts` `functions` `error-handling` `input-validation`

Upgrade so each task is a **dict** `{"task": ..., "status": ...}`.
1. Operations: add, view (numbered, showing status), remove (by number), update-status (by number).
2. The user types **1-based** numbers; convert to 0-based indices internally.
3. **Bounds-check** every number (reject 0, negatives, too-large — a menu number like 0 must NOT delete
   the last item), and wrap `int(input(...))` in `try`/`except ValueError`.
4. Confirm each action; handle the empty-list case in view.

## `guess.py` — Number Guessing Game
Tags: `random` `while` `conditionals` `error-handling`

1. The computer picks a secret number 1–100 with `random.randint`.
2. Loop: read a guess; say "too high" / "too low" / correct.
3. Count the number of attempts and report it on a win.
4. Handle non-numeric input with `try`/`except` (don't count it as an attempt — `continue`).

## `rps.py` — Rock Paper Scissors (best of 5)
Tags: `random` `dicts` `conditionals` `input-validation` `game-logic`

1. Play against a random bot; first to **3 wins** takes the match (max 5 rounds).
2. Map 0/1/2 → Rock/Paper/Scissors (a dict is handy). Read the player's 0/1/2 choice; bot picks randomly.
3. Decide each round correctly (all 9 combinations); track both scores; announce winner/tie each round.
4. **Validate** input: non-numbers and out-of-range choices → message + retry, without burning a round.

## `password_check.py` — Password Strength Analyzer
Tags: `comprehensions` `string-methods` `conditionals`

1. Read a password.
2. Using **list comprehensions**, collect its digits (`.isdigit()`), uppercase (`.isupper()`), lowercase
   (`.islower()`), and special characters (`not c.isalnum()`).
3. Print how many of each it has.
4. Give a verdict: "Strong" if length ≥ 8 **and** it has at least one digit, one uppercase, one lowercase;
   otherwise say what's missing.

Example:
```
Enter a password: hello123
Length: 8 | digits: 3 | uppercase: 0 | lowercase: 5
Weak — add an uppercase letter.
```

## `movies.py` — Movie Data Analyzer
Tags: `comprehensions` `dicts` `dict-counter` `data`

Given a **list of movie dicts** (`title`, `year`, `rating`, `genre`), use **comprehensions** to:
1. Build a list of all titles.
2. Titles rated `>= 8.7`.
3. Titles from year `>= 2000`.
4. Titles in the `"sci-fi"` genre.
5. The **average rating** (build a ratings list, then `sum/len`, format to 1 decimal).
6. **Bonus:** count movies **per genre** (dict-counter or `Counter`); find the highest-rated movie.

## `stats.py` — Stats Calculator
Tags: `tuples` `unpacking` `functions` `return` `comprehensions`

1. `min_max_avg(nums)` — returns **three** values as a tuple `(min, max, average)`. Call it and
   **unpack** into `low, high, avg`; print with the average to 1 decimal.
2. `split_even_odd(nums)` — returns a tuple of **two lists** `(evens, odds)`, built with comprehensions.
   Unpack and print both.
3. Given a list of `(name, score)` **tuples**, loop by **unpacking** (`for name, score in ...`) and print
   `"Raj scored 85"`.
4. **Bonus:** find and print the person with the highest score.

## `dice_stats.py` — Dice Roll Simulator
Tags: `random` `dict-counter` `loops` `data`

1. Roll a 6-sided die **100 times** (`random.randint(1, 6)`).
2. **Count** how many times each face appears (dict-counter pattern).
3. Print a **histogram**: for each face **1 → 6 in order**, print the face, a bar of `*` as long as its
   count, and the count. Loop `range(1, 7)` and look each face up (don't loop the dict — it won't be ordered).

Example:
```
1: ***************** (17)
2: ************* (13)
...
```
4. **Bonus:** print the most/least frequent face; try 10,000 rolls and watch counts even out.

## `hangman.py` — Hangman
Tags: `strings` `lists` `loops` `conditionals` `input-validation` `game-logic`

1. Pick a random word from a list.
2. Track lives (e.g. 6) and guessed letters (a list). Each round, show the word with `_` for
   unguessed letters and the real letter where guessed — **must reveal ALL positions of a repeated letter**.
3. Read a single-letter guess; if already guessed, say so; if in the word, reveal it; else lose a life.
4. **Win** when the whole word is revealed; **lose** at 0 lives (reveal the word).
5. Validate input: reject empty / multi-character / non-letter guesses.

## `wordle.py` — Wordle (simplified)
Tags: `sets` `strings` `slicing` `loops` `game-logic`

1. Pick a random 5-letter word; give the player **6 guesses**.
2. Validate each guess is exactly 5 letters (else re-ask without using a turn).
3. Feedback **per letter** (build a `set` of the secret's letters): right letter & right spot → one marker
   (e.g. `*`), right letter wrong spot → another (`&`), not in the word → the letter itself.
4. Win on an exact match; on loss reveal the word.
5. **Boss level:** handle **repeated letters** correctly (only as many highlights as the secret actually
   has) — needs the dict-counter "available count" idea.

## `word_frequency_counter.py` — Word Frequency Counter
Tags: `dict-counter` `string-methods` `comprehensions` `tuples` `sets`

Given a paragraph of text:
1. **Clean** it: lowercase, and strip punctuation from each word (comprehension with `.strip(".,!?;:()")`).
2. Print the total word count and the **unique** word count (a `set`).
3. Count word frequencies (`Counter`).
4. Print the **top 5** most common words (`most_common(5)`), looping with **tuple unpacking**
   (`for word, count in ...`).

## `mastermind.py` / `mastermind2.py` — Mastermind 🌟 (hardest so far)
Tags: `lists` `dict-counter` `aliasing` `loops` `game-logic`

1. The computer hides a **4-digit code** (digits may repeat).
2. The player gets up to 6 guesses. For each 4-digit guess, report two counts:
   - **black pegs** = right digit **and** right position;
   - **white pegs** = right digit, **wrong** position.
3. The counting must be correct **even with repeated digits** — a digit already matched (or already
   counted) must not be counted again. (Two-pass approach: count exact matches first, then match the
   leftovers, "consuming" each secret digit as you use it.)
4. Win at 4 black pegs; otherwise lose after 6 guesses.
5. Validate input (4 digits; numeric).

> **Extension (hints only, not built): a SOLVER.** Write code that cracks any secret by
> **constraint elimination** — start with all 4-digit candidates; after each guess+feedback, keep only
> the candidates that would produce that exact feedback; repeat until one remains. A real intro to AI search.
> Tags: `AI/agent` `sets` `comprehensions`

## `monkey_type.py` — Typing Speed Test
Tags: `random` `string-methods` `math` `functions` `comprehensions`

1. Show a sentence (random words are fine).
2. Time how long the user takes to retype it (`time.time()` before and after the `input`).
3. Compute **WPM** = words typed ÷ elapsed **minutes** (careful with the seconds→minutes conversion;
   keep the exact float for the rate, separate from any "M min S sec" display).
4. Compute **accuracy**: compare typed vs. original **word by word**, position by position, counting
   matches (loop over the **shorter** length with `min(...)` to avoid IndexError). Report as a %.
5. Print elapsed time, WPM, and accuracy (formatted to 1 decimal).

## `tictactoe.py` — Tic-Tac-Toe vs AI 🌟
Tags: `lists` `functions` `conditionals` `input-validation` `aliasing` `game-logic` `AI/agent`

1. 3×3 board as a **flat list of 9**; positions 0–8. Print it nicely; show the index in empty cells so the
   player knows where to aim (do this on a **copy** so the real board keeps its empty markers).
2. Human is `x`, bot is `o`, alternating turns.
3. `check_winner(board)` — check all **8 winning lines** (3 rows, 3 cols, 2 diagonals); **return** a code
   for user-win / bot-win / draw / continue (keep it silent — no printing — so it can be reused for planning).
4. Validate the human's move: numeric, in range 0–8, and the cell must be empty (no overwriting).
5. **Check for a winner after every move**, and stop immediately (`break`) — don't let the loser play on.
6. **Bot v1:** pick a **random** empty cell.
7. **Bot v2 (rule-based AI):** for each empty cell, *simulate* placing a mark, evaluate with
   `check_winner`, then undo — priority: **win if you can → block the opponent → else random**
   (optionally: prefer center, then corners).

---

# Part 3 — LeetCode

## #1 Two Sum — ✅ Solved
Tags: `hash-map` `dicts` `Big-O`

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers
that add up to `target`. Exactly one solution exists; you may not use the same element twice.
- Example: `nums = [2,7,11,15], target = 9` → `[0, 1]` (because `2 + 7 = 9`).
- **Brute force:** check every pair with nested loops → O(n²).
- **Optimal (follow-up, "better than O(n²)"):** one pass with a **hash map** — for each number, check if
  its complement (`target - num`) is already seen; store `value → index` as you go → O(n).

## #2 Add Two Numbers — ⏳ Shelved (prerequisites: classes + linked lists)
Tags: `linked-lists` `classes` (prereqs) · `math`

Two non-negative integers are given as **linked lists**, with digits in **reverse order**, one digit per
node. Add them and return the sum as a linked list.
- Example: `l1 = [2,4,3]` (= 342), `l2 = [5,6,4]` (= 465) → `[7,0,8]` (= 807).
- The **addition** logic (add digit by digit, carry the overflow) is within reach. The blocker is the
  **linked list** data structure (nodes with `.val` and `.next`), which is built from **classes** —
  unlocks after Lesson 13.

---

# Ideas Not Yet Built (for later)

- **Battleship** — computer hides ships on a 2D grid; you fire shots and get hit/miss/sunk; deduce and
  sink them all. Tags: `2D-thinking` `sets` `game-logic`
- **Tic-Tac-Toe minimax** — an *unbeatable* bot that looks ahead at all future moves (needs **recursion**).
  Tags: `AI/agent` `recursion`
- **Connect Four / Minesweeper / Maze solver** — grids, directional win-scans, and (for the maze)
  pathfinding (BFS/DFS). Tags: `2D-thinking` `game-logic` `recursion`
