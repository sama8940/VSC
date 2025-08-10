def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    result = sum_list(sample_list)
    print(f"結果はこちら!: {result}")
