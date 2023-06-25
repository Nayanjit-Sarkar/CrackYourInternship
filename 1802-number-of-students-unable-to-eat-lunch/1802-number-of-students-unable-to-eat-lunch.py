class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c,l = 0,len(students)
        while c!=l:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                c,l = 0,len(students)
            else:
                students.append(students.pop(0))
                c+=1
        return l
                
