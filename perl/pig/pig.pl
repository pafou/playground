#!/usr/bin/perl
use strict;
use warnings;
use XML::Simple;

use Data::Dumper; 

my @DTDESC = (
          'DTDESC:MSA:DB:Oracle:creation:5',
          'DTDESC:MSA:DB:Oracle:migration:4',
          'DTDESC:BI::RS:modification:7',
          'DTDESC:Technique::RRR:creation:3'
        );

my $dtdesc = {dtdesc => \@DTDESC};
my $xs = XML::Simple->new(XMLDecl => 1, NoAttr => 1, RootName => "dtdesc");
my $xmlout = $xs->XMLout($dtdesc);
print $xmlout;


