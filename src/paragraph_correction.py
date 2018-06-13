from src.diff_match_patch import diff_match_patch as dmp


class ParagraphCorrection:
    def __init__(self, wrong_paragraph, correct_paragraph):
        self.wrong_paragraph = wrong_paragraph
        self.correct_paragraph = correct_paragraph
        self.full_diffs = self.__diff_wordmode()
        self.diff = self.__diff_only()
        self.answer_key = self.__get_answer_key_from_diff()

    def __diff_wordmode(self):
        d = dmp()
        words = d.diff_linesToWords(self.wrong_paragraph,
                                    self.correct_paragraph)
        word_text_one = words[0]
        word_text_two = words[1]
        word_array = words[2]
        full_diffs = d.diff_main(word_text_one, word_text_two, False)
        d.diff_charsToLines(full_diffs, word_array)
        full_diffs = [(c, s.strip()) for c, s in full_diffs]
        return full_diffs

    def __diff_only(self):
        return [diff for diff in self.full_diffs if diff[0] != 0]

    def __get_answer_key_from_diff(self):
        answer_key = {}
        cur_answer = 0
        started = False
        start_index = end_index = None

        for i, diff in enumerate(self.full_diffs):
            if not started and diff[0] != 0:
                start_index = i
                started = True
            elif started and diff[0] == 0:
                end_index = i
                started = False

            start_w_end = start_index and end_index
            start_wo_end = i == len(self.full_diffs) - 1 and started

            if start_w_end or start_wo_end:
                s = slice(start_index, end_index)
                answer_key[cur_answer] = self.full_diffs[s]
                cur_answer += 1
                start_index = end_index = None

        return answer_key
