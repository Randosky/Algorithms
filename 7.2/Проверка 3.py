def generate_permutations(length, minimum, maximum, prev=[], memo={}):
    if length == 0:
        print(*prev)
        return 1

    count = 0
    for i in range(minimum, maximum+1):
        if i in prev:
            continue

        # if (length - 1, i) in memo:
            # count += memo[(length - 1, i)]
        # else:
        count += generate_permutations(length - 1, minimum, i, prev + [i], memo)

    memo[(length, maximum)] = count
    return count

if __name__ == "__main__":
    k, mn, mx = map(int, input().split())
    total_count = generate_permutations(k, mn, mx)
    print(total_count)
