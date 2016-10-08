# PVT_tracking
Tracking, analyzing and manipulating incoming files
##Source Manager
The source manager defines the types of sources and manages the implementation of client specific source instances.  Examples of source types include FTP, Email, API.  The source manager presents an interface to the Polling Manager and Transport Manager to interface with the physical files before they’re in the possession of Preventure.  The Source Manager and its information reside inside Preventure. It facilitates actions with resources that are outside (or potentially outside) of Preventure.

##Polling Manager
The polling manager is a client specific implementation that looks for the arrival of new files.  Its polling mechanism is two fold, using one set of rules to poll for new files and another set of rules to poll the activity on previously found files. It speaks to the various drop areas through the source manager.   It manages each of three outcomes.
No new data present; No action required.
New data found, create data to track for found files polling
Data quiesced, notify transport manager that there’s an awaiting file and inform the Communication manager
##Transport Manager
The transport manager is responsible for the actual movement of files.  It uses the Source Manager to issue commands across the firewall to facilitate transport.  It uses a data source that is initially populated by the Polling Manager.   Once the PM creates a record, the TM initiates the transfer. It updates the record to indicate that transport is in process.  It tracks success/failure.  In the case of failure, it resets the record to match what the PM created.  It counts the retries and repeats for a predefined number of times before setting the record to ‘failed’ and informing the Communication Manager.  In the case of success, It sets up a record for the Decrypt Manager, similar to its own initialization by the Polling Manager. Lastly, it clears the information from the external source.
##Decrypt Manager
The Decrypt Manager is responsible for access to a keystore and uses the keys therein to decrypt the file.  The Decrypt Manager is also responsible for creating authoritative manifest information for each file that it handles.  All files would pass through the DM, and the DM would record its activities, including timestamps, input filenames, output filenames, errors. It would send information to the NM as to its job outcomes.  The DM would require minimal user interactions, basic setup of matching a filename pattern to a key would likely be the only requirement.  The Decrypt manager would also be responsible for compiling checksums of the files that it manages, and recording the authoritative information about every file that passes through the system. 
##Validation Manager
The validation manager would be responsible for supporting tests of the data. It would have granularity down to the client/column.  For each client/column it would look up information that directed it to analyze and report on the column.  Examples include required, matches with validation lists, patterns \d\d\d-\d\d-\d\d\d\d = SSN,(?\d\d\d[-)]?\d\d\d-?\d\d\d\d = phone # with optional parens and hyphens.  
The validation manager will require extensive user interaction, as the user must be able to introduce, and modify the rules.  The validation manager would also track the tests applied to each column and the outcome of the tests.  The validation manager would also be tasked with establishing a severity level (information, warning, failure) and would be configurable to send information to the Communication manager 
##Scrubbing Manager
The Scrubbing Manager is a superset of the Validation Manager. It would be able to take action (for instance, stripping hyphens from SSN’s, padding fields).  It’s logging would be critical. It would share much of the user interaction with the VM.
##Communication Manager 
The Communication Manager would be responsible for compiling and disseminating messages from the various services.  It would require extensive user interaction in order to match the incoming information and make decisions on whether the information is merely logging status or requires actual notification.  The notification manager should understand how to send email.  It should also support interfacing with SFDC in order to create a record for  follow up work and conversation by Preventure staff.

##Task List
* User interface. Research python user setup
* Create DB in SQLITE
* Investigate SQL-Server connection

