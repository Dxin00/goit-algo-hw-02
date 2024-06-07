from collections import deque

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    char_deque = deque(cleaned_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    while True:
        input_string = input("Введіть рядок для перевірки на паліндром (або 'q' для виходу): ").strip()
        if input_string.lower() == 'q':
            break
        if is_palindrome(input_string):
            print("Рядок є паліндромом!")
        else:
            print("Рядок не є паліндромом.")

if __name__ == "__main__":
    main()
