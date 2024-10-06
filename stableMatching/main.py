from collections import deque


# record which woman will a man propose next
def init_proposal_record(man_list: deque):
    res = {}
    for name in man_list:
        res[name] = 0
    return res


# record woman-man pair
def init_woman_to_man_pair_record(preference_woman: dict):
    res = {}
    for name in preference_woman:
        res[name] = ""
    return res


# record man-woman pair
def init_man_to_woman_pair_record(preference_man: dict):
    res = {}
    for name in preference_man:
        res[name] = ""
    return res


def is_prefer(man1, man2, w, preference_woman: dict):
    pref_list = preference_woman[w]
    m2_found = False
    for name in pref_list:
        if man1 == name and not m2_found:
            return True
        if m2_found:
            return False
        if man2 == name:
            m2_found = True
    return False


def stable_match(preference_man: dict, preference_woman: dict):
    man_list = deque(preference_man.keys())
    proposal_recorder = init_proposal_record(man_list)
    woman_to_man_pair = init_woman_to_man_pair_record(preference_woman)
    man_to_woman_pair = init_man_to_woman_pair_record(preference_man)
    while len(man_list) != 0:
        cur_man = man_list.popleft()
        w = preference_man[cur_man][proposal_recorder[cur_man]]
        proposal_recorder[cur_man] += 1
        if woman_to_man_pair[w] == "":
            woman_to_man_pair[w] = cur_man
            man_to_woman_pair[cur_man] = w
        elif is_prefer(cur_man, woman_to_man_pair[w], w, preference_woman):
            last_man = woman_to_man_pair[w]
            man_to_woman_pair[last_man] = ""
            woman_to_man_pair[w] = cur_man
            man_to_woman_pair[cur_man] = w
            man_list.appendleft(last_man)
        else:
            man_list.appendleft(cur_man)

    return man_to_woman_pair, woman_to_man_pair
