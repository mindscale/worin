from worin.tag import FeedForward


def test_feed_forward():
    tag = FeedForward()
    nouns = tag.nouns('"월인천강지곡"은 책이다.')
    assert nouns == ['월인천강지곡', '책']
