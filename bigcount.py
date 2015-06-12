from collections import Counter
import io
import sys

cnt = Counter()

if len(sys.argv) < 2:
    print("Provide an input file as argument")
    sys.exit()

try:
    with io.open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                cnt[word] += 1
except FileNotFoundError:
    print("File not found")

with sys.stdout as f:
    total_word_count = sum(cnt.values())
    for word, count in cnt.most_common(3000000):
        f.write('{: < 6} {:<7.2%} {}\n'.format(
            count, count / total_word_count, word))
