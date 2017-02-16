# -*- encoding: utf-8 -*-
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        print 'Usage: python %s filename' % argv[0]
        quit()
    file_path = str(argv[1])

    with open(file_path) as f:
        print(len(f.readlines()))