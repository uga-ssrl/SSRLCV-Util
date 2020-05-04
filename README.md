# SSRLCV Utitilities

The SSRLCV utilities are meant to help with debugging and data analysis of the SSRLCV output. This repository doees not included the SSRLCV library, the SSRLCV is maintained at [the SSRLCV gitlab page](https://gitlab.smallsat.uga.edu/payload_software/ssrlcv-utilities).

The programs are broken roughly into **IO** and **visualization**. IO helps with generating test cases or anylizing test data. Visualization helps with graphing and viewing test data.

### Recommended Additional Software Tools

* [MeshLab](http://www.meshlab.net/) - Critical for viewing the results of SSRLCV.
* [CloudCompare](https://cloudcompare.org/) - Useful for comparing ground truth models, the ICP algorithm within CC is great for this.


### Requirements and Depencies

* Python 3.*
* Numpy
* Matplotlib
* plyfile

# Included Programs

## IO Helpers

### `modPointCloud.py` -- simple point cloud modification

This program preforms simple point cloud modification. It scales, rotates, or translates an ASCII encoded point cloud

#### USAGE

Run the program with
```
python3 file.ply modPointCloud.py scale rotate_x rotate_y rotate_z translate_x translate_y translate_z
```
Where the arguments are:

* `file.ply   `  -- the PLY file to modify
* `scale      `  -- scales all points in point cloud by this ammount
* `rotate_x   `  -- in degrees, rotates all points around x axis this ammount
* `rotate_y   `  -- in degrees, rotates all points around y axis this ammount
* `rotate_z   `  -- in degrees, rotates all points around z axis this ammount
* `translate_x`  -- translates all points on x axis this ammount
* `translate_y`  -- translates all points on y axis this ammount
* `translate_z`  -- translates all points on z axis this ammount


### `raw_matches_to_matches.py` -- ***DEPRICATED*** anatomy of SIFT conversion

This program converts anatomy of SIFT "raw" matches into a format that can me easily viewed or scripted with. This is DEPRICATED and should be converted into python3; it is only incleded because of its potential usefulness for research.

to generate the [anatomy of SIFT]() matches, view the SSRL mirror of the repo for details. The following is the expected use:

```
./bin/sift_cli images/everest01.png > p01.kp; ./bin/sift_cli images/everest02.png > p02.kp; ./bin/match_cli p01.kp p02.kp > matches_raw.txt
```

## Data Visualization
