#!/usr/bin/env python3


s = 'A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'


def your_function(input_data):
    '''Trả về dict chứa tần suất xuất hiện của mỗi từ theo format:

        result = {
            'a': 1,  # 1 lần xuất hiện
            'count': 3,  # 3 lần xuất hiện
            ...
        }

    :rtype dict:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError(
        "Học viên chưa thực hiện tìm số lần xuất hiện của từng từ"
    )

    return result


def your_function_2(input_data):
    '''Trả về list chứa các tuple của 3 từ xuất hiện nhiều nhất kèm
    số lần xuất hiện của từ đó

    :rtype list:
    '''
    # Sửa tên function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError(
        "Học viên chưa tìm 3 từ xuất hiện nhiều nhất"
    )

    return result


def solve(input_data):
    '''Học viên không cần viết code trong hàm solve, chỉ thực hiện
    đổi tên lại 2 function của mình cho phù hợp

    :rtype tuple:
    '''
    result = (your_function(input_data), your_function_2(input_data))

    return result


def main():
    data = s
    print(solve(data))


if __name__ == "__main__":
    main()
