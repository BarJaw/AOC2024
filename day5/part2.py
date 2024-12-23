def fix_update(rules, update):
    fixed = [None] * len(update)
    for i in range(len(update)):
        pos = len(update)
        pages_after = get_pages_after(rules, update[i])
        # print(update[i], pages_after)
        for page in pages_after:
            if page in update:
                pos -= 1
        fixed[pos - 1] = update[i]
    return fixed


def get_pages_after(rules, page):
    after = []
    for rule in rules:
        if rule[0] == page:
            after.append(rule[1])
    return after


def check_update(rules, update):
    for i in range(len(update) - 1):
        pages_after = get_pages_after(rules, update[i])
        for j in range(i + 1, len(update)):
            if update[j] not in pages_after:
                return False
    return True
        

def main():
    with open('./day5/input.txt', 'r') as f:
        x = f.read().split('\n\n')
        rules = x[0].split('\n')
        updates = x[1].split('\n')[:-1]
        for i in range(len(rules)):
            rules[i] = rules[i].split('|')
        for i in range(len(updates)):
            updates[i] = updates[i].split(',')
        s = 0
        for update in updates:
            res = check_update(rules, update)
            if not res:
                update = fix_update(rules, update)
                s += int(update[len(update) // 2])
        print(s)
                

if __name__ == '__main__':
    main()