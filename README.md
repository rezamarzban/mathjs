# mathjs
Mathjs and Math Notepad are powered by `mathjs.org` (basic MATLAB in JavaScript)

The `mathjs` doesn't need any software to be installed, It only need a web browser.

example1:

```
a = 1
b = 20
n = 1000
h = (b-a)/n
x = a:h:b;
y = x.^2;
integral = (h * sum(y)) - ((h/2) * (y[1] + y[n]))
```

This example calculate integral of x² dx from a=1 to b=20 by trapezoidal rule (n=1000). The output will be:

```
1
20
1000
0.019
2666.3416930705
```

example2:

```
a =  1;
b = 1000;
n = 100000;
h = (b-a)/n;
x = a:h:b;
y = (e.^(-1i*x))./x;
integral = (h * sum(y)) - ((h/2) * (y[1] + y[n]))
```

This example calculate integral of complex exp(-1i*x)/x dx from a=1 to b=1000 (large number is equal to infinity approximately at numerical method) by trapezoidal rule (n=100000). The output will be:

```
-0.33657178190801 - 0.62414432869794i
```
