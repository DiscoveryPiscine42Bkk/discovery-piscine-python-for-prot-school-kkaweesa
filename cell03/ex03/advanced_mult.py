for a in range(11):
    result = [a * b for b  in range(11)]
    print(f"table {a}: {' '.join(map(str, result))}")