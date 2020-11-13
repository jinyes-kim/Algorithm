def solution(phone_book):
    length = len(phone_book)

    if length == 1:
        return True

    for idx in range(length - 1):
        for phone_number in phone_book[idx + 1:]:
            pivot = len(phone_book[idx])
            if phone_book[idx] != phone_number and phone_book[idx] == phone_number[0:pivot]:
                return False

    return True