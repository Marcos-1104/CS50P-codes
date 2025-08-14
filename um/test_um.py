from um import count

def test_word():
    assert count ("yummy") == 0

def test_signs():
    assert count ("um?") == 1
    assert count ("Um, thanks, um...") == 2

def test_mixed():
    assert count ("Um, thanks for the album.") == 1

def test_true():
    assert count ("um") == 1

