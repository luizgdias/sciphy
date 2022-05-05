# awk script to print number of characters used in each column.
# input can be phylip style but without first line

NF>=2&& !blocks{seqs++;name[seqs]=$1; seq[seqs]=$2;
for(i=3;i<=NF;i++)seq[seqs]=seq[seqs] $i}
NF==0{iseqs=0;blocks=1}
NF>=1&&blocks{iseqs++; seq[iseqs]=seq[iseqs] $1;
for(i=2;i<=NF;i++)seq[seqs]=seq[seqs] $i}
END{
  len=length(seq[1]);
  for(i=1;i<=len;i++){
    delete chars;
    nchars=0;
    for(j=1;j<=seqs;j++){
      found=0;
      for(k in chars){
        if(k==substr(seq[j],i,1)){
          chars[k]++;
          found=1;
        }
      }
      if(found==0) {
        chars[substr(seq[j],i,1)]=1;
        nchars++}
    }
     columns++; if(nchars==1) invariants++;
#    printf("%d\n",nchars);
  }
  print "";
}
#END{print invariants/columns}			#invariant sites number 


