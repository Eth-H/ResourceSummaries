# terms
## module
    reusable piece of code that encapsulates implementation details and exposes a public API so it can be easily loaded and used by other code
    allow module design
    aims (fix dependancy requirements)
        abstract (hide implementation)
        encapsulation
        manage dependancies
        reuse
    module api: exported funcs used to interact with a module
## manual fix for modular design
    revealing module pattern
        module declared as func, declared protected by func scope, public symbols returned by func wrapping other funcs
    immediately invoked function expressions

    right order
## module system/formats
    syntax to define depedancies and modules
    way of importing modules that solves dependancy problems
### developer made specifications
    CommonJS and nodeJS (similar)
        require func
            import modules from anouther module to current scope
            takes module id (name in node_modules)
            var dep1 = require('./dep1');
        export obj
            exports contents as a public element
            module.exports = function(){...}
    Asynchronous Module Definition (AMD)
        browsers
        define func defines modules
    Universal Module Definition (UMD)
        browser and nodejs
    System.register
    ES6 native module format
        native to js
        not supported by most browsers
            use transpiler to transpile code to ES5 module format (AMD, commonjs, ...)
        import directive
            bring modules into the namespace
            static anlysers build dependancy tree without running code
                imports not dynamic (cant call from anywhere)
        export directive
            explicitly make elements public
        eg via default import
            export default class DefaultImport(){...}
            import DefaultImport from './lib'
        eg named imports
            export function sayHello(){...}
            export function sayHello2(){...}
            import { sayHello, sayHello2 } from './lib'; //use destructoring to import multiple items

### implement specifications
#### module loader
    interpret/load module written in a certain module format
    runs at runtime
        loaded in browser
        tell main app file
        will download/interpret main app file, and other files as needed
        eg requirejs (amd format), systemjs (amd, commonjs, umd, system.register)
#### module bundlers
    replaces module loader
    runs at build time
        gen bundle file
        load bundle in browser
    EG browsersify (commonjs), webpack (amd, commonjs, ES6 modules)
### transpiler
    convert certain js module format into anouther
    mainly for compatibility, allows newer js formats to work with older browsers
    EG Babel (ES6 module format to ES5 module format)

# links
https://2019.stateofjs.com/data-layer/
https://redux.js.org/introduction/getting-started
https://auth0.com/blog/javascript-module-systems-showdown/
https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/
https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
