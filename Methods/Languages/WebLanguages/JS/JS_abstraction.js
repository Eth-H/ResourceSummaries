//List emthods
	var list = [];
	//Add and remove from end of list
	list.push(1); list.pop(); 
	//Add and remove from start of list
	list.shift(1); list.unshift();


//selection
	 if(i>10 & i<15){log.console("10-15")
    }else if(i>10 || i<15){log.console(">10 or < 15)}
	
	//case statement
		switch(rank){
		   case "Commander":
				console.log("Hello commander! what can I do for you today?"); break;
		   case "Captain":
				console.log("Hello captain! I will do anything you wish."); break;
		   case "what?":
				console.log("Lets try again"); continue;
		   default:
				console.log("I don't know what your rank is."); break 
		}
	//terinary operator, condition ? true : false
		(num>0) ? "positive" : (num<0) ? "negative" : "zero";

//iteration
for (var i = 0; i < myArray.length; i++){console.log(i + myArray[i])}
while (i > 0){i -= 1; console.log(i)}

//objects
	//iterate object
		for (var member in personObject){console.log (personObject[member])}
    //Checks that a property belongs to a object.
		personObject.hasOwnProperty((propertyName)) 
	//del
		delete cat.name;
	//Get property names
		object.keys()
	//Binding
		//Associate object with function to call it
			var person = {name : "John"};
			function printName(){console.log(this.name)}
			var boundPrintName = printName.bind(person);
			boundPrintName();    
		//Or could call functions with other contexs using call()
			printName.call(person);
	//constructors
		//create
		function Bird() {this.name = "Albert"; this.color = "blue"; this.numLegs = 2}
		//new instance
			let blueBird = new Bird();
		//Verify an objects constructor
        	Cockapoo instanceof Dog;				   
		//A prototype is an object that is shared among all instances of the child object
			Animal.prototype = {constructor: Animal, eat: function() {console.log("nom nom nom")}};			
		//Check an objects prototype
			 Dog.prototype.isPrototypeOf(Cockapoo);
		//Object.create(newPrototypeObj), newly created object that gets the param as its prototype
            let Cow = Object.create(Animal.prototype);
						   
						   
						   
//array 
	//spread operator
		//Insert an entire array in a certain position
			let thatArray = ["What","is","this",...array,"useful","for"];			
	//Get the index of an item
		array.indexOf("am");
	//Array manipulaton methods
		//splice(index, numToRemove), remove items from a list and store them in variable
			//EG start at position 4 and remove 2 items
			var splice = myArray.splice(3,2);  
		//slice(indexToStart, indexToEnd+1), copy elements from an array		
			//EG start at position 2 and copy until position 3 
			let todaysWeather = weatherConditions.slice(1, 3);
		//concat, joins two arrays
			//EG x = [1,2,3,4,5,6]        
			x = [1, 2, 3].concat([4, 5, 6]);
		//Combine with higher order fucntions
			FBPosts.filter((post) => post.thumbnail !== null && post.shares > 100 && post.likes > 500)
    	//Array.prototype.map(item, index)
			var arrSorted = arr.map( function( item ){return item * 2;});				   
			var arrSorted2 = arr.map((item, index) => ({id: index, itemName: item }) )
		//Array.prototype.filter()
			//Function logic applied on each item in the array, if the function returns true the item is added
				const filteredList = watchList.filter(elem => Number(elem.imdbRating) >= 8.0).map(elem => ({"title": elem.Title, "rating": elem.imdbRating}));
		//Array.prototype.reduce()
			//Reduces an array to a single value, executes a provided function for each value of the array, the returned value is stored in an accumulator
			//array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
			//Eg Get an average of the imdbRating of moves performed by Christopher Nolan
				var averageRating = watchList.filter(elem => elem["Director"] === "Christopher Nolan")
            		.reduce((total,elem,index,arr)=>{return total+Number(elem["imdbRating"])/arr.length;},0);
		//Array.prototype.sort(), compares two values using unicode strings, provide a callback function to customise the sorting
			//sort() sends the values to the function, then it sorts the values according to the returned (negative, zero, positive) value
			numList = [1, 5, 6, 4]; letterList = ['l', 'h', 'z', 'b', 's'];
			function ascendingOrder(arr) {return arr.sort(function(a, b) {return a - b;});}
			ascendingOrder(numList); //Returns   [1, 4, 5, 6]
			function reverseAlpha(arr) {return arr.sort(function(a, b) {return a < b;});}
			reverseAlpha(letterList); //Returns  ['z', 's', 'l', 'h', 'b']
		//Array.prototype.split(whatToInsertBetweenEachElement), split a string into a list
        	//EG split for space
				arrName.split(" ")
			 //EG split a string into an array of just words
				function splitify(str) {return str.split(/[^a-z]/i);}
				console.log(splitify("Hello World, I-am code")); //returns Hello, World, I,, am, code
         //Array.prototype.join(whatToInsertBetweenEachItem), combine an array into a string
			var arr = ["Hello", "World"]; var str = arr.join(" ");
		//Array.prototype.every(), returns true if all values meet the criteria
			//EG Find out if a list has any negative values
				function checkAllPositive(arr) {return  arr.every(function(currentValue){return currentValue > 0;});}
				checkAllPositive([1, 2, 3, -4, 5]); //Returns false
    	//Array.prototype.some(), returns true if one value meets the criteria
			function checkOnePositive(arr) {return  arr.some(function(currentValue){return currentValue > 0;});}
			checkOnePositive([1, 2, 3, -4, 5]); //Returns true
						   
//regex
	//Find stuff with a literal match/patturn
	//Methods 
		//Find a word, (with a literal match/patturn)
		let testStr = "freeCodeCamp"; let testRegex = /Code/;
		//return true it regex matches
			regexName.test(strToTest);
		//Returns identified expression
			strToTest.match(regexName);
        regex.execute("hello"); // returns result array, null otherwise
        "football".replace(/foot/,"basket"); // replaces matches with second argument
		
		//characters
			//wildcard, match anything, EG will match hox, hoa, ...
				/ho./
			//Character classes/set, get a range of values in character class
				// EG Will accept b start and g end, middle can be "a, i or u"
					/b[aiu]g/;
				//EG Match all letters and numbers in a single character set
					/[a-z0-9]/ig;
				//caret character, used a negated character set
    				//EG no vowels
						/[^aeiou]/ig;
					//EG no letters or numbers
						/[^a-z0-9]/ig;
			 //Look for consecutively presented characters (one or more)
    			/a+/g;
			//Look for zero or more
   				/a*/g;
			//Use Lazy matching to find the smallest possible part of the string that satisfies the regex patturn
				let text = "<h1>Winter is coming</h1>";
				let myRegex = /<.*?>/;
				let result = text.match(myRegex);
				//Will return <h1>
			//Use the caret character outside a character set to search for patturns at the beginning of strings
    			/^Cal/;
    		//Search for patturns at the end of the line
    			/story$/;
			//Use quantity specifiers to specify the lower and upper numbers of patturns
				//EG 3 to 6 h's, >3, =3
					/Oh{3,6} no/; /ha{3,}h/; /ha{3}h/;
			//Specify the possible exsistance of an element using a question mark, it checks for zero or one of the proceeding element
    			/colou?r/;
    		
			//Lookaheads, tells JS to look-ahead in your string to check for patterns further along
				//can search for multiple patturns in the same string
				//A postive lookahead looks to see if the element in the search patturn is there, but won't actually match it
				//A negative lookahead will make sure the element is not there
					//EG +, -
						"qu".match(/q(?=u)/); // Returns ["q"]
						"qt".match(/q(?!u)/); // Returns ["q"]
		//operators
    		/dog|cat|bird|fish/;
		//flags
			//And a i flag to ignore case sensitivity
    			/ignorecase/i;
    		//Add g flag to get more than the first match
    			/Repeat/g;						   
		//Shortcuts
			//Shortcut for usign the entire alphabeat in character sets
				/[A-Za-z0-9_]+/; = /\w+/;
			//Not characters and numbers shortcut
				/[^A-Za-z0-9_]+/; = /\W+/;
			//Shortcut for [0-9] and [^0-9]
				/\d/; /\D/;
			//Match Whitespace and non-whitespace
				/\s/g; /\S/;
		//Capture groups, search for repeat substrings  
			//Use a \x , where x is a number that specifies each additional capture group you use. EG \1 matches the first group
			//EG, returns true, returns ["regex regex", "regex"]
			/(\w+)\s\1/.test("regex regex"); 
			"regex regex".match(/(\w+)\s\1/); 

						   


						   
//random methods
	//Use callback functions by passing them as parameters
	setTimeout(callbackFunction, 5000);
	//get type of variable
		typeof variableName
	//change data types
		//string -> float
			parseFloat("007");			   
		//string -> Int
			//Returns string in int base 2
    			parseInt("11", 2);
	"a".repeat(100)
						   

//Different methods to import a module
	import defaultExport from "moduleName";
	import "moduleName";	
	import * as name from "moduleName";
	import { exportList } from "./file_path"
	import { export1 , export2 as alias2 , [...] } from "moduleName";
	//Maths module
import "Math";
import defaultExport, { export } from [, [...]];
} from "moduleName";
	
	//absolute value of a number
	Math.abs 
	//e to the power of a number
	Math.exp 
	//x to the power of y
	Math.pow(x,y)
	//removes the fraction part from a number
	Math.floor 
	//will give a random number x where 0<=x<1
	Math.random() 

						  
//code examples
	//features
		//Default parameters, when argument is undefined passes a value
			const increment = (function(number, value) {
			  //"use strict";
			  return function increment(number, value = 1) {
				return number + value;
			  };
		
		//Destructuring assignment, this allows you to neatly assign values from an object to a variable.
			var voxel = {x: 3.6, y: 7.4, z: 6.54 };
			var x = voxel.x; var y = voxel.y; var z = voxel.z;  //shortened to 
			const { x, y, z } = voxel;
			//or store into different variable names
			const { x : a, y : b, z : c } = voxel	
			
			const [a, b,,, c] = [1, 2, 3, 4, 5, 6];	// 1, 2, 5
			const [a, b, ...arr] = [1, 2, 3, 4, 5, 7]; // arr = [3, 4, 5, 7]
			
		//Currying, take parameters one at a time or both at once 
			function curried(x) {
				return function(y) {
					return x + y;
				}
			}
			curried(1)(2); // Returns 3
			var funcForY = curried(1);
			funcForY(2)); // Returns 3
		//partial application, pass some args and return a function that takes the remaining args as params
			function impartial(x, y, z) {return x + y + z}
			var partialFn = impartial.bind(this, 1, 2);
			partialFn(10); // Returns 13		
					
		//Nested for loops
			var arr = [[1,2], [3,4], [5,6]];
			  for (var i=0; i < arr.length; i++) {
				for (var j=0; j < arr[i].length; j++) {
				  console.log(arr[i][j]);
				}
			  }		
    //Getter and setter functions
		class Book {
			constructor(author) {this._author = author}
			// getter
			get writer(){return this._author}
			// setter
			set writer(updatedAuthor){this._author = updatedAuthor}
		}		
	//object oriented
		//Mixins, allows other objects to use a collection of functions, better than passing prototype for unrelated functions
			let flyMixin = function(obj) {
				obj.fly = function() {console.log("Flying, wooosh!")}
			};
			let bird = {name: "Donald", numLegs: 2};
			let plane = {model: "777", numPassengers: 524};
			flyMixin(bird); flyMixin(plane);
		//Closure, protect properties within an object from being modified externally
			 //One way to do this is to declare a variable within the cosntuctor function so the scope is restrained
			function Bird() {
				// private property
				let hatchedEgg = 10; 
				// publicly available method that a bird object can use
				this.getHatchedEggCount = function() {return hatchedEgg};
    		}	
		//Immediately Invoked Function Expression (IIFE), executed as soon as they are declared (can give fucntion a name or have it anomynous)		
			 (function () {
            	console.log("A cozy nest is ready");
        	})();	
			//Use a IIFE to group related functionality into a single object or module.
        		//The returned object contains all of the mixin behaviors as properties of the object
				let funModule = (function() {
            		return{
                		isCuteMixin : function(obj) {obj.isCute = function() {return true}},
						singMixin : function(obj) {obj.sing = function() {console.log("Singing to an awesome tune")}}
            		}
        		})();
				funModule.singMixin(ducky);
				ducky.sing();		
				
//text
	/*Example errors: Misspelled variable/fucntion, unclosed parentheses/brackets/braces/quotes, mixed useage of single and double quotes, assigment operator rather then equality operator,
	forgeting opening nad closing parenthesis after a function call, paramters the wrong way, index[0] mistakes espically in for loops, (reinitializing or not, variables in loops),
	no terminal condition leads to infinate loops 
				
	Terminology>
		Callbacks are the functions that are slipped or passed into another function to decide the invocation of that function. (EG Filter)
		First class functions: Functions that can be assigned to a variable, passed into another function, or returned from another function just like any other normal value (covering all js functions)
		Higher order functions: The functions that take a function as an argument, or return a function as a return value
		Lambda: When the functions are passed in to another function or returned from another function, then those functions which gets passed in or returned can be called a lambda.
		in functional programming, changing or altering things is called mutation, and the outcome is called a side effect
 		- A function, ideally, should be a pure function, meaning that it does not cause any side effects.
		arity: Number of arguments a function requires
		Refactor: Rewrite code
		Currying a function: to convert the function of N arity into N functions of arity 1
			-(restructures a function so it takes one argument, then returns another function that takes the next argument),
			useful if you can't supply all the arguments to a function at one time
		//partial application: applying a few arguments to a function at a time and returning another function that is applied to more arguments.
			
	Principles>
		Don't change things in functions (mutation)
		Declare dependencies explicitly (pass needed variables and don't depend on global variables)

						   
						   
						   
						   
						   
						   
						   







