"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
import re
from typing import Callable, Iterable
from ast import literal_eval

PATTERN_FOR_EMAIL = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-z]+$"
PATTERN_FOR_ACCOUNT = "^[A-Za-z0-9]+$"
PATTERN_FOR_DATE = "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
RESULT_FILE_NAME = "result.txt"


def validate_line(line: str) -> bool:
    line_split = line.split(" ")
    if len(line_split) != 5:
        print(f"VIOLATION OF TEST DATA INPUT: {line_split}")
        return False
    else:
        email, amount, currency, account = line_split[0], line_split[1], line_split[2], line_split[3]
        return validate_email(email) and check_amount(amount) and check_currency(currency) and check_account(account)


def validate_email(email: str) -> bool:
    res = True if re.match(PATTERN_FOR_EMAIL, email) else False
    if not res:
        print(f"EMAIL VIOLATION: {email}")
    return res


def check_amount(amount: str) -> bool:
    res = isinstance(literal_eval(amount), int) or (isinstance(literal_eval(amount), float))
    if not res:
        print(f"AMOUNT VIOLATION: {amount}")
    return res


def check_currency(currency: str) -> bool:
    res = currency in ['AUD', 'USD', 'EUR', 'RUB', 'SEK']
    if not res:
        print(f"CURRENCY VIOLATION: {currency}")
    return res


def check_account(account: str) -> bool:
    res = True if re.match(PATTERN_FOR_ACCOUNT, account) else False
    if not res:
        print(f"ACCOUNT VIOLATION: {account}")
    return res


def validate_date(date: str) -> bool:
    res = True if any([re.match(PATTERN_FOR_DATE, d) for d in date.split(" ")]) else False
    if not res:
        print(f"DATE VIOLATION: {date.rstrip()}")
    return res


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    with open(filepath, "r") as test_data:
        for line in test_data:
            for validator in validators:
                if not validator(line):
                    with open(RESULT_FILE_NAME, "a") as file_to_write:
                        file_to_write.write(f"{line.strip()} {validator.__name__}\n")
                    break

    return RESULT_FILE_NAME


if __name__ == "__main__":
    check_data("data.txt", [validate_date, validate_line])
