# terms
    promise
## synchronous vs asynchronous
    sync: wait for something to finish before moving onto anouther task
    async: move on without waiting for task to finish, doing >2 things at once
## rendering
    client-side: components of an application rendered in a browser
    server-side: components rendered server-side and html sent to browser
    
# api architecture
ways to fetch data from a server
SOAP (Simple Object Access Protocol)
    protocol
    GET (retrieve) and POST (add/modify)
    bad
        xml data format: slow, inefficient (data over/under fetching)
REST (Representational State Transfer)
    architectural style
    changes the state of the corresponding source by making a request to the URI (Uniform Resource Identifier)
    http caching
    good
        json data format, but works with xml and html

    bad: requests return all propertes associated with request (most not needed)
GraphQL
    query language
    request types: queries (retrieving data), mutations (changing the data)
    no inheritant cacheing, need client side mechanisums EG Apollo client
    good
        data defintions shifted to client-side (server declares avaliable data, client specifies what to return)
            allows minimal response
            
