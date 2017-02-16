# -*- encoding: utf-8 -*-
import sys
import csv

def merge_files(file_list, filename="merge.txt"):
    with open(filename, "w") as write_f:
        cols = []
        for file_path in file_list:
            with open(file_path) as f:
                col = []
                for row in f:
                    col.append(row.rstrip())
                cols.append(col)

        for i in range(len(cols[0])):
            for j in range(len(cols)):
                write_f.write(cols[j][i])
                if j != len(cols)-1:
                    write_f.write("\t")
            write_f.write("\n")


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        print 'Usage: python %s filename1 filename2 ...' % argv[0]
        quit()
    file_list = []
    for file_path in argv[1:]:
        file_list.append(file_path)

    merge_files(file_list)






