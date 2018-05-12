#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use XML::Simple;
use HTML::Template;
use File::Basename;
use Data::Dumper; 

my $dir=dirname($0);
my $xmldesc=$dir."/descriptionDT.xml";
my $tmpldesc=$dir."/descriptionDT.tmpl";

my $xml = new XML::Simple;
my $descDT = $xml->XMLin($xmldesc, ForceArray => 1);

my $template = HTML::Template->new(filename => $tmpldesc, global_vars => 1);
$template->param(Colonne => $descDT->{'Colonne'});

$template->param(VALUES => '
											<option value="0">0</option>
											<option value="1">1</option>
											<option value="2">2</option>
											<option value="3">3</option>
											<option value="4">4</option>
											<option value="5">5</option>
											<option value="6">6</option>
											<option value="7">7</option>
											<option value="8">8</option>
											<option value="9">9</option>
											<option value="10">10</option>
											<option value="11">11</option>
											<option value="12">12</option>
											<option value="13">13</option>
											<option value="14">14</option>
											<option value="15">15</option>
											<option value="16">16</option>
											<option value="17">17</option>
											<option value="18">18</option>
											<option value="19">19</option>
');

print header,start_html(-title =>"PIG version 0.x",-head => [ Link( { -href => '/pig.css', -rel => 'stylsheet', -type => 'text/css'}) ]);

print $template->output;

use DBI;
my $dbh = DBI->connect('dbi:Pg:dbname=val;host=127.11.69.2','adminzbnp1nd','k2ytPuzXJARq',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

if (param()) {
	my @DTDESC;
	foreach my $p (param) {
		my $pp = param($p);
		if (($p =~ m/DTDESC/) && ($pp > 0)) {
			push @DTDESC,"$p:$pp";
		}
	}
	my $dtdesc = {desc => \@DTDESC};
	my $xs = XML::Simple->new(XMLDecl => 1, NoAttr => 1, RootName => "dt");
	my $xmlout = $xs->XMLout($dtdesc);
	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    my $nice_timestamp = sprintf ( "%04d%02d%02d %02d:%02d:%02d",$year+1900,$mon+1,$mday,$hour,$min,$sec);
    #my $rows = $dbh->do("INSERT INTO dt (idt, dtdesc) VALUES ($nice_timestamp, $xmlout)"); 
    my $SQL = q{INSERT INTO dt (idt, dtdesc) VALUES (?,?)};
    my $sth = $dbh->prepare($SQL);
    $sth->execute($nice_timestamp, $xmlout);
}

my $sth = $dbh->prepare("SELECT idt, dtdesc FROM dt");
$sth->execute();
while(my $ref = $sth->fetchrow_hashref()) {
    print pre("$ref->{'idt'} :: $ref->{'dtdesc'}\n");
}
$dbh->disconnect();

print end_html;
