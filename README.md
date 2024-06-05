# Z-value
Calculate the significance (Z-value) from the p-value.

Simple code which saves using those confusing Z-value tables at the back of your stats book.

Code will also produce plot, which can be disabled by commenting "plt.show()", although this makes an excellent teaching tool in numerical intergration. Just set npts = 100 for a demonstration.

Only accurate to p > 1e-5 [Z < 4.1σ], otherwise use (the much faster) C version  at https://github.com/steviecurran/Z-value
