from collections import defaultdict
import numpy as np
import pylab as plt
import re

log_file = input('Log file path: ')
out_file = input('Out file path: ')

with open(log_file) as fd:
    lines = fd.readlines()
    ratios = []
    sizes = []
    for i in range(len(lines)):
        res = re.match('.*?compression ratio ([\d]+\.[\d]+).*?', lines[i])
        if res is not None:
            ratios.append(1 - 1/float(res.group(1)))

            res = re.match('.*?Acceptable block.*? Tx:([\d]+).*?', lines[i+2])
            if res is not None:
                sizes.append(int(res.group(1)))

with open(out_file, 'w') as fd:
    fd.write('block_txs,compression_ratio\n') 
    for size, ratio in zip(sizes, ratios):
        fd.write('%d,%f\n' % (size, ratio))

large_size_ratios = [pair[1] for pair in zip(sizes, ratios) if pair[0] > 1000]
print('best compression overall: ', max(ratios))
print()
print('Results for all blocks, n: ', len(ratios))
print('mean compression: ', np.mean(ratios))
print('median compression: ', np.median(ratios))
print()
print('Results for blocks with more than 1K txs, n: ', len(large_size_ratios))
print('mean compression: ', np.mean(large_size_ratios))
print('median compression: ', np.median(large_size_ratios))
plt.scatter(sizes, ratios, alpha=0.75)
plt.xlabel('transactions in block')
plt.ylabel('compression ratio')
plt.ylim((0.95, 1.0))
plt.grid(True)

size_ratios_map = defaultdict(list)
for size, ratio in zip(sizes, ratios):
    size_ratios_map[size//50].append(ratio)

plt.figure()
plt.boxplot(size_ratios_map.values())
plt.xlabel('transactions in block')
plt.ylabel('compression rate')
plt.ylim((0.95, 1.0))
plt.xticks(rotation='vertical')
plt.xticks(sorted(size_ratios_map.keys()), [50*k for k in sorted(size_ratios_map.keys())], rotation='vertical')
plt.tight_layout()
plt.show()
