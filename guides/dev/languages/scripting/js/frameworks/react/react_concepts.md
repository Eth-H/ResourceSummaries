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
# hooks
    hook into reacts fuctionality from func components
    useState(intialState) hook
        add state to func component
        returns current state (this.state) and func that updates it (this.setState())
