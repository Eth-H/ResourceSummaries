# intro
XDG MIME Applications
    builds on #Shared MIME database and #Desktop entries to provide default applications

stores defautls in mimeapps.list
    ~/.config/mimeapps.list 	user overrides
    /etc/xdg/mimeapps.list 	system-wide overrides
    ~/.local/share/applications/mimeapps.list 	(deprecated) user overrides
    /usr/local/share/applications/mimeapps.list
    /usr/share/applications/mimeapps.list 	distribution-provided defaults 
format
    [Added Associations]
    image/jpeg=bar.desktop;baz.desktop
    video/H264=bar.desktop
    [Removed Associations]
    video/H264=baz.desktop
    [Default Applications]
    image/jpeg=foo.desktop

# edit mine db
## create new mime type
This example defines a new MIME type application/x-foobar and assigns it to any file with a name ending in .foo. Simply create the following file:
    ~/.local/share/mime/packages/application-x-foobar.xml
        <?xml version="1.0" encoding="UTF-8"?>
        <mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
            <mime-type type="application/x-foobar">
                <comment>foo file</comment>
                <icon name="application-x-foobar"/>
                <glob-deleteall/>
                <glob pattern="*.foo"/>
            </mime-type>
        </mime-info>
    And then update the MIME database:
        update-mime-database ~/.local/share/mime

# use deafult app related to filetype
    //xdg-open resource opener
        xdg-open [file | URL]

# manage mime deafult apps
    //Determine a file's MIME type:
        xdg-mime query filetype photo.jpeg
            image/jpeg
    //Determine the default application for a MIME type:
        xdg-mime query default image/jpeg
            gimp.desktop

    //Change the default application for a MIME type:
        xdg-mime default org.pwmt.zathura.desktop application/pdf
        xdg-mime default sxiv.desktop image/jpg
        xdg-mime default sxiv.desktop image/png

    //Shortcut to open all web MIME types with a single application:
        xdg-settings set default-web-browser firefox.desktop

    //Shortcut for setting the default application for a URL scheme:
        xdg-settings set default-url-scheme-handler irc xchat.desktop
