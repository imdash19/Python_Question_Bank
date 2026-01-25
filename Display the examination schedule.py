# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output: The examination will start from: 11 / 12 / 2014

exam_st_date= [val for val in input('Please enter your date separated with comma: ').split(',')]
print('='*60)

if len(exam_st_date)>2:
    dt= exam_st_date[0]
    for i in range (1, len(exam_st_date)):
        dt= '/' + exam_st_date[i]
    print(dt)

else:
    print("Invalid date")