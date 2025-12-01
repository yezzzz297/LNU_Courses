# Text analyser project
# This program can read a text file, counts lines, words, and characters,
# and show results with simple charts.
# Yetnayet Belachew
# 2025

import os
import matplotlib.pyplot as plt
from collections import Counter

# list all txt files in the same folder
def list_text_files():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files:
        print("No text files found.")
    else:
        print("\nAvailable text files:")
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
    return files


# read file and count lines, words, chars and word frequency
def compute_basic_stats(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    char_no_space = 0
    word_counter = Counter()

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)
            char_no_space += len(line.replace(" ", ""))

            # count words 
            for w in words:
                w = w.strip(".,!?;:\"'()[]{}").lower()
                if w:
                    word_counter[w] += 1

    avg_words_per_line = word_count / line_count if line_count else 0
    avg_chars_per_word = char_count / word_count if word_count else 0

    stats = {
        "lines": line_count,
        "words": word_count,
        "chars": char_count,
        "chars_no_space": char_no_space,
        "avg_words_line": avg_words_per_line,
        "avg_chars_word": avg_chars_per_word,
        "word_counter": word_counter
    }
    return stats


# print basic statistics
def show_basic_stats(stats):
    print("\n--- Basic Statistics ---")
    print("Total lines:", stats["lines"])
    print("Total words:", stats["words"])
    print("Characters (with spaces):", stats["chars"])
    print("Characters (no spaces):", stats["chars_no_space"])
    print(f"Average words per line: {stats['avg_words_line']:.2f}")
    print(f"Average chars per word: {stats['avg_chars_word']:.2f}")


# show a simple bar chart for main statistics
def show_basic_chart(stats):
    labels = ["Lines", "Words", "Chars (with space)", "Chars (no space)"]
    values = [
        stats["lines"],
        stats["words"],
        stats["chars"],
        stats["chars_no_space"]
    ]

    plt.bar(labels, values)
    plt.title("Basic Text Statistics")
    plt.ylabel("Count")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()


# analyse word frequency
def word_analysis(stats):
    counter = stats["word_counter"]
    total_unique = len(counter)
    words_once = sum(1 for c in counter.values() if c == 1)
    top10 = counter.most_common(10)

    print("\n--- Word Analysis ---")
    print("Unique words:", total_unique)
    print("Words appearing only once:", words_once)
    print("\nTop 10 most common words:")
    for i, (w, c) in enumerate(top10, 1):
        print(f"{i}. {w:<10} {c} times")

    show_word_chart(top10)

    return {"unique": total_unique, "once": words_once, "top10": top10}


# chart for word analysis
def show_word_chart(top10):
    words = [w for w, _ in top10]
    counts = [c for _, c in top10]

    plt.bar(words, counts)
    plt.title("Top 10 Most Common Words")
    plt.xlabel("Words")
    plt.ylabel("Times")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.show()


# save results to a text file
def export_results(filename, stats, word_stats):
    export_name = f"results_{filename}.txt"
    with open(export_name, "w", encoding="utf-8") as f:
        f.write("TEXT ANALYSIS REPORT\n")
        f.write("=====================\n")
        f.write(f"File analysed: {filename}\n\n")
        f.write("BASIC STATS:\n")
        f.write(f"Lines: {stats['lines']}\n")
        f.write(f"Words: {stats['words']}\n")
        f.write(f"Chars (with spaces): {stats['chars']}\n")
        f.write(f"Chars (no spaces): {stats['chars_no_space']}\n")
        f.write(f"Average words per line: {stats['avg_words_line']:.2f}\n")
        f.write(f"Average chars per word: {stats['avg_chars_word']:.2f}\n\n")
        f.write("WORD ANALYSIS:\n")
        f.write(f"Unique words: {word_stats['unique']}\n")
        f.write(f"Words appearing once: {word_stats['once']}\n\n")
        f.write("Top 10 Most Common Words:\n")
        for i, (w, c) in enumerate(word_stats["top10"], 1):
            f.write(f"{i}. {w:<10} {c} times\n")

    print(f"\nResults saved to '{export_name}' successfully!")

 # main
def main():
    current_file = None
    stats = None
    word_stats = None  # keep variable active between menu choices

    while True:
        print("\n=============================")
        print("       TEXT ANALYSER")
        print("=============================")
        print("1. Load text file")
        print("2. Show basic statistics")
        print("3. Word analysis")
        print("4. Export results")
        print("5. Exit")
        print("=============================")
        choice = input("Enter your choice: ")

        if choice == "1":
            files = list_text_files()
            if files:
                pick = input("\nEnter file number or name: ").strip()
                try:
                    if pick.isdigit():
                        filename = files[int(pick) - 1]
                    else:
                        filename = pick
                    stats = compute_basic_stats(filename)
                    current_file = filename
                    print(f"\n'{filename}' loaded and analysed.")
                except Exception as e:
                    print("Error loading file:", e)

        elif choice == "2":
            if stats:
                show_basic_stats(stats)
                show_basic_chart(stats)
            else:
                print("Please load a file first!")

        elif choice == "3":
            if stats:
                word_stats = word_analysis(stats)
                print("\nWord analysis completed and saved.")
            else:
                print("Please load a file first!")

        elif choice == "4":
            if stats is not None:
                if word_stats is None:
                    print("\nRunning word analysis before export...")
                    word_stats = word_analysis(stats)
                export_results(current_file, stats, word_stats)
            else:
                print("Please load a file first!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
