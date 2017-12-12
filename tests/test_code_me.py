from some_module import extract_sentence_containing_word


# testing sentence method: simple case
def test_sentence_method_simple():
    assert extract_sentence_containing_word('This day. I like. You hungry?', 'like') == '[I like]'


# testing sentence method: question case
def test_sentence_method_question():
    assert extract_sentence_containing_word('This day. I like. You hungry?', 'hungry') == '[You hungry]'
