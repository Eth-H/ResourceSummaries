# geany
## source links
    https://www.geany.org/manual/#custom-filetypes
    https://www.geany.org/manual/#filetype-extensions
    https://www.geany.org/manual/#lexer-filetype
    https://www.geany.org/manual/#special-file-filetypes-common
## path
    ~/.config/geany/filedefs
    /usr/share/geany/filedefs
		
## shell
	Custom languages
		recognise filetype
			add to Tools->Configuration Files->filetype_extensions.conf
		create config for that specific filetype
			//Creating a custom filetype from an existing filetype (otherwise just create the file)
				cd /usr/share/geany/filedefs
				cp filetypes.foo filetypes.Bar.conf
			//or to override an existing filetype create file in current user
				cd ~/.config/geany/filedefs
				
				
## setup config
    quick setup
        styles 
            Using an existing syntax highlighting lexer (lexer_filetype key).
            Using an existing tags parser (tag_parser key).
        settings
            extension=py
            comment_single=//

        build options
            add needed commands
        Loading global tags files (sharing the tag_parser filetype's namespace).	
    
    full setup
        styling (syntax highlighting)
            key=foreground_color;background_color;bold_flag;italic_flag
            colors
                RGB hex values prefixed by 0x, EG red == 0xff0000, 0xf00, #ff0000, or #f00
            use defaults
                key=0xff0000;;true
            reference named style (in filetypes.common)
                key=named_style, key2=named_style2,bold,italic
            read styles from anouther filetype (also set lexar_filetype=Foo)
                [styling=Foo]
        keywords
            add keyword list specific to filetype
            EG 	primary=False None True and as assert break class continue def del elif else except 
                identifiers=ArithmeticError AssertionError AttributeError BaseException BlockingIOError 
            
        settings
            extension: need to match filetype_extensions.conf
            comment_single, comment_open, comment_close
            comment_use_indent: =true is #command_example();, =false is #	command_example();
            lexer_filetype: use to setup syntax highlighting from anouther file type, should be filetypes.name capitialised, lexer_filetype=Foo 
                
            context_action_cmd: command can be executes at current word/selection, %s inserts selected content,  EG context_action_cmd=devhelp -s "%s"
        indentation
            width (forced indentation width), type (forced indentation type), =0 for spaces only, =1 for tabs only, =2 for mixed 
        build menu (generally overrided by geany.conf user preferences build-menu options)
            compiler (can also run interpretor)
                %f -- complete filename without path, %e -- filename without path and without extension
                EG compiler=gcc -Wall -c "%f
            linker	
                EG linker=gcc -Wall "%f"
            run_cmd
                %e = exe name
                EG run_cmd="./%e"
