# summary
    react framework
## rendering
### pre-rendering
#### static generation (SSG)
    with data - async getStaticProps(context)
        fetch external data that a pages content depends on before pre-rendering
            nextjs will pre-render page with returned props
        can only be exported from a page
        can: query a db, fetch from a api, read from filesystem, ...
        context
            .params: route params for dynamic routes
            .preview .previewData
            
#### server side rendering (SSR)
    async getServerSideProps(context)
        nextjs will pre-render page on req with returned props
        .params: route params for dynamic routes
        .req: HTTP IncomingMessage obj
        .res: HTTP response obj
        .query: The query str
        .preview .previewData

    can create a hybrid app that uses a mix of SSR SG and CSR
### client side rendering (CSR)
    pre-render parts of page that dont need exteral data -> after page load (req time) fetch external data with js
    EG dashboard pages
    can use the swr react hook to fetch data on the client side
            
## routes

## dynamic routes
    can statically generate pages with paths that depend on external data
    getStaticPaths()
        return arr with possible values of a val relating to a filename in a dir
        nextjs will statically pre-render all returned paths
        .paths: arr of path objs
        .fallback: on failure use a fall-back page, or send a 404



    getStaticProps() - fetches necessary data for the post with id
    catch all routes
        pages/posts/[...id].js -> /posts/a, but also /posts/a/b, /posts/a/b/c and so on.
    access router
        import useRouter  from 'next/router'

### api routes
    create endpoint as nodejs func
    dont fetch from getStaticProps, instead write server side code directly


### client-side routing/navigation, via <Link>, faster than browser navigation
    prefetch linked code in background
    api routes, good for endpoints with serverless funcs


    css, sass, css-in-js libs
    dev env hot module replacement
    markdown
        frontmatter: npm install gray-matter
        rendering: npm install remark remark-html

    npx create-next-app 
    //or
    npm init next-app nextjs-blog --example "https://github.com/vercel/next-learn-starter/tree/master/learn-starter"

    npm run {}
        dev - next, starts Next.js in dev mode (uses SSR even for SG pages)
        build - next build, builds the app for production usage
        start - next start, starts a Next.js production server
## dir structure
    pages/
        exported react component in pages dir
        associated with a route like /pageName
            pages/posts/first-post.js -> /posts/first-post
        _app.js
            top-lv component common across all pages
            manage global state
            put global styles
        /posts
            [...].js - dynamic page[s]
        /api
            api routes/endpoints
    public/
        static content
        images/
    components/
        reuseable components
            EG modulised css
    styles/
        glboal styles

    postcss.config.js
        config for default css-in-js transformer

    posts/
        for a static generation site
        write markdown
            can contain YAML front matter for parsing by the gray-matter lib
    lib/
        pure js to import into components
