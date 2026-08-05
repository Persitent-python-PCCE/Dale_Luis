li=[12,5,8,20,3,15,22]
total=sum(li)
a=total/7
print(a)
print(total)
dicti = {
   0:'8AM',
   1:'9AM',
   2:'10AM',
   3:'11AM',
   4:'12PM',
   5:'1PM',
   6:'2PM'
}
print(f"Total: {total} cups | Average: {a:.1f}/hr")
print('Rush hours(above average):')
for i in range(len(li)):
   if li[i] > a:
       print(dicti[i])