# WTmetaD-for-homogeneous-condensation

This repository contains LAMMPS (version 23 June 2022) and PLUMED (v2.8) scripts used in our publication in JCP (Zhong et al., J. Chem. Phys. 160, 124303 (2024); doi: 10.1063/5.0189448).
The well-tempered metadynamics enhanced sampling is adopted to compute the free energy profiles related to the phase change phenomena.
The scripts in chemicalPotentialDifference file can be used to compute the chemical potential difference in liquid-to-vapor transition under a certain system temperature with the canonical ensemble(NVT). The chemical potential difference is determined by the slope of the free energy VS #Atoms like gas.
The scripts in clusterFormationFreeEnergy file can be used to compute the free energy profile VS #Atoms like gas in the homogeneous condensation process under a certain system temperature and a certain initial supersaturation with the canonical ensemble(NVT).
We've included more details in the reference above. Note that other useful Python scripts to post-process the nucleation rates and critical nucleus sizes using LAMMPS Dump files can be found in another repository (https://github.com/ZSHtju/Postprocessing-cluster-with-LAMMPS-atom-trajectory). 
If you have any problem using the scripts, please don't hesitate to email me. 
