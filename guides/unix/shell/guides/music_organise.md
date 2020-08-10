# beets
    pip3 install beets
## config
    https://beets.readthedocs.io/en/stable/reference/config.html
    beets config -p
        ~/.config/beets/config.yaml
    beets config -e

    directory: pathToMusicDir
    library: pathToDbFile
    plugins: a b c
    //replace items in imported files, noramlly truncate spaces
    replace:
        'regex': _
    import: //options with beet import
        write: yes/no //metadata written
        copy: yes/no //cp files into lib dir
        move: yes/no //mv files into lib dir, override copy
        link: yes/no //sym link files in lib dir
        resume: yes/no/ask //resume interrupted
    incremental: yes/no //if skipped dirs are recorded
    group_albums: yes/no //groups mported tracks into albums based on the dirs they reside in
    set_fields: //fields to set vals whe importing
        genre: 'To Listen'
        collection: 'Unordered'
    match: //settings when searching musicbrainz for audio metadata
        required: genre year label
        
    paths: //format stored file paths
        //via special paths and metdata fields, default: most, comp: various artist, singeton: non-album
        default: $albumartist/$album%aunique{}/$track $title
        singleton: Non-Album/$artist/$title
        comp: Compilations/$album%aunique{}/$track $title
        //via query
        albumtype:soundtrack: Soundtracks/$album/$track $title


## queries
https://beets.readthedocs.io/en/stable/reference/query.html
    albumkeyword1 albumkw2, artist1kw3 artist2kw4
    field:value
    field::regex
    :value //search all fields with regex
    1990..1999 //numeric range

## cmds
    beet import [path]
    beet ls [queryStr]
    beet stats

## plugins
### Chromaprint/Acoustid
    need gstreamer or ffmpeg
    sudo apt-get install apt-get install python-gst0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-bad gstreamer0.10-plugins-ugly
    pip3 install pyacoustid
    beet fingerprint [musicFile]
    beet import [musicWithNoTags]

    chroma:
        auto: yes //fingerprint in import process
### fromfilename
    guess tags from filename
    if fingerprinting or current tags dont dientify song
    choosing fallback options (Use as is, Track) will trigger it
### edit
    edit music metadata from $EDITOR
    beet edit [query]
### fuzzy finding lbrary
    beet ls '~query'
    threshold: 0.7  //sensitiviety, 1 perfect match, 0 everything
    prefix: ~ //change trigger prefix
### types 
    custom declare types
    types:
        rating: int
    beet modify "My favorite track" rating=5
    beet ls rating:4..5
### bpd
    mpd client
    apt install python-gi gstreamer1.0
    beet bpd
    bpd:
        host: 127.0.0.1
        port: 6600
        password: seekrit
        volume: 100
### lastgenre
    MusicBrainz database does not contain genre info
    fetch tags from last.fm
    pip install pylast
    lastgenre: 
       auto: yes
    whitelist: //allowed genres
        rock //allow sub genres of rock converted to rock
        african
        asian
        blues
        classical
        comedy
        country
        electronic
        hip hop
        jazz
        pop
        reggae
https://raw.githubusercontent.com/beetbox/beets/master/beetsplug/lastgenre/genres-tree.yaml
    beet lastgenre [query]
### web
    web client and server
### fetchart
    get cover art for an album and save as cover.jpg
    sources- local fs->Cover Art Archive->iTunes Store->Amazon->AlbumArt.org
    Google custom search- need to setup with api key
    pip3 install requests
    fetchart:
        auto: yes/no
        sources:
            - filesystem
            - coverart: release
            - itunes
            - coverart: releasegroup
            - '\*'
            - google
            - fanarttv
    google_key: [apiKey]
    fanarttv_key: [apiKey]
    beet fetchart [query]
plugins: chroma fromfilename edit fuzzy
