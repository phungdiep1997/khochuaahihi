#!/usr/bin/env python3

data = [
    {"name": "Hoang"},
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(input_data):
    '''Trả về list các tuple chứa cặp tên học viên và bạn gái.
    Nếu không có girl_friend thì đặt giá trị đó bằng string rỗng.
    '''
    result = None

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    result = solve(students)  # NOQA
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)


if __name__ == "__main__":
    main()
