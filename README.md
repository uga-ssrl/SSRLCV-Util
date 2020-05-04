# SSRLCV Utitilities

The SSRLCV utilities are meant to help with debugging and data analysis of the SSRLCV output. This repository doees not included the SSRLCV library, the SSRLCV is maintained at [the SSRLCV gitlab page](https://gitlab.smallsat.uga.edu/payload_software/SSRLCV) and [mirrored on github](https://github.com/uga-ssrl/SSRLCV).

The programs are broken roughly into **IO** and **visualization**. IO helps with generating test cases or anylizing test data. Visualization helps with graphing and viewing test data.

### Recommended Additional Software Tools

* [MeshLab](http://www.meshlab.net/) - Critical for viewing the results of SSRLCV.
* [CloudCompare](https://cloudcompare.org/) - Useful for comparing ground truth models, the ICP algorithm within CC is great for this.


### Requirements and Depencies

* Python 3.*
* Numpy
* Matplotlib
* plyfile

# IO Helpers

## `modPointCloud.py` -- simple point cloud modification

This program preforms simple point cloud modification. It scales, rotates, or translates an ASCII encoded PLY file.

### USAGE

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

The program oputputs a PLY file titled `modified.ply`

## ***DEPRICATED*** `raw_matches_to_matches.py` -- anatomy of SIFT conversion

This program converts anatomy of SIFT "raw" matches into a format that can me easily viewed or scripted with. This is  written in python 2.7 and is DEPRICATED; it should be converted into python3 and updated to output an encoded unity struct; it is only incleded because of its potential usefulness for research.

to generate the [anatomy of SIFT](https://gitlab.smallsat.uga.edu/Caleb/anatomy-of-sift) matches, view the SSRL mirror of the repo for details. The following is the expected use:

```
./bin/sift_cli images/everest01.png > p01.kp; ./bin/sift_cli images/everest02.png > p02.kp; ./bin/match_cli p01.kp p02.kp > matches_raw.txt
```

## ***INCOMPLETE*** `scan_camera_gen.py` -- scans the surface of the planet, rather than point tracking

This program generates position and orentation input for testing the camera parameters of a pushbroom scanner. The program is currently incompelte and needs additional contributions

### USAGE

Run the program with
```
python3 scan_orbit_camera_gen.py altitidue stepAngle numSteps
```
Where the arguments are:

* `altitidue   ` -- the altitidue of the circular orbit in km
* `scanDistance` -- the distance on earth to scan, in km
* `numImages   ` -- the number of images locations to produce during the scan

## `sumcut.py` -- determines if more points are on the left or right of csv histogram

Given a particular refrence point, this program determines if there are more points on the left of an input csv file. The input data is interpreted as unordered singluar values in a histogram.

### USAGE

Run the program with:
```
python3 sumcut.py file/path/to/file.csv cutoff \n
```
Where the arguments are:

* `file.csv      `-- a path to a csv file that you want to make a histogram of
* `cutoff number `-- a number which represend the cutoff value to sum either side of

## `test_point_generator.py` -- generates perfect matches for testing R2 -> R3 conversions

This programs generates prefect matches on the image planes of various cameras. It can be used the test if a conversion from the image plane to the real world coordinate system is working correctly. The test points are ouput as c++ / CUDA code which can be copy / pasted into a test program.

### USAGE

simply run the program:

```
python3 test_point_generator.py
```

Additions to give more arguments are parameters are welcome

## `track_orbit_camera_gen.py` -- generates test positions, orentations, and slews of cameras

This program generates example camera positions and orientations which can be used to test 3D reconstructions, and to make camera paramters for blenderGIS genereated test imagery.

This program also outputs slew rates for the given inputs. These slew rates are given from image to image and not as a whole.

### USAGE

Run the program with:
```
python3 track_orbit_camera_gen.py altitidue stepAngle numSteps
```
Where the arguments are:

* `altitidue` -- the altitidue of the circular orbit in km
* `stepAngle` -- the off angle from the point track normal
* `numSteps ` -- the numbers of angle steps to take 

# Data Visualization















<!-- end -->
