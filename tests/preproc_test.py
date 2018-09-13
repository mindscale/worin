from worin.preproc import codify_letter


def test_codify_letter():
    assert codify_letter('a') == (24, 37, 56, 77)
    assert codify_letter('한') == (0, 56, 57, 81)
    assert codify_letter('韓') == (35, 37, 56, 77)