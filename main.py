from src.paragraph_correction import ParagraphCorrection


if __name__ == '__main__':
    with open('./test-data/correct.txt') as f:
        correct = f.read()
    with open('./test-data/wrong.txt') as f:
        wrong = f.read()
    with open('./test-data/responese.txt') as f:
        response = f.read()

    para_crct = ParagraphCorrection(wrong, correct)
