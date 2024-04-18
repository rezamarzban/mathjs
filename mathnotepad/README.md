#### Math Notepad 

Powered by `mathjs`, It is client side web based MATH app with JavaScript (WIP)

Navigate your browser to `https://mathnotepad.com` or use this repository contents (some functions only works at original webpage).

Usage: Download single `MathNotepad.html` from `merged` dir and open it with any browser, Then use it by writing your math codes.

Example:
```
dipole_length = 0.1; 
I = 2; 
K = (2 * pi / 6); 
r = 1000; 
n = 360; 
theta = 0:pi/n:pi; 
E_theta = ((1i * K * I * dipole_length * 377 ) / (4 * pi * r)) * sin(theta) * exp(-1i * K * r); 
H_phi = E_theta / 377; 
S_theta = 0.5 * re(E_theta .* conj(H_phi)); 
P_rad = (pi/n) * sum(S_theta * sin(theta) * r^2) * 2 * pi
Rr = 2 * P_rad / I^2
```

This example calculate radiated power and radiation resistance of a sample short dipole antenna from poynting vector and farfield radiation electricity field at `Math Notepad` web page.

#### merge

With `merge.py` script, All html, js, css files will be merged into single html file. The single html file from running this script is at `merged` dir.
