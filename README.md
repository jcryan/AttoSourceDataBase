# Database of Attosecond Light Sources
This database developed as part of a literature reveiew for our recent [book chapter](https://doi.org/10.1016/bs.aamop.2022.05.001) which presents a survey of existing lightsources with sub-femtosecond duration. The initial survey effort focused on isolated attosecond pulse (IAP) sources, but several notable attosecond pulse train (APT) demonstrations have now been included. The initial survey also focused on sources which reported both a meausred pulse energy (or photon flux) and a measurement of the pulse duration. We have tried to stick with this requirement, but we have included some notable achievements where either a photon flux or pulse duration measurement is missing.   

# The Database
The database consists of two dictionaries (HHGData and FELData) included in AttoSourceDB.py. These can be imported and used to generate plots. The keys of the dictionary are a unique identifer related to the bib reference (see citations). Each entry in the dictionary is a dictionary with keys:

'Duration': list of pulse durations measured in the reference

'PulseEng': A list of pulse energy described in the reference

'PhotonEng': A list of central photon energies for the source

'type': Is the source and isolated attosecond pulse ('IAP') or an attosecond pulse train ('APT'). 

'method': a dictionary describng the generation method and the meterology method. 

'Reference': a dictionay with entries for the first 'author', 'journal' name, 'vol', 'page', and 'year' information

# Plotting Tools
AttoSourcePlot.py contains a class AttoSourcePlot which has several attributes for filtering and plotting the database.
AttoSourceFig.py provides an example of how to use this class 

# Citations
If you use this tool for a publication, remember to cite the original work which describes the source. The keys of the HHGData and FELData dictionaries refer to cite keys in the included bib file (references/Attosecond Source List.bib). There is an additional example tex file to demonstrate the referencing.   
In addition to citing the original work, it is apperciated if you cite our [book chapter](https://doi.org/10.1016/bs.aamop.2022.05.001) in any publications where you use the database tools:
James P. Cryan, Taran Driver, Joseph Duris, Zhaoheng Guo, Siqi Li, Jordan T. O'Neal, Agostino Marinelli, Chapter One - The development of attosecond XFELs for understanding ultrafast electron motion, Editor(s): Louis F. DiMauro, Hélène Perrin, Susanne F. Yelin, Advances In Atomic, Molecular, and Optical Physics, Academic Press, Volume 71, 2022, Pages 1-64, https://doi.org/10.1016/bs.aamop.2022.05.001.

# New Submissions
We welcome suggestions for additional sources to include in the database. If you have find (or develop) a source not included in the database, please use this [simple form](https://forms.gle/GpaRaPvtotJV52QV6) to provide details, and we will be happy to include it. Please note, the database is largely focused on sources which produce pulse with sub-femtosecond duration, are published in peer-reviewed journals, and include a measurement of both the per-pulse energy and a pulse duration using an established method, for example linear streaking.    

# Acknowledgements
This work was supported by the U.S. Department of Energy (DOE), Office of Science, Office of Basic Energy Sciences (BES), Chemical Sciences, Geosciences, and Biosciences Division (CSGB).
![logo](./logos/SLAC-lab-hires.png)
# SLAC National Accelerator Laboratory
The SLAC National Accelerator Laboratory is operated by Stanford University for the US Departement of Energy.  
[DOE/Stanford Contract](https://legal.slac.stanford.edu/sites/default/files/Conformed%20Prime%20Contract%20DE-AC02-76SF00515%20as%20of%202022.10.01.pdf)
