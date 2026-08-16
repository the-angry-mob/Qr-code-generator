import qrcode
def get_qr_content_choice():
    print("What is it that you want the QR Code to hold?")
    print("1. Website / URL")
    print("2. Plain text")
    print("3. Wi-Fi network")
    print("4. Phone number")
    print("5. Email address")
    print("6. SMS message")
    print("7. Contact information (vCard)")
    while True: 
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 7:
                print("\033[31mInvalid choice! Try again\033[0m")
            else:
                break
        except ValueError:
            print('\033[31mInvalid choice!Try again\033[0m')
    return choice
choice = get_qr_content_choice()
if choice == 1:
    while True:
        data = input("FULL Website URL: ")
        if data.startswith("http://") or data.startswith("https://"):
            break
        else:
            print("\033[31mInvalid format, try again!\033[0m")
elif choice == 2 :
    data = input("Message: ")
elif choice == 3 :
    name = input('Wi-Fi name (SSID): ')
    password = input('Wi-Fi password: ')
    data = f"WIFI:T:WPA;S:{name};P:{password};;"
elif choice == 4 :
    while True:
        number = input("Phone number: ")
        if len(number) > 15 or len(number) == 0 or number[0]!= '+' :
            print("\033[31mInvalid number, try again!\033[0m")
        else:
            data = f"tel:{number}"
            break
elif choice == 5 :
    while True:
        email = input("Email address: ")
        if '@' in email:
            data = f"mailto:{email}"
            break
        else:
            print("\033[31mThis is not an email BRUH\033[0m")
elif choice == 6 :
    while True:
        number = input("Phone number: ")
        if len(number) > 15 or len(number) == 0 or number[0]!= '+' :
            print("\033[31mInvalid number, try again!\033[0m")
        else:
            break
    message = input("Message to send: ")
    data = f"sms:{number}?body={message}"
elif choice == 7 :
    name = input("Name: ")
    while True:
            number = input("Phone number: ")
            if len(number) > 15 or len(number) == 0 or number[0]!= '+' :
                print("\033[31mInvalid number, try again!\033[0m")
            else:
                break
    while True:
            email = input("Email address: ")
            if '@' in email:
                data = f"mailto:{email}"
                break
            else:
                print("\033[31mThis is not an email BRUH\033[0m")

    data = (
    "BEGIN:VCARD\n"
    "VERSION:3.0\n"
    f"FN:{name}\n"
    f"TEL:{number}\n"
    f"EMAIL:{email}\n"
    "END:VCARD")
img = qrcode.make(data)
img.show()
