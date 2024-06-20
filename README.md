# Visitors CGI script

This script keeps track of the unique IP addresses who call this script. The IP address of the client is stored in a file if the address is unique (aka not in the file).

## installation

Copy **visitors.cgi** to your **cgi-bin** folder and make sure it has the executable bit set. Make sure the script have enough rights to the **cgi-bin** folder, because the file who keeps track of the unique IP addresses is located in the folder.

## Use

You can call this script from anywhere in your **HTML** files, I suggest using it in an **iframe** tag. 

By default it shows the number of unique visitors to the page. if the 'test' parameter is set to anything but 0 it shows some debugging info like 

    - is the client IP address unique?
    - number of unique visitors
    - the client's IP address

So the call looks somewhat like this

    https://your-website/cgi-bin/visitors.cgi

    or 

    https://your-website/cgi-bin/visitors.cgi?test=1

    