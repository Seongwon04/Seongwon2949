def rev_str(str):
    str_list = list(str)
    if len(str_list) < 1:
        return ''
    else:
        return str_list[-1] + rev_str(''.join(str_list[:-1]))

if __name__ == '__main__':
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))
