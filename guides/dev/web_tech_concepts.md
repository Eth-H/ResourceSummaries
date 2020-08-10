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

# rendering/generating
    client side rendering
        html with attached js that renders site in users browser
        EG: react, vue
        adv
            doesnt re-render the entire page when things are changed
            more libraries and more interactions    
        disadv
            large initial load as downloading js
                need faster internet and hardware
            lower SEO
    pre-rendering
        html pages generated in advance by server
        server side rendering (SSR)
            html rendered on each req (at runtime)
            node with nextjs or gatsby, php
            adv/disadv opposite of CSR
        static generation (SSG)
            html generated at build time, pre-rendered html reused on each req
            few api calls and can host on static CDN
            less functionality (for dynamic data) but fast
    
# routing/nav
    how requests are connected to code
    navigate a webapp
    client site
        url reflect reqs made to server
        page transition happens with js
    server side
        url route normally reflects where the requested page/file is on the server
        each link requests a new page from the server

# styling
    css
    sass
        scss
            extended css with vars
    frameworks
        EG bulma, bootstrap
    css modules
        css file in which class/animation names are locally scoped by default
            styles.modules.css
            import styles from "./style.css";
        unqiue generated class names avoid collision
    css-in-js
        css code is written with the component

# unfurling
    embed info about site in header and meta tags
    display site info to external previews
    oembed standard
