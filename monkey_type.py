import random
import time

def check_accuracy(_sentence,_input):
    matching=0
    _sentence_=[w.strip(".,!?;:()") for w in _sentence.split()]
    _input_=[w.strip(".,!?;:()") for w in _input.split()]
    for i in range(min(len(_sentence_), len(_input_))):
        if _sentence_[i] == _input_[i]:
            matching+=1
    return matching/len(_sentence_) * 100

paragraph = "Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in these crates by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions."
text = paragraph.lower()
words = [w.strip(".,!?;:()") for w in text.split()]

sentence = ""

for i in range(25):
    sentence += random.choice(words) + " "
print("--- Welcome to Monkey type ---\n")
print(sentence)
start = time.time()
user_input=input("Your time starts now!\n")
user_input_stripped=[w.strip(".,!?;:()") for w in user_input.split()]
end = time.time()
minutes = int((end-start) // 60)
seconds = int((end-start) % 60)
total_minutes = (end-start)/ 60
accuracy = check_accuracy(sentence,user_input)
wpm = len(user_input_stripped)/total_minutes



print(f"Time taken = {minutes} Minutes & {seconds} seconds")
print(f"Accuracy = {accuracy:.1f}%")
print(f"Number of words typed: {len(user_input_stripped)}")
print(f"words per minute = {wpm:.1f}")

