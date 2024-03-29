--------------------------------------------------------------
- Michael Savage      Student ID: 17313526           MYSHELL -
--------------------------------------------------------------

||NAME||

    Myshell - A simple command line interpreter that is 
    compatible with Python3 and newer..
     
||SYNOPSIS||

    The shell has many uses. It is started by entering

                    python3 myshell.py

    It is capable of

    • Processing the internal commands (1-8 inclusive),
    • Taking command line input from a batchfile* (9), 
    • Supporting i/o-redirection* on output (10),
    • Executing programs in the background (11), and
    • Executing child processes* (12)

    All other command line input is interpreted as
    program invocation*. The 'subprocess' module creates
    and execs a child process* with the call() method.
    This is only possible in python3 +.

    To find out more about each command, press the space
    bar to read more. Each command description includes
    an example of usage.

    There are supportive definitions at the end of the 
    help file too for some keywords I feel are important.
    Definitions are available for words where you see
    [keyword]*.


--------------------------------------------------------------
-                    INTERNAL SHELL COMMANDS                 -
--------------------------------------------------------------

1. cd [directory]*

2. clr

3. dir [directory]*

4. environ

5. echo [argument]

6. help (or ?)

7. pause

8. quit (or 'q')

--------------------------------------------------------------
-                    OTHER SHELL COMMANDS                    -
--------------------------------------------------------------

9. python3 myshell.py [batchfile]*

10. [command] arg1 arg2 (> OR >>) outputfile

11. [command] arg1 arg2 &

12. python3 test.py


||DESCRIPTION||

--------------------------------------------------------------
-             INTERNAL SHELL COMMAND DESCRIPTIONS            -
--------------------------------------------------------------

                ====================
1.                 cd [directory]* 
                ====================

• change the current working directory* to [directory]*.
• if no argument is given, then the CWD is used.
• if [directory]* = "..", then the CWD is changed to the
  parent directory*.

--------------------------------
- Examples:                    -
-            cd ..             -
-            cd                -
-            cd /users/case2   -
--------------------------------

                ====================
2.                       clr      
                ====================
                            
• clear the shell screen by printing "\033". This is
  the ASCII escape character.
• additional arguments are ignored.

----------------------------------
- Examples:                      -
-            clr                 -
-            clr 1234552xagz     -
----------------------------------

                ====================
3.                dir [directory]* 
                ====================
                            
• list the contents of directory* [directory]*.
• if no argument is given, then current directory* objects
  are listed.
• directory* contents can be redirected to an output file.

-----------------------------------------
- Examples:                             -
-            dir                        -
-            dir /users/case2/savagem7  -
-            dir > gg                   -
-            dir /users >> a.txt        -
-----------------------------------------

                ====================
4.                    environ     
                ====================
                            
• list all the environment strings as keys and values.
• additional arguments are ignored.
• the shell pathname is modified as "/myshell" is appended
  to the end of the name and it is conveniently bold.
• environment strings can be redirected to an output file.

-----------------------------------
- Examples:                       - 
-            environ              - 
-            environ dw23rw       -
-            environ > hello      -
-            environ >> hello     -
-----------------------------------


                ====================
5.                 echo [argument] 
                ====================
                            
• displays [arguments] on the display using print.
• if no arguments are given, a message is displayed saying
  this.
• [arguments] can be redirected* to an output file. 
• for convenience, if no arguments are given when being
  redirected* then an empty string is printed.

-------------------------------------
- Examples:                         -
-            echo hello world       -
-            echo                   -
-            echo 1 + 2 + 3 + 4 + 5 -
-            echo python! > gg      -
-------------------------------------

                ====================
6.                    help ('?')  
                ====================
                            
• display the user manual using the more filter.
• additional arguments are ignored.
• help file can be redirected* to an output file.

-------------------------------
- Examples:                   -
-            help             -
-            ?                -
-            help ada3445     -
-            ? > helpfile     -
-------------------------------

                ====================
7.                     pause      
                ====================
                            
• pauses operation in the shell until 'Enter' is pressed.
• additional arguments are ignored.

-------------------------------
- Examples:                   -
-            pause            -
-            pause unpause    -
-------------------------------

                ====================
8.                   quit ('q')   
                ====================
                            
• quits the shell with a thank you message.
• additional arguments are ignored.

-------------------------------
- Examples:                   -
-             quit            -
-             q               -
-             quit 1234       -
-------------------------------

---------------------------------------------------------
-            OTHER SHELL COMMAND DESCRIPTIONS           -
---------------------------------------------------------

            ===============================
9.          python3 myshell.py [batchfile]*
            ===============================
                            
• as said in the synopsis, starting the shell is done by
  python3 myshell.py
• the shell can take an additional argument at launch
  that will be a batchfile*.
• the [batchfile]* is assumed to contain a set of command 
  lines that the shell can process.
• the line number and arguments are printed in bold, 
  followed by execution of that line.
• when the end-of-file is reached, the shell exits.
• "file input error" is printed when the [batchfile]* is
  invalid or does not exist.

-------------------------------------------------------
- in this example, the batchfile* is i.txt which      -
- contains 2 lines of commands.                       -
-------------------------------------------------------
- Examples:                                           -
-            python3 myshell.py i.txt                 -
-                                                     -
-            Line 1 contains: echo hello              -
-            -----                                    -
-            hello                                    -
-            -----                                    -
-            Line 2 contains: pause                   -
-            -----                                    -
-            Shell paused.. Press 'Enter' to continue -
-            -----                                    -
-------------------------------------------------------

        ========================================
10.     [command] arg1 arg2 (> OR >>) outputfile
        ========================================

• in this shell, i/o redirection* is possible on output.
• redirection* means capturing output from a source such as a 
  file, program or script and then sending it as input to 
  another source.
• in other words, the stdout that would be displayed on the 
  terminal is now put into outputfile.
• output redirection* is possible for the commands;
        - dir, 
        - environ, 
        - echo, and 
        - help
• output can be truncated* by using '>' or it can be appended 
  with '>>'.
• if the file does not exist, it will be created.

-------------------------------------------------
- in this example gg is created and environ is  -
- appended to the same file. abc is created by  -
- environ but then it is truncated* by echo.    -
- the help command appends to newfile.          -
-------------------------------------------------
- Examples:                                     -   
-            dir > gg                           -
-            dir /users > newfile               -
-                                               -
-            environ > abc                      -
-            environ >> gg                      -
-                                               -
-            echo I am truncating abc > abc     -
-            echo > newfile                     -
-                                               -
-            help >> newfile                    -
-                                               -
-------------------------------------------------

        =====================
11.     [command] arg1 arg2 &
        =====================

• the ampersand (&) at the end of the line indicates that 
  background execution will take place.
• subprocess.Popen() is used. New commands can be entered
  while the child process* executes.

-------------------------------
- Examples:                   -
-             echo hello &    -
-             dir &           -
-------------------------------

        ==================
12.     Program Invocation*
        ==================

• Any input that does not correspond to the previous (11)
  commands will be interpreted as an executable child process*.
• subprocess.call() is used even though subprocess.run() is
  the newer, safer version. This is because of limitations.

---------------------------------------------------------
- for the following example, I have made a python file  -
- called test.py which includes the code:               -
-                                                       -
-             i = 0                                     -
-             while i < 4:                              -
-                 print("hello person {}".format(i))    -
-                 i += 1                                -
---------------------------------------------------------
- Examples:                                             -
-             python3 test.py                           -
-                                                       -
-             hello person 0                            -
-             hello person 1                            -
-             hello person 2                            -
-             hello person 3                            -
---------------------------------------------------------


---------------------------------------------------------
-       Bringing All The Shell Commands Together        -
---------------------------------------------------------
-          python3 myshell.py                           -
-          echo import time > x.py                      -
-          echo time.sleep(10) >> x.py                  -
-          python3 x.py &                               - 
-          echo hello                                   -
-          dir                                          -
-          echo environ > x.py                          -
-          echo pause >> x.py                           -
-          q                                            -
-          python3 myshell.py x.py                      -
-          python3 myshell.py                           -
-          help > x.py                                  -
-          cd ..                                        -
-          dir                                          -
-          clr                                          -
-          quit                                         -
---------------------------------------------------------

||DEFINITIONS||

1. batchfile
    • a computer file containing a list of instructions to be 
      carried out in turn.

2. child process
    • created by a parent process. It is a subprocess that
    is a clone of the process that made it. It terminates when
    it has ended.

3. directory
    • a logical section of a file system used to hold 
      files. Directories may also contain other directories.

4. invocation
    • means the execution of a program or function. Child
      process is executed by using the subprocess module.
      Subprocess.call() works in python3 or newer.

5. redirection
    • pointing data to a new output source. Myshell uses the
      terminal to display stdout. 
    • echo 'hello' displays 'hello' on the terminal. 
    • echo 'hello' > gg displays 'hello' in the file gg.

6. truncate
    • replace or overwrite data that is present in a file. This
      is possible with '>'. If gg had echo hello on the first
      line and we entered pause > gg, then echo hello is 
      deleted and pause replaces it.
