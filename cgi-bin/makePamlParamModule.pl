#!/usr/bin/perl -w  
#$ENV{CLUSTALDIR}='/usr/local/bin/clustalw';
use lib "/usr/local/bioperl-1.5.0";
use lib "/usr/local/bioperl-run-1.4";
use Bio::Tools::Run::Phylo::PAML::Yn00;
use Bio::AlignIO;
my $alignio = Bio::AlignIO->new(-format => 'phylip',
               		        -file   => '/disk1/home/kary/d_06/projeto/script/script_aa_pipeline/python/fasta/rh/rh_phy');
my $aln = $alignio->next_aln;

my $yn = Bio::Tools::Run::Phylo::PAML::Yn00->new();
$yn->alignment($aln);
my ($rc,$parser) = $yn->run();
while( my $result = $parser->next_result ) {
  my @otus = $result->get_seqs();
  my $MLmatrix = $result->get_MLmatrix();
  # 0 and 1 correspond to the 1st and 2nd entry in the @otus array
  my $dN = $MLmatrix->[0]->[1]->{dN};
  my $dS = $MLmatrix->[0]->[1]->{dS};
  my $kaks =$MLmatrix->[0]->[1]->{omega};
  print "Ka = $dN Ks = $dS Ka/Ks = $kaks\n";





