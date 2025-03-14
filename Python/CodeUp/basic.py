
print("\'Hello\'")

print("\"!@#$%^&*()\'")

print("\"C:\Download\\'hello\'.py\"")

print(r'print("Hello\nWorld")')

a = input()
b = input()
print(b)
print(a)

num = input()
print(num + "\n" + num + "\n" + num)

a, b = input().split()
print(int(a))
print(int(b))

a, b = input().split()
print(b, a)

a, b = input().split(':')
print(a, b, sep=':')

y, m, d = input().split('.')
print(d, m, y, sep="-")

left, right = input().split("-")
print(left + right)

st = input()
for s in st:
  print(s)

date = input()
print(date[:2], date[2:4], date[4:])

HH, MM, SS = input().split(':')
print(MM)

a = input()
n = int(a, 16)
print('%o' %n)

print(ord(input()))

print(chr(int(input())))

s = ord(input())
print(chr(s + 1))

num = int(input())
s = input()
print(s * num)

a, b = input().split()
print(float(a) ** float(b))

a = float(input())
print(format(a, '.2f'))

a, b = input().split()
print(format(float(a)/float(b), '.3f'))

a, b = input().split()
print(True if a == b else False)

a, b = input().split()
print(True if int(a) < int(b) else False)

a, b = input().split()
print(True if int(a) <= int(b) else False)