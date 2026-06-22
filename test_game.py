from game import check_guess


class TestCheckGuess:
    def test_guess_too_high(self):
        assert check_guess(50, 75) == "high"

    def test_guess_too_low(self):
        assert check_guess(50, 25) == "low"

    def test_guess_correct(self):
        assert check_guess(50, 50) == "correct"

    # 边界情况：答案是 1
    def test_boundary_secret_is_1_guess_1(self):
        assert check_guess(1, 1) == "correct"

    def test_boundary_secret_is_1_guess_2(self):
        assert check_guess(1, 2) == "high"

    # 边界情况：答案是 100
    def test_boundary_secret_is_100_guess_100(self):
        assert check_guess(100, 100) == "correct"

    def test_boundary_secret_is_100_guess_99(self):
        assert check_guess(100, 99) == "low"
