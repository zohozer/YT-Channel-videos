# YT-Channel-videos
Scans a Youtube channel for all available videos and prints the result in console and into an external file called "\_list.txt" into the same directory where the script it is located.

It requires as input a Youtube channel ID in the form of: "https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ" or "UCWr0mx597DnSGLFk1WfvSkQ".

It is using as dependency the ["scrapetube" PIP module](https://github.com/dermasmid/scrapetube) by [dermasmid](https://github.com/dermasmid) that can be installed by typing "pip install scrapetube" into console.

If you need only the videos IDs without the "https://www.youtube.com/watch?v=" part, comment the last but one line of code and uncomment the last line of code.
