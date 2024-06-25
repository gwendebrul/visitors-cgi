#!/usr/bin/perl

# this first use declaration is needed by my server to correctly function
# comment out if needed
#use cPanelUserConfig;

# These next use declarations are standard
use warnings;
use strict;

# The next use declaration must be downloaded (not standard)
use CGI;

my $q = CGI->new;

# This prints the html header necessary for correct use of this script
print $q->header;

# Get ip address of the client connecting to this script
my $ip = $ENV{REMOTE_ADDR};

# $is_unique variable is a flag to set if the client is a unique visitor
# This means that it's IP address is stored in the 'ips.txt' file
my $is_unique = 1;

# the location to the file which contains the unique IP addresses
my $ips_file = "./ips.txt";

# contains the number of IP addresses in the 'ips.txt' file
my $number_of_ips = 0;

# This sets the '$is_test' variable to decide what to print
my $is_test = $q->param('test') || 0;

# The file handle for the '$ips.txt' file
my $IPS;

# check if file exists, if not create file
unless (-e $ips_file) {
	open $IPS, ">", $ips_file;
	close($IPS);
}

# open '$ips.txt' for reading
my $file_opened = open ($IPS, "<", $ips_file);

# If there's an error opening the ips.txt file this should catch it
if ($file_opened != 1) {
	print "error opening file!<br> msessage: $! => $ips_file<br>";
	exit(0);
}

# In this while loop the client's IP address is matched with any of the
# IP addresses in the '$ips.txt' file.
# If there's a match then the client is a returning visitor and not unique.
# At the same time count the number of unique IP addresses in the file
while (<$IPS>) {
	$is_unique = 0 if /$ip/;	
	$number_of_ips++;
}

close($IPS);

# This next block is executed when an IP address is unique 
# It appends the IP address to the 'ips.txt' file
if ($is_unique) {
	open $IPS, ">>", $ips_file;
	print $IPS "$ip\n";	
	close($IPS);
	$number_of_ips++;
}

# if param 'test' is set to any value besides 0 the next few prints will be shown
print "unique: $is_unique<br>" if ($is_test != 0);
print "unique visitors: $number_of_ips<br>" if ($is_test != 0);
print "IP: $ip<br>" if ($is_test!= 0);

# default is to show number of unique visitors (if param 'test' is set then it will not show this)
print "<div class='visitors'>$number_of_ips</div>" if ($is_test == 0);