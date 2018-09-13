from worin.tag import Worin, pos_tagging_model


text = '세종은 조선의 4대 왕이다'
tagger = Worin()


def test_split_text():
    texts = tagger._split_text(text * 10)
    assert len(texts) == 2


def test_nouns():
    nouns = tagger.nouns(text)
    assert nouns == ['세종', '조선', '대', '왕']


def test_pos():
    pos = tagger.pos(text)
    assert pos == [
        ('세종', 'N'), ('은', 'J'),
        ('조선', 'N'), ('의', 'J'),
        ('4', 'S'), ('대', 'N'),
        ('왕', 'N'), ('이', 'J'), ('다', 'E')
        ]


