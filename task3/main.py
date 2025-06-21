import timeit

from kmp import kmp_search
from boyer import boyer_moore_search
from rabin import rabin_karp_search 

with open('text1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('text2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

pattern_no_exist = "що краще js чи python?"
pattern_exit1 = "return middleIndex"
pattern_exit2 = "Робинсон Я., Вебер Д., Эифрем Э"

algorithms = {
    "boyer_moore_search": boyer_moore_search,
    "kmp_search": kmp_search,
    "rabin_karp_search": rabin_karp_search
}

texts = {
    "text1": text1,
    "text2": text2
}

patterns = {
    "exist1": pattern_exit1,
    "exist2": pattern_exit2,
    "not_exist": pattern_no_exist
}

for algo_name, algo_fn in algorithms.items():
    for text_name, text_value in texts.items():
        for pattern_name, pattern in patterns.items():
            label = f"{algo_name} | {text_name} | {pattern_name}"
            result = algo_fn(text_value, pattern)
            print(f"{label} => Result: {result}")
            time = timeit.timeit(lambda: algo_fn(text_value, pattern), number=100)
            print(f"{label} => Time: {time:.6f} seconds\n")



   



# # BOYER
# print("boyer_moore_search result text1 pattern_no_exist", boyer_moore_search(text1, pattern_no_exist))
# print("boyer_moore_search: no exist pattern text 1", timeit.timeit(lambda: boyer_moore_search(text1, pattern_no_exist), number = 100))

# print("boyer_moore_search result text1 pattern_exit1", boyer_moore_search(text1, pattern_exit1))
# print("boyer_moore_search: exist pattern text 1", timeit.timeit(lambda: boyer_moore_search(text1, pattern_exit1), number = 100))

# print("boyer_moore_search result text2 pattern_no_exist", boyer_moore_search(text2, pattern_no_exist))
# print("boyer_moore_search: no exist pattern text 2", timeit.timeit(lambda: boyer_moore_search(text2, pattern_no_exist), number = 100))

# print("boyer_moore_search result text2 pattern_exit2", boyer_moore_search(text2, pattern_exit2))
# print("boyer_moore_search: exist pattern text 2", timeit.timeit(lambda: boyer_moore_search(text2, pattern_exit2), number = 100)) 


# #KMP
# print("kmp_search result text1 pattern_no_exist", kmp_search(text1, pattern_no_exist))
# print("kmp_search: no exist pattern text 1", timeit.timeit(lambda: kmp_search(text1, pattern_no_exist), number = 100)) 

# print("kmp_search result text1 pattern_exit1", kmp_search(text1, pattern_exit1))
# print("kmp_search: exist pattern text 1", timeit.timeit(lambda: kmp_search(text1, pattern_exit1), number = 100)) 

# print("kmp_search result text2 pattern_no_exist", kmp_search(text2, pattern_no_exist))
# print("kmp_search: no exist pattern text 2", timeit.timeit(lambda: kmp_search(text2, pattern_no_exist), number = 100)) 

# print("kmp_search result text2 pattern_exit2", kmp_search(text2, pattern_exit2))
# print("kmp_search: exist pattern text 2", timeit.timeit(lambda: kmp_search(text2, pattern_exit2), number = 100)) 

# #RABIN
# print("rabin_karp_search result text1 pattern_no_exist", rabin_karp_search(text1, pattern_no_exist))
# print("rabin_karp_search: no exist pattern text 1", timeit.timeit(lambda: rabin_karp_search(text1, pattern_no_exist), number = 100)) 

# print("rabin_karp_search result text1 pattern_exit1", rabin_karp_search(text1, pattern_exit1))
# print("rabin_karp_search: exist pattern text 1", timeit.timeit(lambda: rabin_karp_search(text1, pattern_exit1), number = 100)) 

# print("rabin_karp_search result text2 pattern_no_exist", rabin_karp_search(text2, pattern_no_exist))
# print("rabin_karp_search: no exist pattern text 2", timeit.timeit(lambda: rabin_karp_search(text2, pattern_no_exist), number = 100)) 

# print("rabin_karp_search result text2 pattern_exit2", rabin_karp_search(text2, pattern_exit2))
# print("rabin_karp_search: exist pattern text 2", timeit.timeit(lambda: rabin_karp_search(text2, pattern_exit2), number = 100))


