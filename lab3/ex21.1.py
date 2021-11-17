def from_string_to_list(string, container):
    container.extend(map(int, string.split()))


# if __name__ == '__main__':

    # a = [(input())]
    # from_string_to_list((input()), a)
    # print(*a)