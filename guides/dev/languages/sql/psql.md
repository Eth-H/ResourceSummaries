# setup
    sudo apt install postgresql		
    //Only postgres user can run psql
        //Change password
            sudo -u postgres psql postgres
            \password postgres
        //or
            sudo passwd postgres
    su postgres
## login to db
    //Drop to psql shell
        psql postgres
    //Login with user to localhost
        psql -U postgres -h localhost
        [password]
    //Create a new user
        psql create user bob with password "mypass";

# manage DB content
    //Ouside prompt
        //List DB
            psql -l	
    //Activate psql prompt
        psql
        //Dealing within databases	
        //Create schema
            psql create schema friends
        //Create table
            psql create table friends.test( firstname CHAR(15), lastname CHAR(20));
        //Select stuff
            psql select * from friends.test;
    //Insert data 
        psql insert into friends.test values('Mile', 'Smith');
        
# Create DB with createdb
    //Use default DB server
        createdb demo
    //Custom port, host, encoding 
        createdb -p 5000 -h eden -E LATIN1 -e demo
    
# example table creat statement
psql create table public.CustomerData ( id serial PRIMARY KEY, CustomerID VARCHAR, Pets_Name TEXT, CurrentDate date, Animal TEXT, DoB date, Breed TEXT, Male INTEGER, Female INTEGER, Colour TEXT, Owner TEXT, Address TEXT, Mobile TEXT, Email TEXT, MicrochipNumber TEXT, Tattoo_Location TEXT, Neutralised_B INTEGER, VET_Name TEXT, VET_Mobile TEXT, EmergencyContactName TEXT, EmergencyContactRelationship TEXT, EmergencyContactMobile TEXT, PreferencesDislikesY INTEGER, PreferencesDislikes TEXT, PreferenceLikesY INTEGER, PreferencesLikes TEXT, Shampoo TEXT, SheerNumberInWinter TEXT, SheerNumberInSummer TEXT, OtherUsefulDetails TEXT, Fleas INTEGER, Mite INTEGER, Worms INTEGER, Ticks INTEGER, Lice INTEGER, Mange INTEGER, Cough INTEGER, Long worm INTEGER, OtherContagiousOptions INTEGER, Heart INTEGER, Sight INTEGER, Ears INTEGER, Balance INTEGER, A.glandis INTEGER, Ringworm INTEGER, Hip. Dysp INTEGER, Eczema INTEGER, Allergies INTEGER, Arthritis INTEGER, Diabetes INTEGER, Incontinence INTEGER, Warts INTEGER, Shy INTEGER, Good INTEGER, Noisy INTEGER, Fights INTEGER, Soils/waste INTEGER, Escapes INTEGER, Highly strung INTEGER, Bite INTEGER, Muzzule INTEGER, Climbs INTEGER, Chewy INTEGER, OtherBehaviourOption INTEGER, BehaviourNotes TEXT, HealthNotes TEXT);
            
# other
## win setup
    https://www.postgresql.org/docs/9.6/auth-pg-hba-conf.html
    /etc/postgresql/10/main/
    //Further setup steps
        //Make accessable to console ()
        //Add C:\Program Files\PostgreSQL\10\bin to systems path

        //modify the pg_hba.conf to add authentication for new database
            //Reload config files
                service postgresql reload
## Depreciated
    //DB management
        //Create database
            psql create database mydb;
        //Delete database
            psql drop database mydb;

# psql prompt cmds
from prompt can enter SQL directly or use \[x] flag
## List DB
        \l
    //Get DB info (including datatypes)
        \d [tableName]
    //Connect to a database
        \c mydb;
    //Get info on teh connection
        \conninfo
    //Execute terminal command
        \! [terminalCommandSyntax]
    //Change DB password (for connections outside terminal (EG NodeJS))
        //Connect to database then run
        ALTER USER postgres PASSWORD 'newPassword';
## Check out contents of table
    \d friends.test

