# rg

> better grep

- smart case, ignore case
    rg -S ""
    rg -i ""
- file glob
    rg "" -g "/*/*"

- context lines, after, before
    rg -A 2
    rg -B 2

- fixed string (dont have to escape regex chars)
    rg -F ""

- sort ascending, descending
    rg "" --sort [nan, path, modifited, accessed, created]
    rg "" --sortr

- is something found or not
    rg -q ""
