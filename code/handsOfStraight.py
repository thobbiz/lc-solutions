from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)

        for card_value in sorted(hand):
            if card_count[card_value] > 0:
                for next_card in range(card_value, card_value + groupSize):
                    if card_count[next_card] == 0:
                        return False
                    card_count[next_card] -= 1

        return True
