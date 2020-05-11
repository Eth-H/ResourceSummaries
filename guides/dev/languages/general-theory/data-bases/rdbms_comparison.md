# sql constraints
    UNIQUE: Applying this constraint to a column ensures that no two entries in that column are identical 
    NOT NULL: This constraint ensures that a column doesn’t have any NULL entries 
    PRIMARY KEY: A combination of UNIQUE and NOT NULL, the PRIMARY KEY constraint ensures that no entry in the column is NULL and that every entry is distinct 
    FOREIGN KEY: A FOREIGN KEY is a column in one table that refers to the PRIMARY KEY of another table  This constraint is used to link two tables together: entries to the FOREIGN KEY column must already exist in the parent PRIMARY KEY column for the write process to succeed 
    CHECK: This constraint limits the range of values that can be entered into a column  For example, if your application is intended only for residents of Alaska, you could add a CHECK constraint on a ZIP code column to only allow entries between 99501 and 99950 
    DEFAULT: This provides a default value for a given column  Unless another value is specified, SQLite enters the default value automatically 
    INDEX: Used to help retrieve data from a table more quickly, this constraint is similar to an index in a textbook: instead of having to review every entry in a table, a query only has to review entries from the indexed column to find the desired results 

# SQLite
serverless
## eval
    adv
        small footprint / lightweight: no external dependancies, <600Kb
        user-friendly: no config, no server (easy to integrate)
        portable: stored as one file (not across large batch of files)
    disadv (all non-server related)
        Limited concurrency: multiple concurrent process access/queries, but only one change at once, < server dbs
        no user management: access privallges limited to OS (dont fit different permission lvs)
        security: client bugs dont effect a server, easier to control data access to one persistent server process
        
    fits: embedded apps (portabliliy, no future expansions), disk access, testing
    dont fit: lots of data (<140TB but difficult to manage), high write volumes, network access to db (separate machines)

## data types
    null: NULL values
    integer: Signed ints, stored in one of 1-4,6,8 bytes relative to magnitude
    real: Real nums / floating point, stored as 8-byte
    text: Text strings, stored using the db encoding (UTF-8/UTF-16BE/UTF-16LE)
    blob: Any blob of data, each blob stored as inp

# MySQL
server daemon process
phpMyAdmin, DBeaver, HeidiSQL

## eval
    adv
        popular (docs, help) and easy to use, security (user management, security setup script), speed, replication(share info across hosts, fit backup and horizontall scaling)
    disadv
        limitations (lack sql compilance/features), licensing (has paid edition), slow dev
    fits: distributed sys, web apps, expected future db growth
    dont fit: good sql compilance, concurrency (read-writes bad)

## data types
### Numeric types
    tinyint: signed range -128 to 127,unsigned 0 to 255
    smallint: SR -32768 to 32767, UR 0 to 65535
    mediumint: SR -8388608 to 8388607, UR 0 to 16777215
    int/integer: SR -2147483648 to 2147483647, UR 0 to 4294967295
    bigint: SR -9223372036854775808 to 9223372036854775807, UR 0 to 18446744073709551615
    float: single-precision floating-point number
    double: double-precision floating-point number
    dec/decimal/fixed/numeric: packed fixed-point num, display length defiend by col
    bool/boolean: two possible vals
    bit: num of bits per val, 1 to 64
### Date and time types
    date: YYYY-MM-DD
    datetime: timestamp with date/time, YYYY-MM-DD HH:MM:SS
    timestamp: timestamp with time since the Unix epoch (00:00:00 on January 1, 1970)
    time: time of day, HH:MM:SS
    year: 2 or 4 digit format, 4 default
### String types:
    char: fixed-length str, right space padded to meet the specified length
    varchar: str variable length
    binary: char but a binary byte string (rather than nonbinary character string)
    varbinary: varchar but a binary byte string
    blob: binary str, max length 65535 (2^16 - 1) bytes
    tinyblob: blob, max length 255 (2^8 - 1) bytes
    mediumblob: blob, max length 16777215 (2^24 - 1) bytes
    longblob: blob, max length 4294967295 (2^32 - 1) bytes
    text: str, max length 65535 (2^16 - 1) chars
    tinytext: str, max length 255 (2^8 - 1) chars
    mediumtext: str, max length 16777215 (2^24 - 1) chars
    longtext: str, max length 4294967295 (2^32 - 1) chars
    enum: enumeration, str obj that takes a single value from a list of values that are declared when the table is created
    set: enumeration but >=0 values

# postgreSQL
server
obj-relational: also has table inheritance, func overloading, ...
implements MVCC: great concurrency and fits ACID

## eval
    adv
        sql compilance (>others), open source with community, extensible
    disadv
        mem performance (forks presses for new conns with max 10MB), popularity (<mysql)
    fit: data integrity, tool/langauge integration, complex operations (mutiple cpus,concurrency)
    dont fit: speed,short setup time,need replication support

## data types
### Numeric types
    bigint: signed 8 byte int
    bigserial: autoincrementing 8 byte int
    double precision: 8 byte double precision floating-point num
    integer: signed 4 byte int
    numeric/decimal: selectable precision num
    real: 4 byte single precision floating-point num
    smallint: signed 2 byte int
    smallserial: autoincrementing 2 byte int
    serial: autoincrementing 4 byte int
### char types
    character: char str with a specified fixed length
    character varying / varchar: char str with a variable but limited length 
    text: char str with variable unlimited length
### Date and time types
    date: day, month, and year 
    interval: time span 
    time / time without time zone: time of day not including the time zone
    time with time zone: time of day including the time zone 
    timestamp / timestamp without time zone: date and time not including the time zone 
    timestamp with time zone: date and time, including the time zone 
### Geometric types
    box: rectangular box on a plane 
    circle: circle on a plane 
    line: infinite line on a plane 
    lseg: line segment on a plane 
    path: geometric path on a plane 
    point: geometric point on a plane 
    polygon: closed geometric path on a plane 
### Network address types
    cidr: IPv4 or IPv6 network addr
    inet: IPv4 or IPv6 host addr
    macaddr: MAC addr
### Bit string types
    bit: fixed-length bit str
    bit varying: variable-length bit str
### Text search types:
    tsquery: text search query 
    tsvector: text search document 
### JSON types
    json: Textual JSON data 
    jsonb: Decomposed binary JSON data 
Other data types
    boolean: logical Boolean
    bytea: byte array, used for binary data
    money: amount of currency 
    pg_lsn: PostgreSQL Log seq num 
    txid_snapshot: user-level transaction ID snapshot 
    uuid: universally unique identifier 
    xml: XML data 
