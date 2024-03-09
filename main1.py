from collections import defaultdict 

dataset = [
    (6, 19, 28, 44, 60, 10),
    (36, 42, 50, 52, 67, 26),
    (3, 18, 27, 36, 53, 12),
    (16, 26, 29, 38, 50, 6),
    (24, 29, 42, 51, 54, 16),
    (3, 8, 40, 53, 58, 3),
    (4, 27, 33, 41, 42, 14),
    (4, 23, 45, 50, 53, 17),
    (6, 28, 59, 62, 69, 21),
    (1, 4, 45, 47, 67, 18),
    (17, 36, 43, 53, 67, 14),
    (27, 28, 34, 37, 44, 8),
    (12, 21, 62, 67, 69, 17),
    (1, 2, 27, 30, 67, 9),
    (9, 11, 27, 59, 66, 19),
    (15, 18, 19, 41, 43, 14),
    (39, 41, 43, 49, 64, 4),
    (7, 38, 65, 66, 68, 21),
    (1, 5, 32, 50, 64, 8),
    (24, 25, 43, 52, 63, 21),
    (16, 31, 34, 47, 65, 10),
    (18, 22, 43, 61, 65, 2),
    (13, 30, 35, 49, 59, 4),
    (13, 31, 33, 51, 58, 15),
    (25, 40, 43, 48, 50, 11),
    ]





count_dict = defaultdict(int)
top_ten = []
d_length = len(dataset)
patterns = {}

for i in range(1, 69):
    count_dict[i] = 0

def countNumbers(ds):
    for d in ds:
        for n in d:
            count_dict[n] += 1

def analyze_ds_patterns(ds):
    """ l = 1 - 22  m = 23 - 46  h = 47 - 69  """
    
    for d in ds:
        pattern = []
        s = ""

        for n in d:
            if n < 23:
                pattern.append('L')
            elif n >= 23 and n < 47:
                pattern.append('M')
            else:
                pattern.append('H')
        
        for e in pattern:
            s += e

        print(s)
        print(pattern)
        if s not in patterns:
            print("no")
            patterns[s] = 1
        else:
            patterns[s] += 1
    print(patterns)
        
def countRepeats(cd):
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_items[:10]
    top_10_list = [{key: (value/d_length)*100} for key, value in top_10]
    #print(top_10_list)
    return top_10_list

def analyze(nums):
    #print(type(nums))
    for i in nums:
        for key, value in i.items():
            top_ten.append(key)
    #print(top_ten)

def analyze_ds(ds):
    for d in ds:
        for i in top_ten:
            if i in d:
                pass
                #print(d)
                #print(i)


    

        
        


countNumbers(dataset)
#print(count_dict)
top_10_list = countRepeats(count_dict)
analyze(top_10_list)
analyze_ds(dataset)
analyze_ds_patterns(dataset)