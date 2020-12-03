# setup
    sudo apt install weechat-curses
- get vim keybindings
    /script install vimode.py
    - if keybindings err run
        /vimode bind_keys
    - if using tmux/screen
        tmux set-option escape-time 0 //script
        set -sg escape-time 0 //.tmux.conf
    - config
        /fset weechat.bar.input.items -> s -> "mode_indicator+[input_prompt]+(away),[input_search], [input_paste],input_text,[vi_buffer]" 
        /fset weechat.bar.status.items -> s -> "[time],[buffer_last_number],[buffer_plugin],buffer_number+:+buffer_name+(buffer_modes)+{buffer_nicklist_count}+buffer_zoom+buffer_filter,scroll,[lag],[hotlist],completion,cmd_completion"
        /set plugins.var.python.vimode.search_vim on

# terms
    server: irc server
    channel: specific chat room on a server
    nickserv: serverside software pernament nick that identifies you
    each chat is a buffer
    each split within a buffer is a window

# guide, setup freenode server
- tmp add server and conn, prob disabled
    /connect chat.freenode.net
- perm add server
    /server add freenode chat.freenode.net
    /connect freenode
- server specific setup
    /set irc.server.freenode.nicks 
    /set irc.server.freenode.username "My user name"
    /set irc.server.freenode.realname "My real name"
    - autojoin server or channel
        /set irc.server.freenode.autoconnect on
        /set irc.server.freenode.autojoin "#channel1,#channel2"
    - ssl, if server supports
        /set irc.server.freenode.addresses "chat.freenode.net/6697"
        /set irc.server.freenode.ssl on
    - sasl identification, freenode, some servers neccessary
        - register nickname with 
            /msg NickServ REGISTER <password> <email>
            //check email and run register confimation cmd
        - mention account on next login, if not set in config
            /connect chat.freenode.net 6667 <nick>:<password>
        - set registered sasl acc for a server
            /set irc.server.freenode.sasl_mechanism PLAIN
            /set irc.server.freenode.sasl_username <nickname>
            /set irc.server.freenode.sasl_password <password>
            /save
# cmds
    /nick nickname
    /join #ubuntu,#kde
    - mv open channel
        alt arrow
    - pm in channel
        nickname: msg
    - pm direct
        /query nickname
        /close

    /set config.option.value
    /fset weechat.*

# keys
- scroll bar
    F9 F10
- scroll users
    F11 F12

# vi mode cmds
    all /cmds
    :h -> /help
    :q -> /close
    :qa -> /exit
    :w -> /save
    :bn, :bN or :bp
    :bd, :b#
    :b [N]
    :sp :vs -> /window splith, /window splitv
    :!{cmd} -> /exec -buffer shell
    :s/pattern/repl/g 
    :<num>
    :nmap, :nmap {lhs} {rhs}
        <Up>, <Down>, <Left>, <Right>, <C-...> and <M-...>
    :nunmap {lhs} //rm mapping



mode.py] Problematic keybindings detected:
[vimode.py]     meta-jmeta-f -> /buffer -
vimode.py][     meta-jmeta-l -> /buffer +
[vimode.py]     meta-jmeta-r -> /server raw
vimode.py][     meta-jmeta-s -> /server jump
vimode.py][     meta-wmeta-meta2-A -> /window up
vimode.py][     meta-wmeta-meta2-B -> /window down
[vimode.py]     meta-wmeta-meta2-C -> /window right
[vimode.py]     meta-wmeta-meta2-D -> /window left
vimode.py][     meta-wmeta2-1;3A -> /window up
[vimode.py]     meta-wmeta2-1;3B -> /window down
[vimode.py]     meta-wmeta2-1;3C -> /window right
vimode.py][     meta-wmeta2-1;3D -> /window left
vimode.py][     meta-wmeta-b -> /window balance
vimode.py][     meta-wmeta-s -> /window swap
[vimode.py] These keybindings may conflict with vimode.
[vimode.py] You can remove problematic key bindings and add recommended ones by using /vimode bind_keys, or only list them with /vimode bind_keys --list
[vimode.py] For help, see: https://github.com/GermainZ/weechat-vimode/blob/master/FAQ.md#problematic-key-bindings

[vimode.py] tmux/screen users, see: https://github.com/GermainZ/weechat-vimode/blob/master/FAQ.md#esc-key-not-being-detected-instantly

[vimode.py] To force disable warnings, you can set plugins.var.python.vimode.no_warn to 'on'
re] 1:weechat
'']]]]]]]]]]]]]]]]]]]

│13:27:55     | Key "ctrl-W" unbound (context: "default")
│13:27:55     | New key binding (context "default"): ctrl-W => /input delete_previous_word
│13:27:55     | New key binding (context "default"): ctrl-^ => /input jump_last_buffer_displayed
│13:27:55     | New key binding (context "default"): ctrl-Wh => /window left  
│13:27:55     | New key binding (context "default"): ctrl-Wj => /window down
│13:27:55     | New key binding (context "default"): ctrl-Wk => /window up
│13:27:55     | New key binding (context "default"): ctrl-Wl => /window right
│13:27:55     | New key binding (context "default"): ctrl-W= => /window balance
│13:27:55     | New key binding (context "default"): ctrl-Wx => /window swap
│13:27:55     | New key binding (context "default"): ctrl-Ws => /window splith
│13:27:55     | New key binding (context "default"): ctrl-Wv => /window splitv
│13:27:55     | New key binding (context "default"): ctrl-Wq => /window merge
│13:27:55     | Key "meta-jmeta-f" unbound (context: "default")
│13:27:55     | Key "meta-jmeta-l" unbound (context: "default")   
│13:27:55     | Key "meta-jmeta-r" unbound (context: "default")
│13:27:55     | Key "meta-jmeta-s" unbound (context: "default") 
│13:27:55     | Key "meta-wmeta-meta2-A" unbound (context: "default")
│13:27:55     | Key "meta-wmeta-meta2-B" unbound (context: "default")
│13:27:55     | Key "meta-wmeta-meta2-C" unbound (context: "default")
│13:27:55     | Key "meta-wmeta-meta2-D" unbound (context: "default")
│13:27:55     | Key "meta-wmeta2-1;3A" unbound (context: "default")
│13:27:55     | Key "meta-wmeta2-1;3B" unbound (context: "default")
│13:27:55     | Key "meta-wmeta2-1;3C" unbound (context: "default")
│13:27:55     | Key "meta-wmeta2-1;3D" unbound (context: "default")
│13:27:55     | Key "meta-wmeta-b" unbound (context: "default")
│13:27:55     | Key "meta-wmeta-s" unbound (context: "default")
│13:27:55     | Done.

# links
    https://github.com/GermainZ/weechat-vimode
    https://github.com/GermainZ/weechat-vimode/blob/master/FAQ.md#esc-key-not-being-detected-instantly
    https://weechat.org/files/doc/stable/weechat_quickstart.en.html
    https://freenode.net/kb/answer/registration
    https://freenode.net/kb/answer/weechat
    support@freenode.net
