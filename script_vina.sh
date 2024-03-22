#!/bin/bash


#for (my $i=1;$i<101;$i++){
#	system("vina --receptor LTP12_870.pdbqt --ligand target_lipid.pdbqt --center_x 28 --center_y 15 --center_z 10 --size_x 25 --size_y 25 --size_z 25 --exhaustiveness 8 --out LTP12_870_as_receptor$i --log LTP12_870_as_receptor_$i.log");
#}

for i in {1..6};do
	vina --receptor 4h4f.pdbqt --ligand Pept_14aa.pdbqt --center_x 58 --center_y 60 --center_z 58 --size_x 29 --size_y 47 --size_z 15 --exhaustiveness 8 --out 4h4f_as_receptor$i.pdbqt --log 4h4f_as_receptor_$i.log --cpu 12
done
