class Student:
    def __init__(self,name):
        self.name=name
        self.grade=[]
    def add_grade(self,grade):
        self.grade.append(grade)
    def avg(self):
        if not self.grade:
            return 0
        return sum(self.grade)/len(self.grade)
    def letter_grade(self):
        avg=self.avg()

        if avg>=90:
            return 'A'
        elif avg>=75:
            return 'B'
        elif avg>=60:
            return 'C'
        else:
            return 'F'
        
    def report_card(self):
        print(f'student name:{self.name}')
        print(f'student grade:{self.grade}')
        print(f'student avg:{self.avg():.1f}')
        print(f'grades:{self.letter_grade()}')

s1=Student('hero')
s1.add_grade(76)
s1.add_grade(34)
s1.add_grade(66)
s1.report_card()
    
        