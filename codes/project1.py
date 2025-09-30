name1 = input("enter your good name please:")
name2 = input("what is he/she's good name:")
combine_strings = name1 + name2
lower_case_strings = combine_strings.lower()

t = lower_case_strings.count("t")
r = lower_case_strings.count("r")
u = lower_case_strings.count("u")
e = lower_case_strings.count("e")
true = t + r + u + e

l = lower_case_strings.count("l")
o = lower_case_strings.count("o")
v = lower_case_strings.count("v")
e = lower_case_strings.count("e")
love = l + o + v + e
 
love_score =int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"your love score is {love_score } and your are combind like a milk and water...❤️❤️")
elif love_score >= 40 and love_score <= 50:
    print(f"your love score is {love_score } and your are combind like a alright ")
else:
    print(f"your love score is {love_score }.")

