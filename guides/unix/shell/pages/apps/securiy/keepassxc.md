# keepassxc

> pw manager

- launch gui
    keepassxc

## withdraw pws
- get names of pws similar to SQ

    keepassxc-cli locate [pw_database_path] [searchQuery]
- return SQ pw details

    keepassxc-cli search [pw_database_path] [searchQuery]

## add
- username, pw prompt

    keepassxc-cli add -u -p [pw_database_path] [entryName]

- username, gen pw with certain length

    keepassxc-cli add -g -l [pw_length] [pw_database_path] [entryName]
