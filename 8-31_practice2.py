grade1 = input("enter your first grade:")
grade2 = input("enter your second grade:")
grade3 = input("enter your third grade:")

Total = (grade1 + grade2 + grade3)
percentile = (Total/300)*100

if percentile < 100 and percentile >=90:
    print("Grade A")
elif percentile < 90 and percentile >=80:
    print("Grade B")
elif percentile < 80 and percentile >=70:
    print("Grade C")
elif percentile < 70 and percentile >=60:
    print("Grade D")
elif percentile < 60 and percentile >=50:
    print("Grade f")



for i in range(1, 50 ,2):
    print(i)
