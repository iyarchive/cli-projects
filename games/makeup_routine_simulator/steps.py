import time
from utils import slow_print, choose

def apply_primer(confidence, time_left):

    slow_print("\nDo you apply primer?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Took two minutes, but you have now applied primer. +1 Confidence. Wait to dry.")
        confidence += 1
        time_left -= 2

        slow_print(f"\nTime left: {time_left}")

        time.sleep(2)

        slow_print("\nAfter five minutes, your primer has now dried.")
        time_left -= 5
    else:
        slow_print("You skip primer. It was optional anyway. You lose 0 seconds.")

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")
    
    return confidence, time_left

def apply_foundation(confidence, time_left):

    slow_print("\nDo you apply foundation?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Took three minutes, but you have now applied foundation. +5 Confidence.")
        confidence += 5
        time_left -= 3

    else:
        slow_print("It was a bad acne day. -7 Confidence.")

        slow_print("\nWould you like to redo your decision??")
        retry = choose(["Yes", "No"])

        if retry == 1:
            slow_print("You take a deep breath and choose better.")

            slow_print("\nTook three minutes, but you have now finally applied foundation. +5 Confidence.")
            confidence += 5
            time_left -= 3

        else:
            slow_print("You accept your fate.")
            confidence -= 7

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_concealer(confidence, time_left):

    slow_print("\nDo you apply concealer?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Totally hiding those eyebags now. +3 Confidence.")
        confidence += 3
        time_left -= 3
    else:
        slow_print("You still create, darling. But that foundation isn't enough. Your eyebags are waving. -1 Confidence.")

        slow_print("\nWould you like to redo your decision??")
        retry = choose(["Yes", "No"])

        if retry == 1:
            slow_print("You take a deep breath and choose better.")

            slow_print("\nNo sight of any eyebags now! +3 Confidence.")
            confidence += 3
            time_left -= 3

        else:
            slow_print("You accept your fate.")
            confidence -= 1

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_blush(confidence, time_left):

    slow_print("\nDo you apply blush?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Took a minute to give yourself the natural flush. +3 Confidence.")
        confidence += 3
        time_left -= 1
    else:
        slow_print("You look a little pale. -2 Confidence.")
        confidence -= 2

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_contour(confidence, time_left):

    slow_print("\nDo you apply contour?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Cheekbones are looking sleek after a minute. +2 Confidence.")
        confidence += 2
        time_left -= 1
    else:
        slow_print("I see you prefer a cuter and more rounded face. +1 Confidence.")
        confidence += 1

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_highlighter(confidence, time_left):

    slow_print("\nDo you apply highlighter?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Absolutely glowing, queen! One minute well spent. +1 Confidence.")
        confidence += 1
        time_left -= 1
    else:
        slow_print("I see that you're going for a more natural look today. No shame in that.")

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_brows(confidence, time_left):

    slow_print("\nDo you fill in your brows?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("That took 4 minutes, but brows are finally filled. +4 Confidence.")
        confidence += 4
        time_left -= 4
    else:
        slow_print("Your brows are not that camera-ready. -3 Confidence")
        confidence -= 3

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_eyeshadow(confidence, time_left):

    slow_print("\nDo you apply eyeshadow?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Absolutely gorgeous. Three minutes of hard work to look fabulous for the next 12 hours. +3 Confidence.")
        confidence += 3
        time_left -= 3
    else:
        slow_print("Your eyelids are lacking a bit of color. -1 Confidence.")
        confidence -= 1

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_mascara(confidence, time_left):

    slow_print("\nDo you apply mascara?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("That's a minute, but your lashes suddenly gain main character energy. +3 Confidence.")
        confidence += 3
        time_left -= 1
    else:
        slow_print("Your eyes don't pop as much. -4 Confidence")
        confidence -= 4

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_lipstick(confidence, time_left):

    slow_print("\nDo you apply lipstick?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Ahh, finally. The finishing touch. A quick minute, and you're all done. +10 Confidence.")
        confidence += 10
        time_left -= 1
    else:
        slow_print("Why? -7 Confidence.")
        confidence -= 7

    slow_print(f"\nConfidence: {confidence}")
    slow_print(f"Time left: {time_left}")

    return confidence, time_left

def apply_setting_spray(confidence, time_left):

    slow_print("\nDo you apply primer?")
    choice = choose(["Yes", "No"])

    if choice == 1:
        slow_print("Finally locked that all in in just one minute. +2 Confidence.")
        confidence += 2
        time_left -= 1
    else:
        slow_print("You risk your makeup not staying in place for the whole day. -4 Confidence.")

        slow_print("\nWould you like to redo your decision??")
        retry = choose(["Yes", "No"])

        if retry == 1:
            slow_print("You take a deep breath and choose better.")

            slow_print("\nAlright, that makeup is staying ON! +2 Confidence.")
            confidence += 2
            time_left -= 1

        else:
            slow_print("You accept your fate.")
            confidence -= 4

    return confidence, time_left
