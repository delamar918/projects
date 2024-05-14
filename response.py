from validator_collection import checkers

def main():
    email = input("What's your email? ")
    if validate_it(email):
        print("Valid")
    else:
        print("Invalid")

def validate_it(s):
    result = checkers.is_email(s)
    return result

if __name__ == "__main__":
    main()


