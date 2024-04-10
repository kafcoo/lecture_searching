import os, json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]


def liner_search(numbers, my_number):
    results = {"position":[], "count": 0}
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == my_number:
            results["position"].append(i)
            results["count"] += 1

    return results


def pattern_search(sequence, pattern):
    positions = set()
    sequence_index = 0
    n = len(sequence)
    m = len(pattern)
    while sequence_index < n - m:
        pattern_index = 0
        while pattern_index < m:
            if sequence[sequence_index + pattern_index] != pattern[pattern_index]:
                break
            pattern_index += 1
        if pattern_index == m:
            positions.add(sequence_index + m // 2)
        sequence_index += 1

    return positions


"""
# teoreticky ještě efektivnější řešení
    result = []
    for index in range(len(sequence) - len(pattern) + 1):
        if sequence[index:index + len(pattern)] == pattern:
            result.append(int(index + (len(pattern) / 2) - 0.5))

    result = set(result)
    return result

"""
def main():
    print(liner_search(read_data("sequential.json", "unordered_numbers"), my_number=9))
    print(pattern_search(read_data("sequential.json", "dna_sequence"), pattern="ATA"))


if __name__ == '__main__':
    main()