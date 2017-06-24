#!/usr/bin/env python3


__doc__ = '''
- Lưu file https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls về máy với tên event.yaml

- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml. load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra len của kiểu dữ liệu vừa tạo. Dùng thư viện json để `pickle. dump` nội
dung, ghi ra một file tên là event.json

- Dùng thư viện pickle và pickle.dump nội dung trên ra file event.pkl. Chú
ý khi mở file, phải mở ở chế độ 'wb' để ghi ở dạng binary.

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
'''


import os
import yaml
import json
import pickle


def your_function():
    '''Trả về len của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def solve():
    '''Học viên không cần viết code trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    '''
    result = your_function()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
