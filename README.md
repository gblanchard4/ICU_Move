# ICU Move
django app to keep the ICU Move samples in order

## Installs
```
virtualenv env
source env/bin/activate
pip install django
pip install ipython
```

## Sample Types
* Stool
* Air
* Environment

## Sample Nomeclature
Format: {Type}-{ICU}-{Date}-{UID}

### Type
* A = Air
* S = Stool
* E = Environment

### ICUs
* M -> ILH M-ICU
* T -> ILH T-ICU
* O -> UMC Orange Tower-1 M-ICU
* P -> UMC Purple Tower-2 T-ICU S-ICU
* G -> UMC Green  Tower-3 Control ICU

### UIDs
#### Air
A-{tape color}-{ICS}{Side}-{MMDDYY}
#### Stool
S-{number}-{room}-{MMDDYY}
