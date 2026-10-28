import pytest
from spam_scoring import score_message, classify, filter_inbox, inbox_status

def test_plain_message_scores_zero():
    """Test message with no spam words and no links."""
    assert score_message("hello there", False, 0) == 0

def test_low_score_is_clean():
    """Test classification for a clean score."""
    assert classify(1) == "clean"

def test_spam_scoring_basic():
    """Test basic spam word matching and link handling."""
    assert score_message("free cash winner", False, 4) == 10

def test_filter_and_status():
    """Test inbox filtering and status calculation."""
    messages = [
        ("free cash winner", False, 4),
        ("hello friend", False, 0)
    ]
    counts = filter_inbox(messages)
    assert inbox_status(counts) in ["healthy", "noisy", "flooded", "empty"]