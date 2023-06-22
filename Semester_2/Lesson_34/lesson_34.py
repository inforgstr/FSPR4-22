import hashlib
import requests


from pathlib import Path


def request_api_data(query_param):
    url = "https://api.pwnedpasswords.com/range/" + str(query_param)

    result = requests.get(url)

    if result.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error fetching: {result.status_code}, check an API and try again."
        )

    return result


def get_psw_leaks_count(hash, hash_to_check):
    hash = (hash.split(":") for hash in hash.splitlines())
    for hash, count in hash:
        if hash == hash_to_check:
            return count

    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]

    response = request_api_data(first5_char)

    return get_psw_leaks_count(response.text, tail)


def main(passwords):
    for psw in passwords:
        count = pwned_api_check(psw)
        if count:
            print(f"{psw} was found {count} times ... you should change your password.")
        else:
            print(f"{psw} was not found. Good to go!")

    return "Success!"


# Task 1
# args = sys.argv[1:]
# print(args)
# print(main(args))


# Task 2
# path_to_file = Path(__file__).parent / "passwords.txt"

# data = path_to_file.read_text(encoding="utf-8")

# text = [passwords.split(", ") for passwords in data.splitlines()]

# for passwords in text:
#     print(main(passwords))
