#felt it was more inclined to medium than easy. if easy score is 1 and medium score is 2 then the problem lies somewhere 1.8

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        run=True
        while run<2:
            ter=len(sandwiches)
            for i in range(len(sandwiches)):
                if students[0]==sandwiches[0]:
                    sandwiches=sandwiches[1:]
                    students=students[1:]
                    run =0
                    break
                else:
                    toRight=students[0]
                    students=students[1:]
                    students.append(toRight)
            if sandwiches == []:
                return 0
            if i==ter-1:
                run+=1
        return len(sandwiches)
