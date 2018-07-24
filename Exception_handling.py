def main():
    # exception handling statement
    try:
     if a[0][0] == 'S' and a[1][0] == 'M' and a[2][0] == 'K' and a[3][0] == 'J':
         print("This List belongs to my friends name:")
     #this is the code which is executed if the above statement comes to be false
    finally:
     if a[0][0] == 'S' and a[1][0] == 'M' and a[2][0] == 'K' and a[3][0] == 'K':
         print("This List does not belongs to my friends name:")
#this is the list whose elements are to be compared in the loop
a = ['Sanpreet Singh','Manpreet Singh','Kuldeep Singh','KashanPreet Singh']
#running the main function in  this way also
if __name__ == "__main__":
     main()
