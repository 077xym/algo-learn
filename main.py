from collections import Counter
from heapq import heapify

import torch
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from symengine import ceiling


def getNumTeams(cost, min_cost: int, max_cost: int):
    cost.sort()
    res = 0
    for i in range(len(cost)):
        first_cost = cost[i]
        min_index = i + 1
        max_index = len(cost) - 1
        found = False
        while min_index <= max_index:
            if first_cost + cost[min_index] < min_cost:
                min_index += 1
            if first_cost + cost[max_index] > max_cost:
                max_index -= 1
            if min_cost <= first_cost + cost[min_index] and first_cost + cost[max_index] <= max_cost:
                found = True
                break
        if found:
            res += max_index - min_index + 1
    return res


def minimize_maximum_parcels(parcels, extra_parcels):
    max_parcels = max(parcels)
    for item in parcels:
        extra_parcels -= max_parcels - item
    if extra_parcels <= 0:
        return max_parcels
    else:
        add_on = extra_parcels // len(parcels) if float(extra_parcels // len(parcels)) == extra_parcels / len(
            parcels) else extra_parcels // len(parcels) + 1
        return max_parcels + add_on


def getMinimumBoxes(boxes, capacity):
    boxes.sort()
    boxes = boxes[::-1]
    max_box = 0
    for i in range(len(boxes)):
        left = len(boxes) - 1
        while boxes[i] > capacity * boxes[left]:
            left -= 1
        if max_box < left - i + 1:
            max_box = left - i + 1
    return len(boxes) - max_box


def getMinTotalDistance(dist_centers):
    dist_centers.sort()
    min_dist = 2 ** 31
    for i in range(1, len(dist_centers)):
        median_1 = (i - 1) // 2
        median_2 = (i + len(dist_centers) - 1) // 2
        cur_dist = 0

        for j in range(i):
            cur_dist += abs(dist_centers[j] - dist_centers[median_1])
        for j in range(i, len(dist_centers)):
            cur_dist += abs(dist_centers[j] - dist_centers[median_2])
        if cur_dist < min_dist:
            min_dist = cur_dist
    return min_dist


def maxAcutance(image):
    image = [list(i[0]) for i in image]
    row = len(image)
    col = len(image[0])
    row_one_ct = [0] * row
    col_one_ct = [0] * col
    for i in range(row):
        for j in range(col):
            if image[i][j] == "1":  # meaning row i and col j has 1
                row_one_ct[i] += 1
                col_one_ct[j] += 1

    max_act = -(row + col)
    for i in range(row):
        for j in range(col):
            max_act = max(max_act, 2 * (row_one_ct[i] + col_one_ct[j]) - (col + row))

    return max_act


def checkSimilarPasswords(newPasswords, oldPasswords):
    res = []
    for new, old in zip(newPasswords, oldPasswords):
        i = 0
        j = 0
        while i < len(new) and j < len(old):
            next_char = 'a' if new[i] == 'z' else chr(ord(new[i]) + 1)
            if old[j] == new[i] or old[j] == next_char:
                i += 1
                j += 1
            else:
                i += 1
        res.append('YES' if j == len(old) else 'NO')
    return res


import heapq


def calculate_maximum_reward_points(reward_values):
    tot_rewards = 0
    reward_values = [-value for value in reward_values]
    heapq.heapify(reward_values)
    item_cnt = 0

    while reward_values and -reward_values[0] > item_cnt:
        cur_val = -heapq.heappop(reward_values)
        tot_rewards += (cur_val - item_cnt)
        item_cnt += 1

    return tot_rewards


def make_power_non_decreasing(power):
    tot_power = 0
    for i in range(1, len(power)):
        if power[i] < power[i - 1]:
            tot_power += (power[i - 1] - power[i])
    return tot_power


# equivalence: for each letter[i], how many letters before i is a different letter
def countDistinctPasswords(password):
    letterCount = [0] * 26
    result = 1  # 1 for the original password

    for i, letter in enumerate(password):
        idx = ord(letter) - ord('a')
        # (i - letterCount[idx]) is the count of letters not equal to letter[i] before index i, namely the count of substrings ending at i that can reverse to become a different password
        result += i - letterCount[idx]
        letterCount[idx] += 1

    return result


def getSequence(dna):
    res = []
    for s, t in dna:
        char_occur = Counter(s)
        extra_chr = None
        anagram = True
        for c in t:
            if c in char_occur:
                if char_occur[c] == 1:
                    del char_occur[c]
                else:
                    char_occur[c] -= 1
            elif extra_chr and c != extra_chr:
                anagram = False
            else:
                extra_chr = c
        if len(char_occur) > 1:
            anagram = False
        res.append(anagram)
    return res


def getKeyIdentifier(key):
    # find the mid char
    # it is a palindrome -> first half = reverse(second half)
    # first half has same letters as second half
    # reorder first half alphabetically
    mid_idx = len(key) // 2
    mid_char = '' if len(key) % 2 == 0 else key[mid_idx]

    first_half = key[:mid_idx]
    count = [0] * 26
    for i in first_half:
        count[ord(i) - ord('a')] += 1

    lex_first_half = ""
    for i in range(len(count)):
        letter = chr(ord('a') + i)
        lex_first_half += letter * count[i]

    return lex_first_half + mid_char + "".join(reversed(lex_first_half))


def find_min_max(a):
    min_idx = 0
    max_idx = 0
    min_a = a[0]
    max_a = a[0]
    for i in range(1, len(a)):
        if a[i] <= min_a:
            min_a = a[i]
            min_idx = i
        elif a[i] >= max_a:
            max_a = a[i]
            max_idx = i
    return min_a, max_a, min_idx, max_idx


def fortune_telling(m, a, b):
    while m > 0:
        min_a, max_a, min_idx, max_idx = find_min_max(a)
        min_a_b = b[min_idx]
        max_a_b = b[max_idx]

        if max_a > max_a_b:  # swap current max
            a[max_idx] = max_a_b
            m -= 1
            continue
        elif min_a < min_a_b:
            a[min_idx] = min_a
            m -= 1
            continue
        else:
            break
    swapped_a_max = max(a)
    swapped_a_min = min(a)
    return swapped_a_max - swapped_a_min


def maximize_pnl(pnl):
    pnl.sort()
    total_profit = sum(pnl)
    k = 0
    while total_profit - pnl[k] > 0:
        total_profit -= pnl[k]
        k += 1
    return k + 1


def reduce_gifts(prices, k, threshold):
    prices.sort()
    prices = prices[::-1]
    if len(prices) <= k:
        return 0
    cur_sum = sum(prices[0:k])
    last_product = prices[0]
    for i in range(1, len(prices)):
        j = i + k
        if j >= len(prices):
            return i
        cur_sum = cur_sum - last_product + prices[i]
        if cur_sum < threshold:
            return i - 1
        else:
            last_product = prices[i]


def execute_process(execution):
    # key: initial execution time
    # value: execution time after some cohesive executions is executed
    initial_cur = {time: time for time in execution}
    total_time = 0

    for time in execution:
        total_time += initial_cur[time]
        initial_cur[time] -= initial_cur[time] // 2

    return total_time


# find the place target should be put into a, also we need to know whether we found target in a, or we didn't
def binary_search(a, target, find_max):
    lo = 0
    hi = len(a) - 1
    found = False
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < a[mid]:
            hi = mid - 1
        elif target > a[mid]:
            lo = mid + 1
        else:
            found = True
            if find_max:
                lo = mid + 1
            else:
                hi = mid - 1
    if found and find_max:
        return found, lo - 1
    else:
        return found, lo


def execute_process_ii(powers, min_powers, max_powers):
    # sort the powers
    # for each processor i, do binary search of min_power[i] and max_power[i] in the sorted powers
    # the returned value for min_power is the starting point of the range, and the returned value - 1 for max_power is the end point of the range
    powers.sort()
    res = []

    for i in range(len(min_powers)):
        min_power = min_powers[i]
        max_power = max_powers[i]
        _, proc_start = binary_search(powers, min_power, find_max=False)
        found, proc_end = binary_search(powers, max_power, find_max=True)
        if not found:
            proc_end -= 1
        total_proc = proc_end - proc_start + 1
        total_power = sum(powers[proc_start:proc_end+1])
        res.append([total_proc, total_power])

    return res




if __name__ == '__main__':
    # print(binary_search([1, 3, 7, 7, 7, 8, 11, 12, 13, 13, 13, 13, 15, 17], target=6, find_max=False))
    print((execute_process_ii([7, 6, 8, 10], [6, 3, 4], [10, 7, 9])))
