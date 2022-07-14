from bbquote852.api_request import get_quote

print('2nd: ', get_quote())

def test_type_get_quote():
    assert type(get_quote()) == int

def test_length_get_quote():
    assert len(get_quote()) > 0
