from src.diff_match_patch import diff_match_patch as dmp


class ParagraphCorrection:
    def __init__(self, wrong_paragraph, correct_paragraph):
        if wrong_paragraph == correct_paragraph:
            raise Exception("Two paragraphs must be different")

        self.wrong_paragraph = wrong_paragraph
        self.correct_paragraph = correct_paragraph
        self.full_diffs = self.__diff_wordmode()
        self.diff = self.__diff_only()
        self.answer_key = self.__get_answer_from_diff()

    def __diff_wordmode(self, paragraph_one=None, paragraph_two=None):
        if paragraph_one is None:
            paragraph_one = self.wrong_paragraph
        elif not isinstance(paragraph_one, str):
            raise Exception('Paragraph must be a string!')

        if paragraph_two is None:
            paragraph_two = self.correct_paragraph
        elif not isinstance(paragraph_two, str):
            raise Exception('Paragraph must be a string!')

        d = dmp()
        words = d.diff_linesToWords(paragraph_one, paragraph_two)
        word_text_one = words[0]
        word_text_two = words[1]
        word_array = words[2]
        full_diffs = d.diff_main(word_text_one, word_text_two, False)
        d.diff_charsToLines(full_diffs, word_array)
        full_diffs = [(c, s.strip()) for c, s in full_diffs]
        return full_diffs

    def __diff_only(self, full_diffs=None):
        if full_diffs is None:
            full_diffs = self.full_diffs.copy()

        return [diff for diff in full_diffs if diff[0] != 0]

    def __get_answer_from_diff(self, full_diffs=None):
        if full_diffs is None:
            full_diffs = self.full_diffs.copy()

        answer = {}
        cur_answer = 0
        started = False
        start_index = end_index = None

        for i, diff in enumerate(full_diffs):
            if not started and diff[0] != 0:
                start_index = i
                started = True
            elif started and diff[0] == 0:
                end_index = i
                started = False

            start_w_end = start_index and end_index
            start_wo_end = i == len(full_diffs) - 1 and started

            if start_w_end or start_wo_end:
                s = slice(start_index, end_index)
                answer[cur_answer] = full_diffs[s]
                cur_answer += 1
                start_index = end_index = None

        return answer

    def evaluate_response(self, response=None):
        if response == None:
            raise Exception("You must input your response!")
        if not isinstance(response, str):
            raise Exception("Response must be a string!")

        full_diffs = self.__diff_wordmode(paragraph_two=response)
        diff_only = self.__diff_only(full_diffs=full_diffs)
        answer = self.__get_answer_from_diff(full_diffs=full_diffs)
        return full_diffs, diff_only, answer

    def compare_answers(self, answer=None, answer_key=None):
        if answer == None:
            raise Exception('An answer must be specified!')
        elif not isinstance(answer, dict):
            raise Exception('The answer must be a dictionary!')
        else:
            compared_answer = answer.copy()

        if answer_key == None:
            answer_key = self.answer_key.copy()
        elif not isinstance(answer_key, dict):
            raise Exception('Answer key must be a dictionary!')

        for k, v in answer.items():
            if v in answer_key.values():
                compared_answer[k].insert(0, 'CORRECT')
            else:
                compared_answer[k].insert(0, 'INCORRECT')

        return compared_answer
