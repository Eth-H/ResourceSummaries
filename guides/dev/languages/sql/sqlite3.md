# sqlite prompt cmds
    //list
        .databases
        .tables

    //db metadata
        .dbinfo [dbName]
    //get creation script[s]
        .schema [DbOrTableName]

    //move tables across dbs (despite primary keys) using dumps
    //dump table
    sqlite3 old_db.sqlite
    sqlite> .output mytable_dump.sql
    sqlite> .dump my_table
    sqlite> .quit
    //Read the dump into the new_db.sqlite assuming the table there does not exist
    sqlite3 new_db.sqlite
    sqlite> .read mytable_dump.sql

# sqlite prmopt SQL
    //open db
        attach "mydb.sqlite" as db1;
    //merge databases
    attach './KoreanDrama.db' as toMerge;           
    /* BEGIN; */
    insert into Manga select * from toMerge.series; 
    COMMIT; 
    detach toMerge;

    //get columns
        SELECT name FROM PRAGMA_TABLE_INFO('tableName');

        PRAGMA table_info('tableName')


    insert into Cartoons.Manga select * from Manga.Manga;
