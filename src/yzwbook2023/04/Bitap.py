# A～Zの英字を0～25に変換して返す関数
def char_index(c):
    return ord(c) - ord("A")

# 探索対象の文字列text
text = ["A", "B", "A", "B", "A", "B", "A", "C"]
# textの長さ
text_len = len(text)

# 探索する文字列pat
pat = ["A", "B", "A", "C"]
# patの長さ
pat_len = len(pat)

# mask[0]～mask[25]にA～Zに対するビット演算のマスクを設定しておく
# とりあえず、すべての文字のマスクに0を設定する
mask = [0] * 26
# patの中にある文字は、その文字のビット位置に1を設定する
pat_idx = 0
while pat_idx < pat_len:
    # ビット位置を１にした値を用意する
    bit_pos = 1 << pat_idx
    # patの中に同じ文字が存在する場合もあるので、
    # 単にビット位置を1にするだけでなく、
    # 既に設定済みの可能性があるマスクに、OR演算でビット位置を追加設定する
    mask[char_index(pat[pat_idx])] = mask[char_index(pat[pat_idx])] | bit_pos
    pat_idx += 1

# 状態を初期状態にする
status = 0

# 受理状態を判定するための変数（pat_len - 1ビット目を1とした数値）
accept_status = 1 << (pat_len - 1)

# 見つかった位置（見つからないを意味する-1にしておく）
found_idx = -1

# textの探索位置
text_idx = 0

# 状態を遷移させる
# （1）textの左端から1文字ずつチェックして、以下を行う
while text_idx < text_len:
    # （2）直前の状態を1ビット論理左シフトする
    status <<= 1
    # （3）（2）の結果と1をOR演算して、最下位ビットを立てる
    status |= 1
    # （4）（3）の結果と現在チェックしている1文字のマスクでAND演算を行い、
    # その結果を新たな状態とする
    status &= mask[char_index(text[text_idx])]
    # （5）状態の最上位桁（表では一番下）が1なら受理状態まで遷移したので、
    # patが見つかったことになる
    if status & accept_status != 0:
        found_idx = text_idx - (pat_len - 1)
        break
    # そうでないなら（2）に戻る
    text_idx += 1

# 探索結果を表示する
print(f"探索結果は、{found_idx}です。")