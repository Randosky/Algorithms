def get_weights_dict(weights):
    weights_dict = {}
    for i in range(alphabet):
        weight = weights[i]
        if weight not in weights_dict:
            weights_dict[weight] = []
        weights_dict[weight].append(i)
    return weights_dict


def count_occurrences(message):
    counts = {}
    for s in message:
        index = ord(s) - chars
        counts[index] = counts.get(index, 0) + 1
    return counts


def calculate_weight(message, weights_dict, counts):
    total_weight, position, result_word = 0, 0, []

    for weight in sorted(weights_dict.keys(), reverse=True):
        for index in weights_dict[weight]:
            if index in counts and counts[index] > 1 and weight > 0:
                total_weight += (len(message) - 1 - position * 2) * weight
                result_word.append(chr(index + chars))
                position += 1
                counts[index] -= 2

    end_result_word = len(result_word)

    for index in range(alphabet):
        if index in counts:
            for _ in range(counts[index]):
                result_word.append(chr(index + 1072))

    final_result = "".join(result_word + result_word[:end_result_word][::-1])
    return final_result, total_weight


if __name__ == "__main__":
    m = input()
    w = list(map(int, input().split()))
    alphabet = 32
    chars = 1072

    total_r, total_w = calculate_weight(m, get_weights_dict(w), count_occurrences(m))

    print(total_r, total_w)
