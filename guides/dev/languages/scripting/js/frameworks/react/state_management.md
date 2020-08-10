# example items of state
    what the user sees (data)
    the data we fetch from an API
    the URL
    the items selected inside a page
    eventual errors to show to the user

# no libraries
    individual local state per class component
        pass state though props
        children share parent component props
        update via this.setState()
    context api
    react router pass data through urls
    history

# redux library
    state management library
    creates a global state for the whole application (not for individual apps)

    store: apps entire state, reducer will update
    actions: objs with properties: describe type of action and what to change in app state
    reducers
        funcs that implement behaviour of actions to update the store via state
        reducerFunc(action, currentState)
        react components will connect to the store via reducers

        state owned/calc by the single root reducer func, it can be split into slices
            each slice is responsible for providing an intial val and calc updates for its slice of state
        unless using middleware, these should contain most of the logic on manipulating state
            but cant execute async logic, gen random vals, modify external vars
    action creators
        funcs that wrap the actions, may implement some logic alongside
## store methods
    getState() for reading the current state of the application
    dispatch() for dispatching an action
    subscribe() for listening to state changes
## react-redux
 t   get component to interact with store
### connect()
    connect react component to redux store
    takes 2-3 args
        custom funcs
            mapStateToProps = function() //mapState func
                connects a part of the Redux state to the props of a React component
                gives component access to the part of the store it needs
                aimed at iterating state, large data transformations
                    slow
                    on store changes all mapStateToProps funcs of all connected components run
                        need to be quick, otherwise possible bottleneck
                    only return new obj refs if needed
                        use memorised selector funcs to avoid (trsfms only run when input values changed)
                    avoid expensive operations unless data changes
                        calc some trnfms in reducers, action creators, components render()
                        store some transformations in the store
                implement
                    func should iterate return val to be used
                    statefull component can access via: this.props.mapStateReturnedFuncOrVal
                    stateless access via: params to func

            mapDispatchToProps = function()
                connects Redux actions to React props 
                enables component to send msgs to the store

### hooks
    provide alternative to connect() using react hooks
#### selectors
    alternative to connect(mapStateToProps)
    encapsulate process of extracting values from specifc locations in state tree
    vs mapState func
        centralised knowledge about state, so unlikely to break if state changed, unlike mapState
    memorized func: remember last args and returned value, if args are the same return old value instead of recomputing
        offload iteration of state to a external selector func
        that func is reuseable
    implement
        within connect() mapState
        useSelector(selector) hook
            can use external selector or inline selector
            returned val of selector used in useSelector hook, so can return non-objs
        memorized selectors
            createSelector() from reselect

    useDispatch() hook
        returns ref to dispatch func from redux store
    useStore() hook
        return entire store, obviously less efficient than selector
        useStore().getState()

## redux middleware
    separate logic from components
    adv: logic separate from UI, middleware reuseable, can be tested in isolation
    required to deal with non-serializable values such as Promises, Symbols, Maps/Sets, functions, or class instances

## deal with async calls
    cant return promises from an action creator (only objs)
    redux-thunk middleware
        thunk allows returning of funcs from action creators, which can contain async code.
    custom middleware
        mv async logic to custom middlware, though hard to manage/test
    redux-saga middleware
        amangeing side effects
        create separate thread for impure actions
        will intercept actions with takeEvery
        can live in a
            watcher function
                generator func wathcing all interested actions
                will call a worker saga in response to an action
            worker function 
                will call remote API via a func with redux-saga/effects/call() and dispatch it as an action with redux-saga/effects/put()

## redux toolkit bootstrap
    create-react-app myapp --template redux
    funcs
        combineReducers({reducer1, reducer2}) if same name
        combineReducers({reducer1: importedReducer, reducer2: importedReducer2})
            combine 2 reducers into one obj
            can import this obj and dispatch actions using either reducer
        configureStore(rootReducer, middleware)
            wrap createStore, if passed sliced reducers uses combineReducers to produce one root reducer


## redux folder layout
    ducks - via fetures/functionality
    traditional - via reducers, actions, store
