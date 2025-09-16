# 探索対象の文字列text
text = ["A", "B", "A", "B", "A", "B", "A", "C"]
# textの長さ
text_len = len(text)

# 探索する文字列pat
pat = ["A", "B", "A", "C"]
# patの長さ
pat_len = len(pat)

# 見つかった位置（見つからないを意味する-1にしておく）
found_idx = -1

# textの探索位置
text_idx = 0
# textの探索終了位置
text_last_idx = text_len - pat_len

# textを探索する
while text_idx <= text_last_idx:
    # textとpatが一致するかどうかチェックする
    pat_idx = 0
    while pat_idx < pat_len:
        # 一致しない場合
        if text[text_idx + pat_idx] != pat[pat_idx]:
            break
        # チェック位置を1つ先に進める
        pat_idx += 1
    # 一致した場合
    if pat_idx == pat_len:
        # 見つかった位置を書き換える
        found_idx = text_idx
        break
    # 探索位置を1つ先に進める
    text_idx += 1

# 探索結果を表示する
print(f"探索結果は、{found_idx}です。")