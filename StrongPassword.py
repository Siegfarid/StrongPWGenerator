import random
import string

def generate_password(length):
    if length < 12:
        print("Panjang kata sandi minimal harus 12 karakter.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        panjang = int(input("Masukkan panjang minimal kata sandi (minimal 12 karakter): "))
        password = generate_password(panjang)
        if password:
            print("Kata sandi acak Anda:", password)
            break
    except ValueError:
        print("Masukkan bilangan bulat yang valid.")