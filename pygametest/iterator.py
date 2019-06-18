import json
import random
import sys
import traceback

class AlgIterator(object):
    def __init__(self,
                 alg_dic: dict,
                 shuffle: bool =False):
        # self.alg_dic = alg_dic
        self.alg_dic = self.del_null(alg_dic)
        self.akeys = list(self.alg_dic.keys())
        if shuffle:
            # 出現するアルゴリズムの順番をランダムにする
            random.shuffle(self.akeys)
        self.alen = len(self.akeys)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.alen:
            raise StopIteration()
        letter = self.akeys[self.idx]
        alg = self.alg_dic[letter]
        self.idx += 1
        return letter, alg, self.idx

    def del_null(self, algs: dict) -> dict:
        # "ぬぬ"のような無効なレターペアの削除
        null_letters = []
        for k in list(algs.keys()):
            # nan 判定の方法としてfloatかどうかを用いる
            if isinstance(algs[k], float):
                null_letters.append(k)

        for nk in null_letters:
            del algs[nk]

        return algs

    def jump_letter(self, letter: str) -> None:
        if letter:
            try:
                self.idx = self.akeys.index(letter)
            except:
                # 無効なレターペアなら警告
                print("Letter {} is in not your letters.".format(letter))
                self.idx -= 1
        else:
            # 空文字ならパス
            pass

        return

def set_iterator(path: str = "../data/myalgs.json"):
    with open(path, "r", encoding="utf-8") as f:
        algs = json.load(f)

    return AlgIterator(algs, shuffle=False)

def main():
    with open("../data/myalgs.json", "r", encoding="utf-8") as f:
        algs = json.load(f)

    alg_iterator = AlgIterator(algs, shuffle=False)
    while(True):
        try:
            print(alg_iterator.__next__())
            key_input = input()
            alg_iterator.jump_letter(key_input)
        except:
            traceback.print_exc()
            print("all algs over.")
            break

    return



if __name__ == "__main__":
    main()