PythonClassRepository
=====================

Repository for learning Python and programming techniques via edx

When using Cloud9 use the following to commit files to GitHub and run the application in Cloud9 Terminal:

to run a file use Terminal Alt-t (View --> Terminal --> New Terminal)
type into the command line: python fileName.py

To check for untracked files:
    git add -A -n (The -A adds all untracked files and the -n make it a dryrun so they are not actually added)
To commit to GitHub:
    git add <file> (this adds the files to commit)
    git commit -am "commit message" (this adds the message to the commit)
    git push (this pushes the file to GitHub)

To pull changes from GitHub:
    git pull (updates cloud9 with latest GitHub files)
