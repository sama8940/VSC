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

# skip[0]～skip[25]にA～Zに対して何文字先に進めるかを設定しておく
# とりあえず、すべての文字にpat_lenを設定する
skip = [pat_len] * 26
# patの中にある文字（末尾を除く）は、その文字の位置に応じて設定を書き換える
pat_idx = 0
while pat_idx < pat_len - 1:
    skip[char_index(pat[pat_idx])] = pat_len - pat_idx - 1
    pat_idx += 1

# 見つかった位置（見つからないを意味する-1にしておく）
found_idx = -1

# textの探索位置
text_idx = pat_len - 1

# textを探索する
while text_idx < text_len:
    # textとpatが一致するかどうかチェックする
    pat_idx = pat_len - 1
    while pat_idx >= 0:
        # 一致しない場合
        if text[text_idx - (pat_len - 1 - pat_idx)] != pat[pat_idx]:
            break
        # チェック位置を1つ前に進める
        pat_idx -= 1
    # 一致した場合
    if pat_idx < 0:
        # 見つかった位置を書き換える
        found_idx = text_idx - (pat_len - 1)
        break
    # 探索位置をtextの探索位置の文字に合わせて先に進める
    text_idx += skip[char_index(text[text_idx])]

# 探索結果を表示する
print(f"探索結果は、{found_idx}です。")