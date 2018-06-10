from diff_match_patch import diff_match_patch as dmp


def diff_wordmode(text1, text2):
    d = dmp()
    words = d.diff_linesToWords(text1, text2)
    word_text_1 = words[0]
    word_text_2 = words[1]
    word_array = words[2]
    diffs = d.diff_main(word_text_1, word_text_2, False)
    d.diff_charsToLines(diffs, word_array)
    return diffs
