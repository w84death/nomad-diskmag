# Nomad Diskmag
![Floppy](screens/diskmag.gif)

E-zine on a 1.44 floppy tailored made on Raspberry Pi computer. 

## Issues

- Issue #0 04/2021 [IN PRODUCTION]


## Requiments

- python3
- pygame
- timidity 
- freepats
- (optional) pyinstaller
- (optional) 1.44MB FDD and a floppy drive

On Ubunu 20.04/Raspbian install those:
```apt install python3-pygame timidity freepats```
```python3 -m pip install pyinstaller```

![Raspi](screens/raspi-fdd.jpg)

## Running

Copy source files from the floppy to local harddrive.

### from sources

- ```cd Diskmag```
- ```python3 main.py```

### Building

```cd Diskag```
```./build.sh```

Binary will be in ```/dist/```. Run it using ```./Diskmag/Nomad_Diskmag_0```