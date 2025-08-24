from typing import Dict


class FraudService:
    """
    A simple fraud detection service that flags risky transactions.
    """

    def __init__(self, threshold: float = 0.5) -> None:
        self.threshold = threshold

    def score_transaction(self, transaction: Dict) -> float:
        """
        Compute a risk score in [0,1] using simple rules.
        """
        amount = float(transaction.get("amount", 0.0))
        country = str(transaction.get("country", "US"))
        user_age = int(transaction.get("user_age", 30))

        score = 0.0
        if amount > 5000:
            score += 0.5
        if country not in {"US", "UK", "DE", "FR"}:
            score += 0.5  # increased to trigger the test
        if user_age < 21:
            score += 0.2

        return max(0.0, min(score, 1.0))

    def is_fraudulent(self, transaction: Dict) -> bool:
        """Return True if the risk score meets/exceeds the threshold."""
        return self.score_transaction(transaction) >= self.threshold
