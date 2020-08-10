# tools
    templates
        https://github.com/facebook/create-react-app
        https://github.com/WellyShen/react-cool-starter/
        https://github.com/react-boilerplate/react-boilerplate
    routing
        react-router
            //implement core pkg for web apps or native
            react-router-dom
            react-router-native
    ready-made components / UI frameworks
        reactstrap
        react-bootstrap
            react-router-bootstrap
        MaterialUI
        react-toolbox
        react-foundation

# func components vs class components
    class
        have own/local state
        need more code, render() mtd and extends React.Component
    func
        stateless
        accept properties, return jsx
        react hooks
# lifecycle mtds
    componentDidMount
    componentDidUpdate
    componentWillUnmount

# hooks
    hook into reacts fuctionality from func components
    each has isolated state
    rules
        cant call in classes or non-React funcs
        can only call at toplevel (not in loops,conditions,nested funcs)
    useState(intialState) hook
        add state to func component
        returns current state (this.state) and func that updates it (this.setState())
        const [count, setCount] = useState(0); 
    useEffect(func, [val, val2])
        perform side effects from a func component
        useEffect(() => { document.title = `You clicked ${count} times`; });
        runs "effect" func after flushing DOM changes
            like componentDidMount & componentDidUpdate, applys after every render
            like componentWillUnmount, can return a func to run on umount
        optionally dont carry out the effect if no arr val has changed since last render
    useMemo()
        memorise a val
        only recompute val if an arr param changes
        const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
    useRef(initialVal)
        create new mutable ref obj with obj.current = initialVal
        obj persists for lifetime of component

    custom hooks
        usefull to share state between hooks
