with open("res/day2.txt") as f:
    p = f.read().split(',')

def is_invalid(n, part):
    num_s = str(n)
    length = len(num_s)
    # Part 1
    if part == 1: return length % 2 == 0 and num_s[:length//2] == num_s[length//2:]
    # Part 2
    for i in range(1, length // 2 + 1):
        # Split into sections of length i
        if length % i == 0 and all(len(set(num_s[j::i])) == 1 for j in range(i)):
            return True
    return False

total1, total2 = 0, 0
for r in p:
    start, end = r.split('-')
    for i in range(int(start), int(end)+1):
        if is_invalid(i, 1): total1 += i
        if is_invalid(i, 2): total2 += i

print("Part 1:", total1)
print("Part 2:", total2)

# Golf - 240 characters
print(*map(sum,zip(*sum([[(i*((s:=str(i))[:(h:=(l:=len(s))//2)]==s[h:])*(1-(l%2)),i*(not all((l%j)+any(len(set(s[k::j]))-1 for k in range(j))for j in range(1,h+1))))for i in range(o,t+1)]for o,t in[map(int,r.split('-')) for r in p]],[]))))