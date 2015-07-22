# ICU Move
django app to keep the ICU Move samples in order

## Installs
```
virtualenv env
source env/bin/activate
pip install django
pip install django-grappelli
```

## Sample Types
* Stool
* Air
* Floor
* Door

## Sample Nomeclature
Format: {Type}-{ICU}-{Date}-{UID}

### Type
* A = Air
* D = Door
* F = Floor
* S = Stool

### ICU
* M = ILH M-ICU (1&2)
* T = ILH T-ICU
* P = UMC T/S-ICU
* O = UMC M-ICU 
* G = UMC Control ICU

### Date
* MMDD

###UID
Specialized for each sampletype

#### Air
* { [Tower] [Pump] [Side] [Day] }
  * Tower
    * M, T, P ,O, G 
  * Pump
    * 1-9
  * Side
    * A = Inside reception
    * B = Outside reception
  * Day
    * Correspond to day of study i.e. Aug 1 = 01

#### Door
* { [Tower] DC [Day] }
  *Tower 
    * M, T, P ,O, G
  * DC
    * “Door Combined”
  * Day
    * Correspond to day of study 
    
#### Floor
* { [Tower] FC [Day] }
  * Tower 
    * M, T, P ,O, G
  * FC
    * “Floor Combined”
  * Day
    * Correspond
