# Guide to connect to the ARC cluster
ARC stands for Advanced Research Computing. Here we will cover how to log in, run jobs and export files. If you want further information visit https://rcs.ucalgary.ca/ARC_Cluster_Guide.

Note: You need to be at the University of Calgary or you should use their VPN if you are off-campus whenever you want to use ARC. 
Instructions to install the VPN: https://ucalgary.service-now.com/kb_view.do?sysparm_article=KB0030079

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
  
## How ARC works

- ARC cluster is a conglomeration of many different compute clusters or partitions. 
- Each partition has its own characteristics. 
- You need to choose use one partition to run your code (Exception: when you use your home directory to test your code, as we will see below)
- Each partition has different number of nodes. 
- In order to know the characteristics of each partition you can type arc.info in the terminal and the follow table will appear

 ```
 [username@arc ~]$ arc.info
 
 Partitions: 13 (bigmem, cpu2013, cpu2017-bf05, cpu2019, cpu2019-bf05, cpu2021, cpu2021-bf24, cpu2022, cpu2022-bf24, gpu-v100, lattice, parallel, single)


      ==============================================================================================
                     | Total  Allocated  Down  Drained  Draining  Idle  Inval  Mixed  Reserved
      ----------------------------------------------------------------------------------------------
              bigmem |     2          0     0        0         0     0      0      2         0 
             cpu2013 |    14          8     0        0         0     0      0      6         0 
        cpu2017-bf05 |    36          2     0        0         0     0      0     34         0 
             cpu2019 |    40         13     0        0         0     0      0     27         0 
        cpu2019-bf05 |    87         84     0        1         0     0      0      2         0 
             cpu2021 |    46         13     0        2         8     0      0     23         0 
        cpu2021-bf24 |     7          1     0        1         0     0      0      5         0 
             cpu2022 |    60          7     0        8         0     0      0     45         0 
        cpu2022-bf24 |     8          0     0        8         0     0      0      0         0 
            gpu-v100 |    13          0     0        0         0     0      0     13         0 
             lattice |   196        126     2       19         0    10      1     38         0 
            parallel |   576        102    74      143         0     0      0    253         4 
              single |   168         28    45        9         0    71      0     15         0 
      ----------------------------------------------------------------------------------------------
       logical total |  1253        384   121      191         8    81      1    463         4 
                     |
      physical total |  1253        384   121      191         8    81      1    463         4 
 
  ```

## How to run a job
### Directly from the Home directory 

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
It is always good to remove a module if you are no longer plan to use it, in order to avoid issues with the different languages (bash, python). 

```
module remove python/anaconda3-2018.12
```
### Using a script

Use it for your definitive code. Still, if there are some issues you'll figure it out. But it is always convinient to use a pre-tested code, which you know ther should not be any issues. And if there are issues you know is for something related to the cluster and not your code. 

Some information first on how ARC 



