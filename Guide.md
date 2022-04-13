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
- You need to choose one partition to run your code (Exception: when you use your home directory to test your code, as we will see below)
- Each partition has different number of nodes. 
- In order to know current state of each partition you can type **arc.info** in the terminal and the follow table will appear

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
  
 - Each partition has both a memory request and a time limit. Look for that here: 
 https://rcs.ucalgary.ca/ARC_Cluster_Guide#Selecting_a_Partition 
 - The command **sinfo** allows you to see the time limit each partition has directly on the terminal
  ```
 [username@arc ~]$ sinfo
 
 PARTITION    AVAIL  TIMELIMIT  NODES  STATE NODELIST
single          up 7-00:00:00      6 drain* cn[001,039,041,043-044,133]
single          up 7-00:00:00     45  down* cn[015,029-038,042,045-056,061-080,139]
single          up 7-00:00:00      3  drain cn[002-003,096]
single          up 7-00:00:00      9    mix cn[008,021,081,085,088,092,095,097,138]
single          up 7-00:00:00      2  alloc cn[009,137]
single          up 7-00:00:00    103   idle cn[004-007,010-014,016-020,022-028,040,057-060,082-084,086-087,089-091,093-094,098-132,134-136,140-168]
lattice         up 7-00:00:00      1  inval cn194
lattice         up 7-00:00:00     14 drain* cn[186,229-230,232-233,274,281-282,286,288-292]
lattice         up 7-00:00:00      1  down* cn272
lattice         up 7-00:00:00      5  drain cn[195,220,241,300,364]
lattice         up 7-00:00:00      8    mix cn[225,231,236,263,273,275,316,351]
lattice         up 7-00:00:00     76  alloc cn[169,173-176,182-185,196-199,221-224,237-240,242-259,267-270,301-315,329-346]
lattice         up 7-00:00:00     90   idle cn[170-172,177-181,187-193,200-219,226-228,234-235,260-262,264-266,271,276-280,283-285,287,293-299,317-327,347-350,352-363]
lattice         up 7-00:00:00      1   down cn328
parallel        up 7-00:00:00    110 drain* cn[0532,0538,0544,0561,0576,0580-0600,0602-0603,0614,0640,0644,0647,0651,0659,0663,0674,0685,0691,0694,0751,0755,0767-0768,0773-0780,0782,0788,0798,0801-0804,0807,0873,0880-0881,0883,0886,0898,0902,0906-0907,0918,0922,0925-0928,0951,0957-0958,0969-0970,0977,0982,0989-0992,0997,1001,1011,1019,1023-1024,1029,1035,1038-1039,1041-1043,1047,1049,1053-1055,1057,1063,1076,1080-1081,1086,1091]
parallel        up 7-00:00:00     72  down* cn[0553-0556,0569,0571,0575,0615,0621,0624,0627,0630,0658,0664,0668,0680,0686,0690,0698,0708,0716,0723-0724,0743,0747,0750,0765,0786,0792,0794-0795,0799,0805-0806,0825,0836,0861,0889,0904,0908-0909,0915,0921,0932,0945-0948,0952,0959,0962,0964,0993,0999,1002,1010,1025-1026,1032,1037,1040,1048,1056,1058,1069,1074,1077,1082,1085,1093-1095]
parallel        up 7-00:00:00     33  drain cn[0516,0530,0568,0573,0609,0622,0642,0670,0693,0699,0701,0721,0727-0728,0730,0735-0736,0764,0790,0800,0817,0826,0828,0831,0839,0858,0860,0872,0879,0884,0919,0930,0933]
parallel        up 7-00:00:00      4   resv cn[0893,0897,1000,1033]
parallel        up 7-00:00:00     79    mix cn[0520,0525-0526,0539,0541,0543,0557,0559,0605,0607,0613,0617-0618,0631,0633-0636,0653,0666-0667,0672-0673,0676,0702-0704,0706,0712-0713,0726,0732-0733,0744-0746,0756-0758,0762,0783-0784,0811,0814-0815,0822,0827,0829-0830,0843,0846,0849,0853-0854,0862-0863,0887,0943,0961,0963,0968,0976,0985-0986,0994,1003,1017-1018,1034,1044,1050,1060,1064,1071,1073,1083,1090,1092,1096]
parallel        up 7-00:00:00    206  alloc cn[0513-0515,0517-0519,0521-0524,0527-0529,0531,0533-0537,0540,0542,0562-0567,0570,0572,0574,0577-0579,0601,0604,0608,0610-0612,0616,0619,0623,0625,0629,0637-0639,0641,0645-0646,0648-0649,0654-0657,0660-0662,0677-0679,0682-0684,0687-0689,0695-0697,0700,0705,0709-0711,0714-0715,0717-0720,0722,0731,0734,0737,0739-0742,0749,0752-0754,0761,0763,0766,0769-0772,0785,0787,0789,0791,0797,0808,0813,0816,0818-0821,0823-0824,0832-0835,0837-0838,0840-0842,0847,0850-0851,0855-0857,0859,0865,0867-0871,0875,0877,0882,0885,0891-0892,0895,0899-0901,0903,0905,0910,0912,0914,0916,0923-0924,0929,0931,0934-0940,0949-0950,0953-0956,0965-0967,0971-0974,0980-0981,0983,0996,1004-1009,1013-1014,1020-1022,1027-1028,1030-1031,1051-1052,1065,1068,1070,1075,1078-1079,1087,1089]
parallel        up 7-00:00:00     70   idle cn[0558,0560,0606,0620,0626,0628,0632,0643,0650,0652,0665,0669,0671,0675,0681,0692,0707,0725,0729,0738,0748,0759-0760,0781,0793,0796,0809-0810,0812,0844-0845,0848,0852,0864,0866,0874,0876,0878,0888,0890,0894,0896,0911,0913,0941-0942,0944,0960,0975,0978-0979,0984,0987-0988,0995,0998,1012,1015-1016,1036,1045-1046,1059,1061-1062,1066-1067,1072,1084,1088]
parallel        up 7-00:00:00      2   down cn[0917,0920]
cpu2019*        up 7-00:00:00     27    mix fc[22-27,29,31-33,35-38,41-44,46,50-51,53-54,56-58,61]
cpu2019*        up 7-00:00:00     13  alloc fc[28,30,34,39-40,45,47-49,52,55,59-60]
cpu2021         up 7-00:00:00      2 drain* mc[47-48]
cpu2021         up 7-00:00:00      9   drng mc[15,24-27,35-36,39,46]
cpu2021         up 7-00:00:00     22    mix mc[3-12,16,18-19,23,31-32,34,37-38,40-41,43]
cpu2021         up 7-00:00:00     12  alloc mc[1-2,13-14,17,20-22,29-30,42,44]
cpu2021         up 7-00:00:00      1   idle mc45
cpu2022         up 7-00:00:00      8 drain* mc[113-116,121-124]
cpu2022         up 7-00:00:00      1   drng mc74
cpu2022         up 7-00:00:00     25    mix mc[65-69,72-73,86,88-94,98-99,108-112,117-119]
cpu2022         up 7-00:00:00     26  alloc mc[70-71,75-85,87,95-97,100-107,120]
cpu2013         up 7-00:00:00      9    mix h[1,3,5-6,9-11,13-14]
cpu2013         up 7-00:00:00      3  alloc h[2,7-8]
cpu2013         up 7-00:00:00      2   idle h[4,12]
gpu-v100        up 1-00:00:00     13    mix fg[1-13]
bigmem          up 1-00:00:00      2    mix fm[1-2]
cpu2022-bf24    up 1-00:00:00      8  drain mc[57-64]
cpu2021-bf24    up 1-00:00:00      1  drain mc52
cpu2021-bf24    up 1-00:00:00      5    mix mc[49,51,53-55]
cpu2021-bf24    up 1-00:00:00      1  alloc mc50
cpu2019-bf05    up    5:00:00      1  drain fc85
cpu2019-bf05    up    5:00:00      9    mix fc[4,8,18-21,80,91,107]
cpu2019-bf05    up    5:00:00     75  alloc fc[1-3,5-7,10,12-17,62-79,81-84,86-90,92-106,108-127]
cpu2019-bf05    up    5:00:00      2   idle fc[9,11]
cpu2017-bf05    up    5:00:00     20    mix s[1-15],th[4,6,8,12,17]
cpu2017-bf05    up    5:00:00      1  alloc s16
cpu2017-bf05    up    5:00:00     15   idle th[1-3,5,7,9-11,13-16,18-20]
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
Once you know your code works, it is convinient to send it using a script. 
- In this script you specify the partition you will use, the memory and the time it will need to run. 
- You can send it for one set of parameters or for several set of parameters.
- Your script needs to end with the termination **.slurm**
- Example: https://github.com/mariamasoliver/connect_to_ARC/blob/main/script.slurm

### Before running the script
For this specific script, you should create before running it, three folders:
- Results
- Out
- Report


#### How to run the script
From your Home directory
 ```
  ssh username@arc.ucalgary.ca
  [username@arc ~]$ cd data
```
You cd to the folder containing your script and your code. Both have to be saved on the same folder.
```
  [username@arc data]$ cd test

```

If you already specified the input in the script, or its input independent run it like
```
  [username@arc test]$ sbatch script.slurm

```
If its input dependent
```
  [username@arc test]$ sbatch --array=1,2,3,....,N script.slurm

```

where 1,2,3...,N are the set of your parameters. They have to be **integers**. You should adapt your code accordingly. 

Tomorrow add:
You can check the state of your programs runnings like this

You can check - while the program running- some memory information

