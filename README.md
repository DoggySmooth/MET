			---	MET DOCUMENTATION	---


MET is a format for reverse engineer reports of applications. The advantage of MET is a clear defined data structure allowing users to generate graphs for analysis as allowing them to create tools to manipulate the data. Using XML as main format makes it known to the most of people out there and its extensible structure makes changes fast.

There are unlimited manners to write a report of an analysis based on what the reverse
engineer thinks its relevant. The reports layout needs to be understood first and if 
we want to do M2M manipulations we need to adapt/write tools to work with that 
particular report. It's useless to tell that this is inefficient. That's where MET
comes into the screen. By defining rules and formats as also providing tools to easily
query and manipulate reports, MET speeds up the whole reverse engineering process and 
in the same time makes it easier for someone else to understand the analysis. As the
format and layout is defined, MET provides extensibility to the reports and also to the tools that manipulate the data. MET users could collaborate on some reverse engineering of an application and easily merge their output.

This is the main idea behind MET.

MET could so implement a whole bunch of features manipulating the data.

Features:

	1. Graph generation
	
	Easy graph generation showing how the package is structured and which nodes are
	malicious.

	2. JSON generation
	
	Maschine to Maschine data transfer and manipulation using well known JSON format	
	3. HTML 

	Displaying analysis in an easy to read format displaying the malicious behavior 	
	of classes, packages or methods with an description.

	4. Merging

	Merging of generated XML files from plims together in an unique file.

______________
Architecture:
______________

The main file MET is using is the XML format, from which is generated all the files
described in "Features". As XML is a verbose and annoying language, we use a python library to generate the XML: PLIM.

PLIM -> XML <-> JSON -> HTML

Format

Plim’s structure is intuitive.
 
	doctype xml

	analysis
	 res			/1..1  
	 metadata-------------	/1..*  
	  date			/1..1  
	  access 		/1..1  
	  accessloc 		/1..1  
	  author 		/1..1  
	  email 		/1..1  
	  perm			/1..1  
	  tags 			/1..1  
	 data			/1..1  
	  art	-------------	/1..*  
	   loc			/1..1  
	   type			/1..1  
	   name 		/1..1  
	   level		/1..1  
	   desc			/1..1  
	   tag			/0..*  
______________

Technical data
______________


1.Graph Generation

The structured JSON file allows to do data manipulation in an well known manner.
GraphViz's library for python helps to structure the data and generate the graph.
JSON's library is used to import the json generated file from the XML.


2.JSON Generation

For the generation of the JSON file a tool is being used. Called xml2json, it lets easily generate the data. JSONLINT is used to format the data and finally JSONLINT to validate the data structure of the JSON file.

3.HTML generation

A self written python script generates the files including an intuitive layout. 
The html generation is based on the generated json file.

4.XML generation

PLIM tool is included in the package and with the help of plim compiler "plimc" it generates an XML file from its plimfile. The generated XML goes trough a formating phase with the help of xmllint and then a written XSD file validates the structure of the generated xml.

5.Merging

An python script has been coded to make it easier for the users to merge existing xml files allowing distributed work to be done. The tool checks if the same SHA256 is present in the XML files for consistency purpose.

______

Tools
______


Files creation

All the tools are included in this package token from github under directory “met”.
The launching scripts are under “ scripts”.


Merging

In the directory "met/scripts/" there is the python script called met-merger.py.
Run ./met-merger.py 'firstXMLfile' 'secondXMLfile'	to generate the merged XML.

					

__________________
--- MET HOW TO ---
__________________


STEPS:

	1. CREATE A PLIM FILE WITH AN ANALISIS
	2. PASTE IT IN FOLDER "plims"
	3. execute python3 amrev.py "plimFile"
	4. ALL THE OUPUT IS AVAILABLE IN FOLDER "output/$(nameOfPlim)/"


Let's start with the plim writing.
PLIM file will be converted in XML and the XML will be checked if there is the correct syntax with the help of xsd. The XSD schema is in "res/schema/".

By looking at it, we know how to structure our plim file. The cardinals shows if a tag can be ommited or repeated.

NOTE: ITS IMPORTANT TO TAKE CARE FOR A CORRECT INDENTATION.

The first part are meta datas about the reverse

	analysis  
	 res sha256://bsaifbiasoujb2345F3k1bj4F3223r  
	 metadata  
	  date 03041993  
	  access 03042012  
	  accessloc googleplay  
	  author Smooth  
	  email smooth  
	  perm shared  
	  tags trojan,exploit,root   
	 metadata  
	  date 05091994  
	  access 01081998  
	  accessloc googleplay  
	  author Boo  
	  email boos  
	  perm shared  
	  tag trojan  
	
	
As usual. That kind of information can be easily extracted from most reverse engineer tools for android applications and put there for informative purpose.


NOW LETS MOVE ON WITH THE MAIN ANALYSIS

	 data  
	  art  
	   loc com.adsdk.adwo/H  
	   type attribute  
	   name d  
	   level benign  
	   desc It's a WebView that overlays the main screen displaying malicious adds  
	   tag Heavy  
	  art  
	   loc com.adsdk.adwo/x  
	   type method  
	   name toString(var X)  
	   level malicious  
	   desc Converts an String into an encrypted base64 String  
	  art  
	   loc com.sdk/L  
	   type URL  
	   name bhkjnl.commandandcontrol.cn  
	   level malicious  
	   desc URL of the command and control server used by the malicious app  
	  art  
	   loc com.sdk/L  
	   type URL  
	   name bhkjnl.commandandafsd.afs  
	   level malicious  
	   desc URL of the command and control server used by the malicious app  
                                                                         
This plim file is self explanatory.
This example is found under directory examples.

run compile.py plim 			to generate its xml  
run met-x2j.py 				to generate json  
run met-graph.py jsonFile		to generate svg  
run met-report.py jsonFile		to generate html  

The atomic tools are located in directory "met/scripts/". 
Instead of running the above script, each step can be done manually.

Thanks!

