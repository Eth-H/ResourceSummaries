# xclip

> interact with x clipboard

- primary / x11 primary area
xclip -o [-selection primary | -selection p]? 
- use secondary / x11 secondary area
xclip -o -selection [secondary|sec]
- use system clipboard
xclip -o -selection [clipboard|clip]

- also print out
xclip -o -selection p -f

- strip newline, 
xclip -o -selection p -r

- specify specify type of data, eg image
xclip -sel clip -t image/png input_file.png
