# sqlite prompt cmds
    //list
        .databases
        .tables
        //sqlite prompt settings
            .show

    //db metadata
        .dbinfo [dbName]
    //get creation script[s]
        .schema [DbOrTableName]
    //open db
        //from cli
            sqlite3 old_db.sqlite
        //from prompt
            attach 'mydb.sqlite' as 'db1';

# reading/outputting to filesystem
## sql text files
    //this will store the data as the sql statements used to create it
        //set output file (instead of stdout)
            .output mydump.sql
            //set back to screen output
                .output stdout
        //dump entire db
            .dump
        //dump specifc table
            .dump tableName
        //dump structure only
            .schema
        //dump data only
            .mode insert //apply before setting output
            //now all sql select statements converted to insert statments
            select * from table;
        //read dump back into sql (will execute sql within file)
            .read mydump.sql
## data files
    //import data from a file
        //file can match any of the modes from .mode
        .import file
    //output data to non-sql file type
        csv: Comma-separated values
        column: Left-aligned columns.
        html: HTML <table> code
        insert: SQL insert statements for TABLE
        line: One value per line
        list: Values delimited by .separator string
        tabs: Tab-separated values
        tcl: TCL list elements
        .mode {}
        .ouput file
    //EG convert data file to sqlite file
        .mode csv
        .import OutlineTable.csv Cartoons
        .output fileName
        .save output.db //?
