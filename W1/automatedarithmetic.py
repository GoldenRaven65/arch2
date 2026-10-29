# 1. Kies sommen, tafelsommen of minsommen.
# 2. Schrijf twee getallen van 1 tot en met 100 op.
# 3. Zet het juiste teken ertussen: +, * of -.
# 4. Reken de som rustig uit op papier of met blokjes.
# 5. Schrijf je antwoord op en controleer het.
# 6. Doe dit tien keer en tel je goede antwoorden.
# 7. Schrijf je fouten op en probeer ze nog een keer.

import random



def arithmetic_operation(arithmetic_type):
    """Run ten exercises for the requested arithmetic operation.

    Args:
        arithmetic_type: One of ``summation``, ``multiplication``, or
            ``subtraction``.

    Raises:
        ValueError: If ``arithmetic_type`` is not supported.
    """
    operations = {
        "summation": ("+", lambda left, right: left + right),
        "multiplication": ("*", lambda left, right: left * right),
        "subtraction": ("-", lambda left, right: left - right),
    }

    if arithmetic_type not in operations:
        raise ValueError(
            "arithmetic_type must be summation, multiplication, or subtraction"
        )

    symbol, calculate = operations[arithmetic_type]
    correct_answers = 0
    mistakes = []

    for exercise_number in range(1, 11):
        left = random.randint(1, 100)
        right = random.randint(1, 100)
        expected = calculate(left, right)

        answer_text = input(f"{left} {symbol} {right} = ")
        try:
            answer = int(answer_text)
        except ValueError:
            answer = None

        if answer == expected:
            correct_answers += 1
        else:
            mistakes.append(
                f"{left} {symbol} {right} = {answer_text} "
                f"(correct answer: {expected})"
            )

    print(
        f'You had {correct_answers} correct and {len(mistakes)} incorrect '
        f'answers in "{arithmetic_type}"'
    )
    if mistakes:
        print("Mistakes:")
        for mistake in mistakes:
            print(mistake)


def main():
    """Ask the user which arithmetic operation to practise."""
    arithmetic_type = input(
        "Arithmetic operation (summation, multiplication, subtraction): "
    ).strip().lower()
    arithmetic_operation(arithmetic_type)


if __name__ == "__main__":
    main()