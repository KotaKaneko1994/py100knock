# -*- encoding: utf-8 -*-
import sys
import csv


def saveCols(file_path, cols):
    """
    :param file_path: str
    :param cols: List[int]
    :return: List[List]
    """
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        val = []
        for row in reader:
            val.append(row)
    r = []
    for i in cols:
        with open("col" + str(i+1) + ".txt", "w") as f:
            for row in val:
                f.write(row[i] + "\n")

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        print 'Usage: python %s filename' % argv[0]
        quit()
    file_path = str(argv[1])

    saveCols(file_path, cols=[0, 1])






