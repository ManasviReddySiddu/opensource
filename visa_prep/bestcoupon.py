n=int(input())
d1=0.1*n
d2=100
max_discount=max(d1,d2)
final_amount=n-max_discount
print(int(final_amount))
