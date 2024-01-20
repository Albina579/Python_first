# дана строка, в которой буква h встречается как минимум 2 раза.
# разверните последовательность символов, заключённую между первым и последним появлением буквы h
# в противоположном порядке

s = "I am learning Python. hello, World!"
h_first = s.find("h")
h_last = s.rfind("h")
s_new = s[:h_first] + s[h_last:h_first:-1] + s[h_last:]
print(s_new)
