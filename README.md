# Guide to connect to the ARC cluster
ARC stands for Advanced Research Computing. Here we will cover how to log in, run jobs and export files. If you want further information visit https://rcs.ucalgary.ca/ARC_Cluster_Guide.
## How to log in
### For Linux/macOS users open the terminal and type
```
ssh username@arc.ucalgary.ca
```
### For windows users use MobaXterm and type

```
ssh -X username@arc.ucalgary.ca
```

where the **username** is your University of Calgary username. 

You can download MobaXterm here  https://mobaxterm.mobatek.net/.


## Directories

There are two main directories

- **Home directory (/home or ~)**

  - It is the one you are logged in by default. 
  - You have 500 GB quota & 200,000 file limit. 
  - Your data here does not get erased after a time. 

  It looks like this in the terminal:

   ```
  [username@arc ~]$
  ```
  To access to your data
   ```
  [username@arc ~]$ cd data
  [username@arc data]$
  ```


- **Temporary directory (/scratch)** 

  - Use this directory to temporary store large files. 
  - Here all files we'll be deleted after 5 days your job finalizes. 
  - 15 TB quota & 250,000 file limit. 
  
  It looks like this in the terminal:

   ```
  [username@arc scratch]$ 
  ```

## How to run a job

1. Directly from the Home directory 

Use it for programm testing

  **Important considerations**
  - There is no memory allocation
  - There is no time specification
  - It is meant for short sessions (no longer than 15 min) requiring few memory 
 

```
ssh username@arc.ucalgary.ca
[username@arc ~]$ cd data
[username@arc data]$ cd test
[username@arc test]$ module load python/anaconda3-2018.12
[username@arc test]$ python lorenz.py
```





