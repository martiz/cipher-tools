from keyboard_maps import *
import string

# --- Cipher Implementations ---

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text (str): The input text.
        shift (int): The number of positions to shift letters.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The processed text.
    """
    result = ""
    if mode == "decrypt":
        shift = -shift  # Decryption is just shifting the other way

    for char in text:
        if char.isalpha():
            # Determine the starting character ('a' or 'A')
            start = ord("a") if char.islower() else ord("A")
            # Calculate the shifted position (0-25)
            offset = (ord(char) - start + shift) % 26
            # Convert back to character
            result += chr(start + offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def atbash_cipher(text):
    """
    Encrypts or decrypts text using the Atbash cipher (A=Z, B=Y...).

    Args:
        text (str): The input text.

    Returns:
        str: The processed text. (Encryption and decryption are the same)
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            # Calculate the mirrored position (0-25)
            offset = 25 - (ord(char) - start)
            result += chr(start + offset)
        else:
            result += char
    return result

# --- QWERTY Keyboard Shift Data (Simple version, ignores edges) ---
# fmt: off

# Here was the QWERTY_ENCRYPT_MAP, outsourced to keyboard_maps.py

# Create decrypt map by reversing the encrypt map
QWERTY_DECRYPT_MAP = {v: k for k, v in QWERTY_ENCRYPT_MAP.items()}
# fmt: on

def keyboard_shift_qwerty(text, mode):
    """
    Encrypts (shifts right) or decrypts (shifts left) using QWERTY layout.

    Args:
        text (str): The input text.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The processed text.
    """
    result = ""
    shift_map = QWERTY_ENCRYPT_MAP if mode == "encrypt" else QWERTY_DECRYPT_MAP
    for char in text:
        # Get the shifted char, or the original if not in the map
        result += shift_map.get(char, char)
    return result

# --- Helper Functions ---

def get_int_input(prompt):
    """Gets integer input from the user with validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# --- Main Program Logic ---

def main():
    """Runs the main encryption/decryption tool."""
    print("╔════════════════════════╗")
    print("║    hid-D/E/N-crypt     ║")
    print("╚════════════════════════╝")
    print("--- Simple Cipher Tool ---")

    # Choose mode FIRST
    while True:
        mode_choice = (
            input("Choose mode (e for encrypt, d for decrypt): ").lower().strip()
        )
        if mode_choice in ["e", "encrypt"]:
            mode = "encrypt"
            break
        elif mode_choice in ["d", "decrypt"]:
            mode = "decrypt"
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

    # Get text input SECOND
    text_to_process = input(f"Enter the text to {mode}: ")

    # Choose cipher THIRD
    print("\nAvailable Cipher Methods:")
    print("1: Caesar Cipher")
    print("2: Atbash Cipher")
    print("3: QWERTY Keyboard Shift (Right for encrypt, Left for decrypt)")

    while True:
        try:
            cipher_choice = int(input("Choose cipher method (1-3): "))
            if 1 <= cipher_choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process based on choice
    result_text = ""
    if cipher_choice == 1:
        shift_value = get_int_input(
            f"Enter the Caesar shift value (e.g., 1 for {mode}ing A->B): "
        )
        result_text = caesar_cipher(text_to_process, shift_value, mode)
    elif cipher_choice == 2:
        if mode == "decrypt":
            print(
                "(Note: Atbash encryption and decryption are the same operation.)"
            )
        result_text = atbash_cipher(text_to_process)
    elif cipher_choice == 3:
        result_text = keyboard_shift_qwerty(text_to_process, mode)

    # Display result
    print(f"\n--- Result ({mode.capitalize()}ed Text) ---")
    print(result_text)
    print("-------------------------------")

if __name__ == "__main__":
    main()
