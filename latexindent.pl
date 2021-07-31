#!/usr/bin/env perl
use strict;
use warnings;
use Unicode::GCString;

my $gcs  = Unicode::GCString->new("hello world");
print $gcs->columns();

exit(0);
