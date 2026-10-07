s = "programming"

s1=s[0:4]
print(s1)

s2=s[8:]
print(s2)

s3=s[::-1]
print(s3)
def check_palindrome():
    word = "racecar"
    if word[::-1]=="racecar":
        return True
    else:
        return False
print(check_palindrome())

sentence = "  Learning Python is fun  "
sentence = sentence.strip()
print(sentence)

sentence = sentence.upper()
print(sentence)
sentence_list=sentence.split()
print(sentence_list)
print(len(sentence_list))

bonus = "hello world foo"
bonus_list= bonus.split()
print(bonus_list)
bonus_reverse_list=bonus_list[::-1]
print(bonus_reverse_list)
bonus_reverse= " ".join(bonus_reverse_list)
print(bonus_reverse)