#!/bin/bash

## minimizacao
# gmx grompp -f step6.0_minimization.mdp -o step6.0_minimization.tpr -c step5_input.gro -r step5_input.gro -p topol.top -n index.ndx;
# gmx mdrun -v -deffnm step6.0_minimization;

echo "DEU CERTO A PARTE DA MINIMIZACAO";
echo " ";
echo " ";
echo " ";


### Equilibrio
gmx grompp -f step6.1_equilibration.mdp -o step6.1_equilibration.tpr -c step6.0_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.1_equilibration;

gmx grompp -f step6.2_equilibration.mdp -o step6.2_equilibration.tpr -c step6.1_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.2_equilibration;

gmx grompp -f step6.3_equilibration.mdp -o step6.3_equilibration.tpr -c step6.2_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.3_equilibration;

gmx grompp -f step6.4_equilibration.mdp -o step6.4_equilibration.tpr -c step6.3_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.4_equilibration;

gmx grompp -f step6.5_equilibration.mdp -o step6.5_equilibration.tpr -c step6.4_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.1_equilibration;

gmx grompp -f step6.6_equilibration.mdp -o step6.6_equilibration.tpr -c step6.5_minimization.gro -r step5_input.gro -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step6.6_equilibration;


### Producao

gmx grompp -f step7_production.mdp -o step7.tpr -c step6.6_equilibration -p topol.top -n index.ndx;
gmx mdrun -v -deffnm step7 -nice 0;
