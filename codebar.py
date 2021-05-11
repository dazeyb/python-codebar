# # Codebar

# ## Part I: Members, Students and Instructors

# You're starting your own web development school called Codebar! Everybody at Codebar -- whether they are attending workshops or teaching them -- is a `Member`.
# * Each member has a `full_name`.
# * Each member should be able to `introduce` themselves (e.g., "Hi, my name is Kevin!").

# Each `Member` is also either a `Student` or an `Instructor`.
# * Each student has a `reason` for attending Codebar (e.g., "I've always wanted to make websites!").
# * Each instructor a `bio` (e.g., "I've been coding in Python for 5 years and want to share the love!").
# * Each instructor also has a set of `skills` (e.g., `["Python", "Javascript", "C++"]`).
# * An instructor can gain a new skill using `add_skill`.




class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduction(self, introduction):
        self.introduction = introduction
        print(f"Hello, my name is {full_name}")
    
    def __str__(self):
        return f"{self.full_name}"



class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

    def reason(self):
        print(f"{reason}")

    def __str__(self):
        return f"The Member {self.full_name} gave this reason'{self.reason}'"



class Instructor(Member):
    def __init__(self, full_name, bio, skills):
        super().__init__(full_name)
        self.bio = bio
        self.skills = [skills]


    def add_skill(self, skill):
        self.skills = self.skill.append(skill)


keith = Student("Keith", "Loves codin")
print(keith)
 


class Workshop:
    def __init__(self, name, date, subject, instructors=[], students=[]):
        self.name = name
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students


    
    def add_participant(self, participant):
        if isinstance(participant, Instructor):
            self.instructors.append(participant)

        elif isinstance(participant, Student):
            self.students.append(participant)

        else:
            print("That is not a member")

    def print_details(self):
        print(f"The workshop is {self.date} and is about {self.subject}.")


    def __str__(self):
        return f"{self.name} - {self.subject} - {self.date} with the instructors {''.join(map(str,self.instructors))} and students{''.join(map(str,self.students))}"


workshop1 = Workshop('Workshop1', 'Today', 'Subject')

workshop1.add_participant(keith)

print(workshop1)

