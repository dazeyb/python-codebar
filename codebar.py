# Codebar

## Part I: Members, Students and Instructors

You're starting your own web development school called Codebar! Everybody at Codebar -- whether they are attending workshops or teaching them -- is a `Member`.
* Each member has a `full_name`.
* Each member should be able to `introduce` themselves (e.g., "Hi, my name is Kevin!").

Each `Member` is also either a `Student` or an `Instructor`.
* Each student has a `reason` for attending Codebar (e.g., "I've always wanted to make websites!").
* Each instructor a `bio` (e.g., "I've been coding in Python for 5 years and want to share the love!").
* Each instructor also has a set of `skills` (e.g., `["Python", "Javascript", "C++"]`).
* An instructor can gain a new skill using `add_skill`.




class Member:
    def __init__(self, reason):
        self.number = phone_number
        self.reason = reason
    
    def introduce(self):
        print(f"Calling {self.number} from {other_number}.")
    
    def text(self, other_number, msg):
        print(f"Sending text from {self.number} to {other_number}: {msg}")


class Student(Member):
    def __init__(self, reason="I've always wanted to make websites!"):
        self.number = phone_number
    
    def reason(self, other_number):
        print(f"Calling {self.number} from {other_number}.")
    
    def text(self, other_number, msg):
        print(f"Sending text from {self.number} to {other_number}: {msg}")



class Instructor(Member):
    def __init__(self, bio="I've been coding in Python for 5 years and want to share the love!"):
        self.number = phone_number
    
    def call(self, other_number):
        print(f"Calling {self.number} from {other_number}.")
    
    def text(self, other_number, msg):
        print(f"Sending text from {self.number} to {other_number}: {msg}")