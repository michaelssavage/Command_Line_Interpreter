# name: Michael Savage
# student ID: 17313526

import os
import sys
import subprocess

def main(args):
   # The main function works on the input. 
   # The function determines if a batchfile is in the command line or not.
   # If not, the function prepares to take in input.
   # /myshell is appended to the "shell" environment and is conveniently in bold.
   # The screen is cleared and a welcome message is displayed.
   if len(args) > 1:
       myshell(args[1])
   os.environ["SHELL"] = "\033[1m" + str(os.getcwd()) + "/myshell\033[0m"
   clr()
   print('Welcome. Type help (or ?) for more information. Enter a command to begin.\n')
   while True:
       currentDir = os.getcwd()
       args = getinput(currentDir)
       execute(args)

def myshell(fileIn):
   # this function is called if there is a batchfile.
   # for example, python3 myshell.py gg
   # gg is opened. each line is numbered and in bold.
   # each line will be executed.
   try:
       with open(fileIn, "r") as file:
           i = 1
           for line in file:
               print("\n\033[1mLine {} contains: \033[0m".format(i) + line)
               execute(line.split())
               i += 1
   except:
       print("File input error")
   raise SystemExit

def getinput(currentDir):
   # input is taken in and returned as list of arguments.
   line = input(currentDir + " >>> ").strip()
   args = line.split()
   return args

def execute(args):
   # try execute the args.
   # otherwise, generate EOF error.
   # output redirection on dir, environ, echo, & help.
   try:
       if len(args) == 0:
           pass
       # overwrite or append
       elif len(args) > 2 and (">" == args[-2] or ">>" == args[-2]):
           redirect(args[:-1], args[-1])
       # &
       elif "&" == args[-1]:
           p = subprocess.Popen(args[:-1])
           p.wait()
       # cd
       elif "cd" == args[0]:
           cd("".join(args[1:]))
       # clr
       elif "clr" == args[0]:
           clr()
       # dir
       elif "dir" == args[0]:
           dir("".join(args[1:]))
       # environ
       elif "environ" == args[0]:
           environ()
       # echo
       elif "echo" == args[0]:
           echo(" ".join(args[1:]))
       # help
       elif "help" == args[0] or "?" == args[0]:
           help()
       # pause
       elif "pause" == args[0]:
           pause()
       # quit
       elif "quit" == args[0] or "q" == args[0]:
           quit()
       else:
           childprocess(args)
   except EOFError as e:
       print("Error while trying to execute" + args)

def childprocess(args):
   # child process takes the form; python3 example.py
   try:
       subprocess.call([args[0],args[1]])
   except:
       print("Subprocess was not able to call [" + "] [".join(args) + "]")

def redirect(command, filename):
   # main overwrite that will deal with dir, environ, echo & help
   # the redirect will have parameters for the sign ( > or >> )
   # and parameter for the filename.
   try:
       if "dir" == command[0]:
           # redirect(command, sign, filename)
           redirect_dir("".join(command[1:-1]),command[-1],filename)
            
       elif "environ" == command[0]:
           # redirect(sign, filename)
           redirect_environ(command[-1], filename)
         
       elif "echo" == command[0]:
           # redirect(command, sign, filename)
           redirect_echo(" ".join(command[1:-1]),command[-1],filename)
         
       elif "help" == command[0]:
           # redirect(sign, filename)
           redirect_help(command[-1], filename)
       else:
           print("Output redirection unavailable for *" + " ".join(command[:-1]) + "*")
   except:
       print("Error while trying to execute" + command)

def cd(args):
   # Changes the current directory and updates the PWD environment variable.
   # otherwise, generate error message stating directory does not exist.
   try:
       if not args:
           currentDir = os.getcwd()
       else:
           os.chdir(args)
           os.environ["PWD"] = os.getcwd()
   except Exception as e:
       print("The directory path *" + args + "* is invalid or does not exist.")

def clr():
   # clear the whole terminal screen.
   print("\033c",end="")

def dir(args):
   # lists the contents of the directory.
   # if no directory given, current directory is used.
   try:
       if not args:
           args = "."
       content = "-----------------\n"
       for line in os.listdir(args):
           content += line + "\n"
       content += "-----------------"
       print(content)
   except:
       print("The directory *" + args + "* is invalid or does not exist")

def redirect_dir(args, sign, filename):
   # lists the contents of the directory to the output file.
   if not args:
       args = "."
   content = "-----------------\n"
   for line in os.listdir(args):
       content += line + "\n"
   content += "-----------------"
   if ">" == sign:
       with open(filename, 'w+') as f:
           f.write(content)
   else:
       with open(filename, 'a+') as f:
           f.write("\n" + content)

def environ():
   # lists the environ strings.
   # "shell" has /myshell appended to it.
   # PWD is updated with cd.
   environ = os.environ
   content = "-----------------"
   for k, v in environ.items():
       content += k + " = " + v + "\n"
   content += "-----------------"
   print(content)

def redirect_environ(sign, filename):
   # lists the environ strings to the output file.
   environ = os.environ
   content = ""
   for k, v in environ.items():
       content += k + "=" + v + "\n"
   if ">" == sign:
       with open(filename, 'w+') as f:
           f.write(content)
   else:
       with open(filename, 'a+') as f:
           f.write("\n" + content)

def echo(args):
   # prints the string out if args are given.
   # if no args are given, it will warn the user.
   content = "-----------------\n"
   if not args:
       content += "The echo command was given no arguments."
   else:
       content += args.rstrip()
   content += "\n-----------------"
   print(content)

def redirect_echo(args, sign, filename):
   # prints the argument given to the output file.
   # A warning is not printed out to the file.
   # instead, a blank space is printed.
   content = args.rstrip()
   if ">" == sign:
       with open(filename, 'w+') as f:
           f.write(content)
   else:
       with open(filename, 'a+') as f:
           f.write("\n" + content)

def help():
   # help file that has the capability of the more filter.
   # ? can be inputted for help too.
   # Use the space-bar to move forward.
   os.system("more README")

def redirect_help(sign, filename):
   # prints the whole content of the help file to the output file.
   f = open("README", "r")
   content = f.read()
   if ">" == sign:
       with open(filename, 'w+') as f:
           f.write(content)
   else:
       with open(filename, 'a+') as f:
           f.write("\n" + content)
   f.close()

def pause():
   # pauses the program until Enter is pressed.
   # anything on the keyboard can be pressed and will have no effect.
   print("-----------------")
   input("Shell paused.. Press 'Enter' to continue")
   print("-----------------")

def quit():
   # input can be "q" or "quit",
   # A thank you message is printed, and the shell exits.
   content = "-----------------\nThanks for using MyShell. Come back soon!\n-----------------"
   print(content)
   raise SystemExit

if __name__ == "__main__":
   # batchfile would represent sys.argv
   main(sys.argv)
