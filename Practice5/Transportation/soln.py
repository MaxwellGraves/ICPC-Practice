from symbol import comparison


s, r, f, t = map(int, input().split())

raw_mats = { name : [] for name in input().split()}
factories = { name : [] for name in input().split()}
companies = {n : {name for name in input().split()[1:]} for n in range(t)}

