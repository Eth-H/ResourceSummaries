.NET framework with command line shell and scripting language
PowerShell Cmdlets: Powershell local lightweight command that does something and returns the result as a .NET object,
use this with more cmdlets or by writing to a file/screen, no exe file relates to the cmdlets so they cant be accessed outside the PS
Execution Policy restricts PS scripts that are allowed to run	
cmdlets have a 'verb-noun' naming system

# PowerShell Integrated Scripting Environment (ISE)
    Write/run/test PS scripts
    Has tab completion and search commands,
# basic
    //Get help
        [command] -?
    //Find commands	
        Get-Command -Noun Computer
        Get-Command -Verb Stop
    //Format output to a table
        Generate-Table

//Global object, contains default search path for powershell modules.
    env:psmodulepath

# Aliases
    //Generally ommands have longer names than Bash and CMD alternatives, though powershell comes with several aliases set up for common cmdlets
    //Default aliases
        //ls, dir
            Get-ChildItem 
        //cat (Get contents of a file)
            Get-Content
        //cd
            Set-Location {targetDirectoryPath}
        //rm (delete files and folders)
            Remove-Item
    //Blank: Get all set aliases, -Name [aliasName],  
        Get-Alias {}
    // -Name [alias_name], -Value [cmdlet_to_run]
        Set-Alias {} {}
# Processes
    //blank: List all running processes, -Name [processName]: get a specific process
        Get-Process {}
        Start-Process -FilePath ["exeName/activationCommand"]
    //-Name {processName}, -ID {processID}; confirm: Good if stopping processes with names and wildcards 
        Stop-Process {} {}  
# Objects
//cmdlets are designed to deal with objects, so outputs are more than text
//Each object contains properties (contain info about object (last access time, parent and root directories)) and  methods (manipulate object)	
    //Check info stored inside the result of a command
        Get-ChildItem | Get-Member
    //EG concerning the above command, you could use the Delete Method to delete the directory that object repersents
    //Store result of a command in a variable
        $child_items = Get-ChildItem
    //List names
        $child_items.Name
    //Access methods
        $child_items.[methodName]()
# Execution policy
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    set-executionpolicy unrestricted
    Get-ExecutionPolicy -List
# Package managers
    Scoop
        //Install scoop
            iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
        //Install programs
            scoop install sudo
            sudo scoop install 7zip git openssh --global
            scoop install aria2 curl grep sed less touch
            scoop install python ruby go perl	


