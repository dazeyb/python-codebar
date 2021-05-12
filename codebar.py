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
        return f"{self.full_name} - {self.reason}\n"



class Instructor(Member):
    # aka constructor
    def __init__(self, full_name, bio, skills=''):
        super().__init__(full_name)
        self.bio = bio
        self.skills = skills
 


    def add_skill(self, skill):
        # self.skills = self.skills.append(skill)   This doesn't work
        # self.skills.append(skill)
        self.skills = self.skills + ' ' + skill + ' '


    
    def __str__(self):
        return f"{self.full_name} - {self.skills}\n{self.bio}\n"

# keith = Student("Keith", "Loves codin")
# print(keith)
 


class Workshop:
    def __init__(self, date, subject, instructors=[], students=[]):
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
        print(f"Workshop - {self.date} - {self.subject} \n\n Students \n {''.join(map(str,self.students))} \n\n Instructor \n{''.join(map(str,self.instructors))}")


    def __str__(self):
        return f"{self.name} - {self.subject} - {self.date} with the instructors {''.join(map(str,self.instructors))} and students{''.join(map(str,self.students))}"


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
