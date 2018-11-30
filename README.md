# GitAPIVisual
A Python2 application that collects information about the programming languages used by a developer in their repositories.
It then displays this info in a variety of charts.

To setup install python flask and PyGithub.

$ pip install Flask
$ install PyGithub

Navigate to the directory and generate information for a user by typing.

$ python app.py username

If you don't include a username it will generate information on Mike Bostock, the creator of d3.js as a demo.
Open the local port it tells you it is running on, in a web browser. 
Since all the information is collected when the program is first run, it might take a while for organisations or users with lots of repositories. 
Once the data is collected you can navigate through the various graphs using the links without any lag.
In the event where you exceed your rate limit. You can pass an access tokken as a second argument in the command line.

You can test parts of the code by running

$ python testGitRetrieval.py

Sample screenshots of the program, with Mike Bostock's stats as of 30/11/18

