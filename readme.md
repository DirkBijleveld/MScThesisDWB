<h3 align="center">MSc Political Science Thesis</h3>

  <p align="center">
    Methodology for defection scores on the European Parliament
  </p>

<!-- USING EXEC.PY -->
## Replicating findings

This software is designed to run with a single operation and provide identical results to what is used in the MSc thesis: "Defection in the European Parliament: Far-Right & Eurosceptic Parties and the Principal-Agent Problem" 

<!-- code block python -->
```sh
python exec.py full
```
Requires the original .xlsx as downloaded from the VoteWatch website. Some changes must be made to some files. Instructions can be found in data/downloads/readme.txt

Individual operations can be run by replacing 'full' with the following commands:

```sh
python exec.py intermediary session=<session number>
```

```sh
python exec.py clean session=<session number> filter_legislative=<true/false>
```
```sh
python exec.py defection session=<session number>
```

```sh
python exec.py prep session=<session number>
```

The final defection data .csv will be found in data/meps/EP<id>_RCVs_MEPS.csv

Some other commands can be used to interpret data:

```sh
python exec.py regression session=<session number> party=<true/false> group=<true/false> eurosceptic=<true/false> 
```
```sh
python exec.py boxplot session=<session number> party=<true/false> group=<true/false> eurosceptic=<true/false> 
```
```sh
python exec.py correlation session=<session number>
```