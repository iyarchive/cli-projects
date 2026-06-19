from utils import slow_print
from steps import (
    apply_primer,
    apply_foundation,
    apply_concealer,
    apply_blush,
    apply_contour,
    apply_highligher,
    apply_brows,
    apply_eyeshadow,
    apply_mascara,
    apply_lipstick,
    apply_setting_spray
)

def game_intro():
    slow_print("✨ Makeup Routine Simulator ✨")
    slow_print("You have 90 minutes to get ready.")
    slow_print("Choose the corresponding number of your choice.")

    slow_print("\nSkills: Fairly Intermediate" \
    "\nConfidence: 10/25")

def main():
    confidence = 10
    time_left = 90

    game_intro()

    confidence, time_left = apply_primer(confidence, time_left)
    confidence, time_left = apply_foundation(confidence, time_left)
    confidence, time_left = apply_concealer(confidence, time_left)
    confidence, time_left = apply_blush(confidence, time_left)
    confidence, time_left = apply_contour(confidence, time_left)
    confidence, time_left = apply_highlighter(confidence, time_left)
    confidence, time_left = apply_brows(confidence, time_left)
    confidence, time_left = apply_eyeshadow(confidence, time_left)
    confidence, time_left = apply_mascara(confidence, time_left)
    confidence, time_left = apply_lipstick(confidence, time_left)
    confidence, time_left = apply_setting_spray(confidence, time_left)

    slow_print("\nYou put down the spray and stare at your reflection.")
    time.sleep(1)
    slow_print("Wait.")
    time.sleep(1)
    slow_print("Oh.")
    time.sleep(1)
    slow_print("You actually ate that.")

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")


if __name__ == "__main__":
    main()
