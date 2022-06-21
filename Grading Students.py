''' HackerLand University has the following grading policy:

   1. Every student receives a grade in the inclusive range from 1 to 100.
   2. Any grade less than 30 is a failing grade. 

    
Sam is a professor at the university and likes to round each student's grade according to these rules:

  1.If the difference between the grade and the next multiple of 5 is less than 3 , round up to the next multiple of 5.
  2.If the value of grade  is less than 38 , no rounding occurs as the result will still be a failing grade.

Examples
  1. grade = 84 round to85 (85 - 84 is less than 3)
  2. grade = 29 do not round (result is less than 40)
  3. grade = do not round (60 - 57 is 3 or higher) 
  '''
  
  #Passed through all test cases */
  
  #Python
  
  def gradingStudents(grades):
    # Write your code here
    grades=[int(i) for i in grades]
    for i in range (len(grades)):
        if grades[i]>=38:
            if (((((grades[i]//5)+1)*5)-grades[i])<3):
                grades[i]=5*((grades[i]//5)+1)
                print(grades[i])
    return grades
  
 
  
  
