"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
 
# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
#print('Number of arguments:', len(sys.argv), 'arguments.')

#print("the script has the name %s" % len(sys.argv)) 
# get command line argument length.
#argv_len = len(sys.argv)
#print('there are ' + str(argv_len) + ' arguments.')
# loop in all arguments.
#for i in range(argv_len):
  #tmp_argv = sys.argv[i]
  # print out argument index and value.
  #print(str(i))
  #print(tmp_argv)
 #print('argv ' + str(i) + ' = ' + tmp_argv)
# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())