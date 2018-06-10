from src.utils import diff_wordmode


if __name__ == '__main__':
    with open('./test-data/correct.txt') as f:
        correct = f.read()
    with open('./test-data/wrong.txt') as f:
        wrong = f.read()
    diffs = diff_wordmode(wrong, correct)
