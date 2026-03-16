from logic_utils import check_guess

def test_winning_guess():
    # Test winning with different numbers from game ranges
    # Easy range (1-20): test with 10
    outcome, message = check_guess(10, 10)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

    # Normal range (1-50): test with 35
    outcome, message = check_guess(35, 35)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # Test too high hints with numbers from actual game ranges
    # Easy range (1-20): secret=15, guess=18
    outcome, message = check_guess(18, 15)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    # Normal range (1-50): secret=22, guess=28
    outcome, message = check_guess(28, 22)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # Test too low hints with numbers from actual game ranges
    # Easy range (1-20): secret=12, guess=8
    outcome, message = check_guess(8, 12)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

    # Normal range (1-50): secret=42, guess=35
    outcome, message = check_guess(35, 42)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
