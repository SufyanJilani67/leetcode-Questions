class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        j=0
        length=len(students)
        while j != length:
            if(students[0]==sandwiches[0]):
                j=0
                students.pop(0)
                sandwiches.pop(0)
            else:
                j+=1
                temp=students.pop(0)
                students.append(temp)
            if j == len(students):
                break
            
        return len(students)