from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio

@given(st.text() | st.none())
def test_sender_domain_no_crash(s):
    result = sender_domain(s)
    assert isinstance(result, str)

@given(st.text() | st.none())
def test_first_link_no_crash(s):
    result = first_link(s)
    assert isinstance(result, str)

@given(st.text() | st.none())
def test_shout_ratio_no_crash(s):
    result = shout_ratio(s)
    assert 0.0 <= result <= 1.0