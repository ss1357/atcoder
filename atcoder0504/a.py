import copy
from collections import Counter

def is_complete(boad):
    for col in boad:
        if ['.'] in col:
            return False
    return True


def change_around_white_cells(boad, h, w, x, y):
    # 5を中心とした座標の辞書
    index_dic = {1:(-1, 0), 2:(0, -1), 3:(0, 1), 4:(1, 0)}
    # 一番左の列に中心
    if x - 1 < 0:
        index_dic.pop(1)

    # 一番右の列に中心
    if x + 1 >= w:
        index_dic.pop(4)

    # 一番上の行に中心
    if y - 1 < 0:
        index_dic.pop(2)

    # 一番下の行に中心
    if y + 1 >= h:
        index_dic.pop(3)

    for key in index_dic.keys():
        i, j = index_dic[key]
        boad[y + j][x + i] = ['#']

    return boad

def change_around_black_cells(boad, h, w, x, y):
    # 5を中心とした座標の辞書
    index_dic = {1:(-1, 0), 2:(0, -1), 3:(0, 1), 4:(1, 0)}
    # 一番左の列に中心
    if x - 1 < 0:
        index_dic.pop(1)

    # 一番右の列に中心
    if x + 1 >= w:
        index_dic.pop(4)

    # 一番上の行に中心
    if y - 1 < 0:
        index_dic.pop(2)

    # 一番下の行に中心
    if y + 1 >= h:
        index_dic.pop(3)

    for key in index_dic.keys():
        i, j = index_dic[key]
        if boad[y + j][x + i] == ['#']:
            boad[y + j][x + i] = ['#']
            break

    return boad

def check_major(boad):
    all_cell = []
    for b in boad:
        line = ""
        for i in b:
            line += i[0]
        all_cell.append("".join(line))
    all_cell = "".join(all_cell)
    cell_cnt = Counter(list(all_cell))
    if "#" in cell_cnt.most_common()[0]:
        return "#"
    return "."


def main():
    #マス目入力
    input_data = input().split()
    h, w = (int(i) for i in input_data)
    # print(h,w)
    #盤面入力
    boad = []
    for i in range(h):
        boad.append(list(list(i) for i in input()))
    # print(boad)

    new_boad = copy.deepcopy(boad)

    cnt = 0
    complete_flag = is_complete(boad)
    while(not complete_flag):
        cnt += 1
        print(check_major(boad))
        for y, col in enumerate(boad):
            if ['#'] in col:
                indexes = [i for i, d in enumerate(col) if d == ['#']]
                for x in indexes:
                    cell = col[x]
                    if cell == ['#']:
                        new_boad = change_around_white_cells(new_boad, h, w, x, y)
                        complete_flag = is_complete(new_boad)
                        if complete_flag:
                            break
                    if ['#'] not in col[x:]:
                        break
            if complete_flag:
                break

        boad = copy.deepcopy(new_boad)
        # for b in new_boad:
        #     print(b)
        # print("++++++++")
    print(cnt)


if __name__ == '__main__':
    main()