Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello,World')
Hello,World
>>> 42*60+42
2562
>>> 10/1.61
6.211180124223602
>>> (42+42/60)/10
4.2700000000000005
>>> (42*60+42)/10#跑1km需要的秒数
256.2
>>> 10/(2562/3600)#平均速度(多少千米每小时)
14.05152224824356
>>> #第二章节
>>> #练习2-1
>>> >>> print(1)
x=2
print(x)
SyntaxError: invalid syntax
>>> print(1)
x=2
print(x)
SyntaxError: multiple statements found while compiling a single statement
>>> x=2
>>> print(2)
2
>>> print(1)
1
>>> print(1)
1
>>> print(1)x=2 print(2)
SyntaxError: invalid syntax
>>> 5
5
>>> 2
2
>>> 
>>> n=42
>>> print(n)
42
>>> 42=n
SyntaxError: cannot assign to literal
>>> n=42;n+1
43
>>> n=1;Print(n+3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    n=1;Print(n+3)
NameError: name 'Print' is not defined
>>> n=1;print(n+3)
4
>>> n=1;x=3;y=8;(n+x)/y
0.5
>>> n=1,x=3,y=8,(n+x)/y
SyntaxError: cannot assign to literal
>>> n=1.x=3.y=8.(n+x)/y
SyntaxError: invalid syntax
>>> x=2;y=4;xy
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x=2;y=4;xy
NameError: name 'xy' is not defined
>>> x=2;y=4;x*y
8
>>> #第二章练习2-2
>>> r=5;v=(4/3)pir***3
SyntaxError: invalid syntax
>>> import math
>>> math.pi
3.141592653589793
>>> #2-2-1
>>> r=5;v=(4/3)math.pi*r**3
SyntaxError: invalid syntax
>>> r=5;v=(4/3)pi*r**3
SyntaxError: invalid syntax
>>> pi=math.pi
>>> 3*pi
9.42477796076938
>>> r=5;v=(4/3)pi*r**3
SyntaxError: invalid syntax
>>> r=5;v=(4/3)*pi*r**3
>>> print(v)
523.5987755982989
>>> 上面2-2-1的答案
SyntaxError: invalid syntax
>>> #上面2-2-1的答案
>>> #2-2-2
>>> 24.95*0.6+3+59*0.75
62.22
>>> #2-2-3
>>> 1.6*(6*60+10)*2+(4*60+30)*4.8
2480.0
>>> 2480/60
41.333333333333336
>>> 41+52
93
>>> 93-60
33
>>> 33#7:33:
33
>>> 2480-41*60
20
>>> #答案是：7:33:20