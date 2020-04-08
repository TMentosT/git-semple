#!/usr/bin/python3
# -*- coding: utf-8 -*-

def read_the_file(dir_path):
    with open(dir_path, 'r') as file:
        for line in file:
            if '+' in line:
                index = line.find('+')
                convert(line[index:])


def convert(line):
    nums = ''.join(filter(str.isdigit, line))
    nums = nums[1:11]
    result = "+1 ({}{}{}) {}{}{}{}{}{}{}".format(*nums)
    print(result)

def main():
    dir_path = str(input("Введите полный путь до файла и название файла:\n"))
    try:
        read_the_file(dir_path)
    except:
        print("Возможно путь был указан неправильно или файл не существует.\nПопробуйте еще раз")
        main()

if __name__ == "__main__":
    main()
