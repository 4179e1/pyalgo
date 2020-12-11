#!/usr/bin/env python3

import sys, copy

def make_check_board(n):
    board = []
    for x in range(n):
        board.append(bytearray("."*n, "utf-8"))

    return board

def print_check_board(board):
    sys.stdout.write(" ")
    for i in range(len(board)):
        sys.stdout.write("{}".format(i))
    sys.stdout.write("\n")

    i = 0
    for x in board:
        print ("{}{}".format(i,x.decode('utf-8')))
        i+=1

    sys.stdout.write("\n")


def nqueen (n):
    cb = make_check_board(n)

    ans = []

    def isvalid (row, col):
        n = len(cb)
        #检查列是否有冲突
        for i in range(n):
            if cb[i][col] == ord('Q'):
                return False

        # 检查右上角是否有冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if cb[i][j] == ord('Q'):
                return False
            i -= 1
            j += 1


        # 检查左上角是否有冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if cb[i][j] == ord('Q'):
                return False
            i -= 1
            j -= 1

        return True

    def btf(row):
        if row == len(cb):
            ans.append (copy.deepcopy(cb))
            return

        for col in range (len(cb[row])):
            # 排除不合法选择
            if not isvalid(row, col):
                continue

            # 做选择
            cb[row][col] = ord('Q')
            
            # 进入下一行决策
            btf(row + 1)

            # 撤销选择
            cb[row][col] = ord('.')

    btf(0)

    return ans


if __name__ == "__main__":
    b = make_check_board(8)
    print_check_board (b)

    ans = nqueen(4)
    for x in ans:
        print_check_board(x)