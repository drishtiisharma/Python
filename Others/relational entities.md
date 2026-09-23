
```sql
/* 
RELATIONAL SCHEMA DESIGN SKETCH
=================================
1. TABLE: STUDENTS
   ------------------------------
   - student_id       [PRIMARY KEY]
   - first_name       
   - last_name        
   - email            

2. TABLE: COURSES
   ------------------------------
   - course_id        [PRIMARY KEY]
   - course_title     
   - credits          

3. TABLE: ENROLLMENTS (Junction Table)
   -----------------------------------
   - enrollment_id    [PRIMARY KEY]
   - student_id       [FOREIGN KEY -> references STUDENTS(student_id)]
   - course_id        [FOREIGN KEY -> references COURSES(course_id)]
   - grade            
   - enrollment_date  

===================================================================
RELATIONSHIP SUMMARY:
- STUDENTS to ENROLLMENTS : 1-to-Many (1:N)
- COURSES to ENROLLMENTS  : 1-to-Many (1:N)
- STUDENTS to COURSES     : Many-to-Many (M:N) resolved via ENROLLMENTS
===================================================================
*/
```

#### Diagram

[Diagram](https://i.ibb.co/Xf3RkGw0/relational-entities.png)
