import pytest
from spam_scoring import score_message, classify, filter_inbox, inbox_status

def test_score_message_branches():
    """Test spam word matching and uppercase word branches."""
    assert score_message("FREE cash winner", False, 0) == 6
    assert score_message("HELLO world", False, 0) == 1

def test_link_count_branches():
    """Test link count thresholds (>3, >0, and 0)."""
    assert score_message("hello", False, 4) == 4
    assert score_message("hello", False, 2) == 1
    assert score_message("hello", False, 0) == 0

def test_sender_known_and_floor_branches():
    """Test known sender logic and score floor limit (< 0)."""
    assert score_message("hello", True, 0) == 0
    assert score_message("free cash", True, 0) == 1

def test_classify_branches():
    """Test all classification brackets (spam, suspicious, clean)."""
    assert classify(10) == "spam"
    assert classify(8) == "spam"
    assert classify(5) == "suspicious"
    assert classify(4) == "suspicious"
    assert classify(3) == "clean"

def test_filter_inbox_branch():
    """Test inbox filtering across multiple messages."""
    messages = [
        ("free cash winner", False, 4),
        ("hello friend", False, 0),
        ("urgent prize", False, 1)
    ]
    result = filter_inbox(messages)
    assert isinstance(result, dict)

def test_inbox_status_branches():
    """Test inbox status conditions (empty, flooded, noisy, healthy)."""
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
    assert inbox_status({"spam": 6, "suspicious": 1, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 3, "suspicious": 2, "clean": 5}) == "noisy"
    assert inbox_status({"spam": 1, "suspicious": 2, "clean": 7}) == "healthy"