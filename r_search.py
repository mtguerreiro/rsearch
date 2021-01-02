import numpy as np

# --- Input ---
R = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6,
     3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
     10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36,
     39, 43, 47, 51, 56, 62, 68, 75, 82, 91,
     100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360,
     390, 430, 470, 510, 560, 620, 680, 750, 820, 910,
     1000, 1100, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000,
     3300, 3600, 3900, 4300, 4700, 5100, 5600, 6200, 6800, 7500, 8200, 9100]

##f = lambda r1, r2 : r2/r1
##k = 1.066666666666666

f = lambda r1, r2 : r2 / (r1 + r2) * 9
k = 2.75

#f = lambda r1, r2 : (r2 / r1)
#k = 1.142857142857143
#k = 1.7142857142857144

# --- Search ---
n_f = f.__code__.co_argcount

r = np.array(R)
n_r = r.shape[0]

# For two parameters
if n_f == 2:
    kl = f(r.reshape(-1, 1), r)

# For three parameters
elif n_f == 3:
    kl = f(r.reshape(-1, 1, 1), r.reshape(1, -1, 1),r.reshape(1, 1, -1))

e = abs(k - kl) / k
i_r = np.unravel_index(np.argmin(e), e.shape)
    
# --- Output ---
print('R1: {:.1f}'.format(r[i_r[0]]))
print('R2: {:.1f}'.format(r[i_r[1]]))
if n_f == 3:
    print('R3: {:.1f}'.format(r[i_r[2]]))
print('Output: {:.2f}'.format(kl[i_r]))
print('Error: {:.2f} %'.format(100 * e[i_r]))

