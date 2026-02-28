# FILE NAME - grade_converter.py

# NAME: Jared Thibado
# DATE: 02/27/2026
# BRIEF DESCRIPTION:  code that coververts number grades to letter grades



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    #print("...")
    print("===== Grade Converter =====")
    number_grade = int(input("Enter a numerical grade (1-100): "))

    if   number_grade > 100:
            print("A+")
    elif number_grade >= 90 and number_grade <= 100:
            print("A")
    elif number_grade >= 80 and number_grade <= 89:
            print("B")
    elif number_grade >= 70 and number_grade <= 79:
            print("C")
    elif number_grade >= 65 and number_grade < 70:
            print("D")
    elif number_grade <= 64:
            print("F") 
    #print("...")
   
main()







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
Always check your less than and greater than signs to make sure they are correct. Just spent like 5 minutes trying to figure out why every 
grade was an A+. A simple mistake that is easy to miss when fixing your code.





'''
