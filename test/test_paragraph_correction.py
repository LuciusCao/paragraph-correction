from src.paragraph_correction import ParagraphCorrection

import pytest


@pytest.mark.parametrize(
    'wrong_paragraph, correct_paragraph, full_diffs, diff, answer_key', [
        ('I am a boy', 'I was a girl',
         [(0, 'I'), (-1, 'am'),
          (1, 'was'), (0, 'a'),
          (-1, 'boy'), (1, 'girl')],
         [(-1, 'am'), (1, 'was'),
          (-1, 'boy'), (1, 'girl')],
         {0: [(-1, 'am'), (1, 'was')],
          1: [(-1, 'boy'), (1, 'girl')]},
        ),
        ('I am, a boy', 'I was, a girl',
         [(0, 'I'), (-1, 'am'),
          (1, 'was'), (0, ', a'),
          (-1, 'boy'), (1, 'girl')],
         [(-1, 'am'), (1, 'was'),
          (-1, 'boy'), (1, 'girl')],
         {0: [(-1, 'am'), (1, 'was')],
          1: [(-1, 'boy'), (1, 'girl')]},
        ),
        ('I am a boy.', 'I was a girl.',
         [(0, 'I'), (-1, 'am'),
          (1, 'was'), (0, 'a'),
          (-1, 'boy'), (1, 'girl'), (0, '.')],
         [(-1, 'am'), (1, 'was'),
          (-1, 'boy'), (1, 'girl')],
         {0: [(-1, 'am'), (1, 'was')],
          1: [(-1, 'boy'), (1, 'girl')]},
         ),
    ])
def test_initialization(wrong_paragraph, correct_paragraph, full_diffs,
                        diff, answer_key):
    para_crct = ParagraphCorrection(wrong_paragraph, correct_paragraph)
    assert para_crct.wrong_paragraph == wrong_paragraph
    assert para_crct.correct_paragraph == correct_paragraph
    assert para_crct.full_diffs == full_diffs
    assert para_crct.diff == diff
    assert para_crct.answer_key == answer_key
