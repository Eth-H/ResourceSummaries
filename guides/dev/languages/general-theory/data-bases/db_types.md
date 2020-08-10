# links
https://en.wikipedia.org/wiki/List_of_relational_database_management_systems
https://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems
https://en.wikipedia.org/wiki/Database_model
https://en.wikipedia.org/wiki/Comparison_of_structured_storage_software

# theory
## DB charateristics
    DB model
        RDBMS: database employing the relational management system
        nosql: simple database without relational features
    application programming interface
        sql (strucutered query language), used for most RDBMSs
        proprietary native APIs

    db architecture
        client-server: DBMS runs as a daemon, programs (clients) can send reqs
        serverless/in-process: DBMS runs as a process, generally embedded with an app
    db storage engine
        DBMS underlying software component used to actually store the database, generally flatfiles (text or binary)
        storage structures: used by DBSE to store info on disk, EG ordered/unordered flat files, ISAM, heap files, hash buckets, or B+ trees
        A DB needs to be embeddable to be used as a DBSE within a larger DBMS
        a DBSE may not have a DBMS and may just be a storage structure, EG csv files
    storage mode: in-mem, on-disk (embed), both
    Multiversion concurrency control (MCC, MVCC)
        concurrency control: ensures that correct results for concurrent operations are generated
        MCC: CC mtd used by DBMSs to provide concurrent DB access and PL transactional memory

## database model
    determines db locial structure and dtermines manner of CRUD operations
    model list
        //outdated
            hierarchical database
            network
        relational
            most use SQL data definition and QL
        realtional-obj
            relational but with an object-oriented db model: objects, classes and inheritance directly supported
        physical data model
            data design repersented as implemented
            inverted index
            flate file
                lack integrated indexes, built-in references between data elements, or complex data types
                tabular,csv,json,xml
                linear nosql dbs
        triplestore
            triple: subject-predicate-obj, EG bob is 35
            sql and nosql document based verions
        //nosql
            fits programming models, app layer does most processing
            main types -> sub-types/examples
                document
                key-value
                    key-val cache and key-val store EG Redis
                    consistent EG oracle nosql
                wide column EG Bigtable
                graph
                    as graph is more complicated generally have query lang
                    EG Oracle, SPARQL 1.1; Neo4j, Cypher
                ?
                    obj/object-oriented
                        
    multi-model database
        support multiple data models against a single integrated backend
            EG Redis

# database list
## DBMSs
    if multi-model db, first model is the most prominant
    name
        data model/s
        query lang
        arhictecture

    CouchDB: document
    ibm domino: document 
    Amazon DynamoDB: wide column
    Bigtable: wide column
    Cassandra: wide column
    HBase: wide column
    Neo4j: graph; Cypher
    Amazon Neptune: Gremlin, SPARQL

    CUBRID: relational
    Apache Derby: relational
    MariaDB: relational
    msaccess: relational
    mysql: relational; server
    sqlite: relational; local files

    Redis
        key-value, document (JSON), property graph, streaming, time-series 
        mainly key-val
    oracle database
        relational, document (json and xml), graph triplestore, property graph, key-value, objects
        oracle: relational
        oracle nosql: key-value, document; SPARQL 1.1 (graph QL)
        oracleDB: relational
    MongoDB
        document (XML and JSON), graph, key-value, time-series
        mainly document
    Couchbase: document (JSON), key-value; N1QL

    posgreSQL: obj-relational; server
    Microsoft SQL Server: obj-relational;

## db engines
    berkley DB: key-value; bad license, old, btree
    LMDB: key-value; api based off BDB, uses MVCC
    levelDB
        key-value; no concurrent access, string to string, uses fast snappy compression, btree;
        rocksDB: key-value; facebooks levelDB fork
    skipdb: key-value; skiplist
    shelve: python dictionary;
    csv: rows and cols;

# nosql
    generic db that doesnt use a relational sql model
    non-relational
        less complex and more flexible
            fits unstructured/semi-structured data
        schema-less: fits agile development
        horizontally scalable
            work well with clustered env (multiple computers perform task indepenatly)

    open source,  (), ,
    too flexible (leads to inconsistency)
        no predefined schema
        lack of adherence to acid principles
        no standard query language

## data types
    key val stores
        associative-arrays/dictionaries/hash-table
            attribute name/key and attribute/val
        adv: high performance,efficicent,scalable
        EG use: chaching, msg queuing,session management
        redis
            in-memory data store
            db, cache, msg broker
            supported data structures
                strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams
        memcached
            in-memory data store
            main use: cache
    Document stores
        like key val store
            key paired with document data structure
            but db is aware of data within it (key-val leaves this to the app)
                each column has some metadata (provides some structure)
                db may have api or QL to read column metadata
                nest documents
            popular formats: xml, bson, json, yaml, pdf, ms word/excel
        mongodb: distributed, most popular
        couchbase: json, memcached-compatible, also func as key-val
        apache couchdb: json, js QL
    wide-column stores / columnar / column oriented
        data stored as cols (instead of rows), optimised for queries over large data sets
        cols stored as separate file/region rather than grouped as a table
        similar to relational
            record order: first entry in each col related to other first entries
            each col same datatype -> compress
            some can use sql
        fast queries, fit aggregate funcs
        load performance bad
            columns written separately
            incremental loads, individial record reads
        apache cassandra
            distributed, maximize scalability, availability, and performance 
        apache hbase
            distributed, maximize possible table size
            fits Hadoop and HDFS 
    graph dbs
        like document: but highlight relationship between docs
        networks
            nodes
            node properties
            undirected/directed edges
            EG use: social network, fraud detection, recommendation engines, and identity, access management application
        Neo4j: ACID-compliant, most popular graph db
        ArangoDB: multi-model that unites graph/document/key-value, AQL/full-text search/ranking engine.
        OrientDB: multi-model, graph/document/key-value/object, SQL/ACID transactions
