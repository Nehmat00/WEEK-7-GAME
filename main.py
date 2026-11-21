import random
WORDS = ["python", "castle", "window", "forest", "bridge", "guitar", "dinosaur", "umbrella"]
Reveal_Answers = False

def clean(s):
    return s.strip().lower()

def redact(answer):
    return "<hidden>" if not Reveal_Answers else answer


def StringManipulationReverse(text):
     return text[::-1]

def StringManipulationUpperLowerLowered(word):
    clue = word.upper()
    return word.lower()


def StringManipulationTitleCase(word):
    sentence = f"{word} is great"
    return sentence.title()


def StringManipulationStrip(sample):
    return sample.strip()



def StringManipulationSwapcase(text):
    return text.swapcase()

def StringManipulationLstrip(sample):
    return sample.lstrip("-")

def StringManipulationCentre(text):
    return text.center(20, "-")



def StringManipulationStartsEnds(word, pre, suf):
    return (
        "yes" if word.startswith(pre) else "no",
        "yes" if word.endswith(suf) else "no",
    )


def StringManipulationFindIndex(s, sub):
    return (s.find(sub), s.index(sub))

def StringManipulationCount(word, ch):
    return word.count(ch)



def StringManipulationSplitJoin(csv):
    return "-".join(csv.split(","))


def StringManipulationSplitlinesJoin(poem):
    return ";".join(poem.splitlines())


def StringManipulationZfill(n):
    return n.zfill(5)



def StringManipulationCharTests(s):
  return( s.isalpha(),
    s.isdigit(),
    s.isalnum(),
    s.isspace(),
    s.islower(),
    s.isupper(),
    s.istitle(),
          )

def pReverse(word):
    __student_target = StringManipulationReverse(word)
    clue = word[::-1]
    target = word
    guess = input(f"reverse the word clue:{clue}")
    ok = clean(guess) == clean(target)
    return ok, redact(target)

def pUpperLower(word):
    __student_target = StringManipulationUpperLowerLowered(word)
    clue = word.upper()
    target = word.lower()
    guess = input(f"Make this lowercase {clue}\nLowercase: ")
    ok = clean(guess) == target
    return ok, redact(target)



def pTitle(word):
    __student_target = StringManipulationTitleCase(word)
    sentence = f"{word} is great"
    clue = sentence.lower()
    target = sentence.title()
    guess = input(f"Title-case this (must use .title()): '{clue}'\nAnswer: ")
    ok = guess == target
    return ok, redact(target)

def pSwapcase(_word):
    clue_text = "PyThOn RuLeS"
    __student_target = StringManipulationSwapcase(clue_text)
    target = clue_text.swapcase()
    guess = input(f"Swap the case (must use .swapcase()): {clue_text}\nAnswer: ")
    ok = guess == target
    return ok, redact(target)

def pStrip(_word):
    sample = "   spaced out   "
    __student_target = StringManipulationStrip(sample)
    target = sample.strip()
    guess = input(f"Trim spaces (must use .strip()): [{sample}]\nAnswer: ")
    ok = guess == target
    return ok, redact(target)


def pLstripRstrip(_word):
    sample = "---left only"
    _student_target = StringManipulationLstrip(sample)
    target = sample.lstrip("-")  
    guess = input(f"Remove leading '-' only : [{sample}]\nAnswer: ")
    ok = guess == target
    return ok, redact(target)


def pReplace(word):
    masked = "".join("*" if ch.lower() in "aeiou" else ch for ch in word)
    clue = masked
    guess = input(
        f"Unmask vowels in '{clue}' (type original word). "
        f"(earlier built with repeated .replace())\nAnswer: "
    )
    ok = clean(guess) == clean(word)
    return ok, redact(word)

def pAlign(_word):
    text = "MENU"
    _student_target = StringManipulationCentre(text)
    target = text.center(20, "-")
    guess = input("Centre 'MENU' to width 20 with '-' :\nAnswer: ")
    ok = guess == target
    return ok, redact(target)

def pPrefixSuffix(word):
    pre = word[:2]
    suf = word[-2:]
    _student_pair = StringManipulationStartsEnds(word, pre, suf)
    correct_pre = "yes" if word.startswith(pre) else "no"
    correct_suf = "yes" if word.endswith(suf) else "no"
    guess_pre = input(f"Does '{word}' start with '{pre}'? (yes/no) ").strip().lower()
    guess_suf = input(f"Does '{word}' end with '{suf}'? (yes/no) ").strip().lower()
    ok = (guess_pre == correct_pre) and (guess_suf == correct_suf)
    return ok, redact(f"starts:{correct_pre}, ends:{correct_suf}")




def pFindIndex(_word):
    s = "mississippi"
    _student_pair = StringManipulationFindIndex(s, "ss")
    pos_find = s.find("ss")
    pos_index = s.index("ss")
    ans1 = input(f"In '{s}', find position of 'ss' (must use .find()): ")
    ans2 = input(f"...and (must use .index()): ")
    ok = ans1.isdigit() and ans2.isdigit() and int(ans1) == pos_find and int(ans2) == pos_index
    return ok, redact(f"find:{pos_find}, index:{pos_index}")

def pCount(word):
    ch = random.choice("aeiou")
    _student_target = StringManipulationCount(word, ch)
    target = word.count(ch)
    ans = input(f"How many '{ch}' in '{word}'? ('{ch}')) ")
    ok = ans.isdigit() and int(ans) == target
    return ok, redact(str(target))

def pSplitJoin(_word):
    csv = "red,blue,green"
    _student_target = StringManipulationSplitJoin(csv)
    target = "-".join(csv.split(","))
    ans = input(f"Turn commas into hyphens {csv}\nAnswer: ")
    ok = ans == target
    return ok, redact(target)


def pSplitlinesJoin(_word):
    poem = "Roses\nViolets\nSugar\nSpice"
    _student_target = StringManipulationSplitlinesJoin(poem)
    lines = poem.splitlines()
    target = ";".join(lines)
    ans = input("Join lines with ';' (no spaces) (must use .splitlines() and .join): ")
    ok = ans == target
    return ok, redact(target)


def pZfill(_word):
    n = "42"
    _student_target = StringManipulationZfill(n)
    target = n.zfill(5)
    ans = input("Pad '42' to width 5 with zeros (must use .zfill(5)):\nAnswer: ")
    ok = ans == target
    return ok, redact(target)




def pCharTests(_word):
    s = input(
        "Type something; we'll classify it.\n"
        "Try: .isalpha(), .isdigit(), .isalnum(), .isspace(), .islower(), .isupper(), .istitle()\n"
        "Input: "
    )
    __student_tuple = StringManipulationCharTests(s)
    results = (s.isalpha(), s.isdigit(), s.isalnum(), s.isspace(), s.islower(), s.isupper(), s.istitle())
    print("alpha digit alnum space lower upper title ->", results)
    ok = any(results)
    return ok, redact(str(results))

PUZZLES = [
    pReverse, pUpperLower, pTitle, pSwapcase,
    pStrip, pLstripRstrip, pReplace, pAlign,
    pPrefixSuffix, pFindIndex, pCount,
    pSplitJoin, pSplitlinesJoin, pZfill, pCharTests
]

def main():
    print("String Gauntlet — Skeleton (answers hidden; complete the StringManipulation functions)")
    lives, score, rounds = 3, 0, 5
    for r in range(1, rounds + 1):
        word = random.choice(WORDS)
        puzzle = random.choice(PUZZLES)
        print(f"\n=== Round {r} | Lives: {lives} | Score: {score} ===")
        correct, reveal = puzzle(word)
        if correct:
            print(" Correct!")
            score += 1
        else:

            print(f" Not quite. Answer: {reveal}")
            lives -= 1
        if lives == 0:
            break
    print(f"\nGame over! Final score: {score}")


if __name__ == "__main__":
    main()
