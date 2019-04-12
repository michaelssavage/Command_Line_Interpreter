# name: Michael Savage
# student ID: 17313526

       MYSHELL    MICHAEL SAVAGE    HELP FILE
---------------------------------------------------------

NAME:
   Myshell - A simple command line interpreter
   that is compatible with Python3.6 and newer..
   
SYNOPSIS:
   The shell is capable of processing the internal 
   commands (1-8 inclusive), taking command line input 
   from a batchfile (9), supporting i/o-redirection 
   on output (10), and executing programs in the 
   background. 
   All other command  line input is interpreted as 
   program invocation.


---------------------------------------------------------
INTERNAL SHELL COMMANDS:

1. cd [directory]

2. clr

3. dir [directory]

4. environ

5. echo [argument]

6. help (or ?)

7. pause

8. quit (or 'q')


---------------------------------------------------------
OTHER:

9. myshell.py [filename]
- input is taken from the [filename].

10. [command] arg1 arg2 > (>>) outputfile
- i/o redirection is possible on output with either 
replace (>) or append (>>).

11. [command] arg1 arg2 &
- Background execution of [command] occurs when an 
ampersand (&) is at the end of the command line.

12. All other command line input is interpreted as
program invocation. The 'subprocess' module creates
and execs a child process with the call() method.
This is only possible in python3 +.


-----------------------------------------------------
DESCRIPTION: 
              ====================
              == cd [directory] ==
              ====================

- change the current default directory to [directory].
-Example

              ====================
              ==       clr      ==
              ====================
              
- clear the shell screen.
-Example

              ===================
              = dir [directory] =
              ===================
              
- list the contents of directory [directory].
-Example

              ====================
              ==    environ     ==
              ====================
              
- list all the environment strings.
-Example

              ====================
              =  echo [argument] =
              ====================
              
- displays [arguments] on the display.
-Example

              ====================
              ==   help (or ?)  ==
              ====================
              
- display the user manual using the more filter.
-Example

              ====================
              ==    7. pause    ==
              ====================
              
- pauses operation in the shell until 'Enter' is pressed.
-Example

              ====================
              ==  quit (or 'q') ==
              ====================
              
- quits the shell.
-Example

              ====================
              ==    batchfile   ==
              ====================
              
- input is taken from the [filename].
-Example

              ====================
              = i/o redirection  =
              ====================
              
- output redirection
-Example

              ====================
              Background execution
              ====================

- ampersand (&)
-Example

              ====================
               program invocation
              ====================

- program invocation.
- child process
-Example
