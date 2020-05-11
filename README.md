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

---

# IO Helpers

---

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

---

## ***DEPRICATED*** `raw_matches_to_matches.py` -- anatomy of SIFT conversion

This program converts anatomy of SIFT "raw" matches into a format that can me easily viewed or scripted with. This is  written in python 2.7 and is DEPRICATED; it should be converted into python3 and updated to output an encoded unity struct; it is only incleded because of its potential usefulness for research.

to generate the [anatomy of SIFT](https://gitlab.smallsat.uga.edu/Caleb/anatomy-of-sift) matches, view the SSRL mirror of the repo for details. The following is the expected use:

```
./bin/sift_cli images/everest01.png > p01.kp; ./bin/sift_cli images/everest02.png > p02.kp; ./bin/match_cli p01.kp p02.kp > matches_raw.txt
```

---

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

---

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

---

## `test_point_generator.py` -- generates perfect matches for testing R2 -> R3 conversions

This programs generates prefect matches on the image planes of various cameras. It can be used the test if a conversion from the image plane to the real world coordinate system is working correctly. The test points are ouput as c++ / CUDA code which can be copy / pasted into a test program.

### USAGE

simply run the program:

```
python3 test_point_generator.py
```

Additions to give more arguments are parameters are welcome

---

## `track_orbit_camera_gen.py` -- generates test positions, orentations, and slews of cameras

Perhaps the most useful util program for testing. This program generates example camera positions and orientations which can be used to test 3D reconstructions, and to make camera paramters for blenderGIS genereated test imagery.

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

An example is to take 3 images at 400km with a 15 degree off angle for each is:

```
python3 track_orbit_camera_gen.py 400 15 3
```

### Use for Pointing Budget

The script produces some values that are usable for pointing and controls bounding. The scrip will output the follwing values (in order)

* `orbit angle  ` (rad): The angle a stingle `stepAngle` defined above makes with the center of mass of the orbiting body
* `input angle  ` (rad): The given input angle `stepAngle` converted to radians
* `orbit arclen ` (km): The arc length of the orbit path
* `ground arclen` (km): The arc length of the ground path
* `velocity     ` (km/s): The orbital velocity at the `altitidue`
* `slew time    ` (s): The total time it take to slew between **one** set of images. To get a total slew time multiply this by `numSteps` defined above

The script also produces slew rate values between **one** set of images.

* `Tracking Slews`: These slews are tracking (by pointing directly at) an arbitrary point on the surface of the orbiting body
	* `slew rate` (rad/s): the slew rate between **one** set of images
	* `slew rate` (deg/s): the slew rate between **one** set of images
* `Nadir Slews`:
	* `slew rate` (rad/s): the slew rate between **one** set of images
	* `slew rate` (deg/s): the slew rate between **one** set of images


---

# Data Visualization

---

## `2dplotcsv.py` -- plots a csv file

This program accepts a list of values and plots them in that order. The input values must be an ASCII encoded csv file

### USAGE

Run the program with:
```
python3 2dplotcsv.py file/path/to/file.csv xlabel ylabel
```
Where the arguments are:

* `file.csv` -- a path to a csv file that you want to graph
* `xlabel  ` -- a string to label the x axis
* `ylabel  ` -- a string to label the y axis


---

## `bundle_adjustment_tests_viewer.py` -- view a plot of the minimization process of bundle adjustment

This program plots values that are output during a tests of bundle adjustment. This helps a programmer view convergences to an optima, how long these convergences take, and when they fail. To have the nessesary outputs for graphin this debug needs to be enabled within bundle adjustment. A graph of the optimizations is produced as an output.

The script is graphing multiple csv files what are of the form `$$$Errors.csv` where the `###` indicates and integer run number of a specific bundle adjustment test.

### USAGE

Run the program with:
```
python3 bundle_adjustment_tests_viewer.py file/path/to/ba/tests/ badRunCut OptimalVal
```
Where the arguments are:

* `directoryPath`  -- a directory path
* `badRunCut    `  -- A value representing a bad run
* `OptimalVal   `  -- A value representing the optimal value

---

## ***DEPRICATED*** `disparity.py` -- shows a disparity map from dense matches

Used in disparity testing, this script is now depricated. It could still be used to generate example disparities.

---

## `feature_vector_plot.py` -- draws feature vectors over an image segment

This program draws arrows that represent vectors over each pixel in the input image. The input image should be small and ideally square. An input image of 25 by 25 pixels is the largest size that should realistically be used. This should be used to view example HOGS or SIFT discriptors.

### USAGE

Run the program with:
```
python3 feature_vector_plot.py /path/to/image
```
Where the arguments are:

* `imagePath`  -- a directory path including the image


---

## `logGrapher.py` -- graphs SSRLCV logger power, voltage, current, and state output

This allows a programmer to view the state transitions, voltage, current, and power draw over time as an SSRLCV pipeline is executed. These values are graphed if enabled. This is encredibly useful for power budget related things.

The program reads the `ssrlcv.log` file which leaves tags for state, power, voltage, and current. This could be extended to graph thermal output as well. The output is visually graphed.

### USAGE

Run the program with:
```
python3 logGrapher.py file/path/to/log.csv enableStates enableVoltage enableCurrent enablePower
```
Where the arguments are:

* `file.csv     `  -- a path to the log file
* `enableStates `  -- Graph the state transitions of the pipeline
* `enableVoltage`  -- Graph the voltage of the system over time
* `enableCurrent`  -- Graph the voltage of the system over time
* `enablePower  `  -- Graph the wattage of the system over time

---

## `logTimes.py` -- analyzes runtimes between SSRLCV pipeline states

This program retuns accurate runtimes for states of the pipeline. This is used to measure how long feature detection, extraction, and matching takes. It is used to measure how long triangulation, filtering, and bundle adjustment take.

### USAGE

Run the program with:
```
python3 logTimes.py file/path/to/log.csv
```
Where the arguments are:

* `file.csv`       -- a path to the log file

### Use in precise timing

The program outputs the following precise timing of SSRLCV:

* `   Total Runtime`: The total time taken to run the pipeline in ms
* ` Seed Image Time`: The time taken to generate seed image features in ms
* `Feature Gen Time`: The time taken to generate features in ms
* `   Matching Time`: The time taken to match features in ms
* `Triangulate Time`: The time taken to triangulate in ms
* `  Filtering Time`: The time taken to filter in ms
* ` Bundle Adj Time`: The time taken in bundle adjustment in ms

---

## `match_plotter.py` -- view matched points between images

This program visualizes matched points between images. It shows the location on one image where the feature is located and draws a line to the feature on the corresponding image.

### USAGE

Run the program with:
```
python2 match_plotter.py -m matches -1 image1 -2 image2
```
Where the arguments are:

* `-m matches` the path and file location of a CSV encoded matches file
* `-1 image1` the path and file location of image 1 in the matched set
* `-2 image2` the path and file location of image 2 in the matched set

---

## `multi_match_plotter.py` -- view matched points between several images

TODO

### USAGE

TODO

---

## `plot_sensitivities.py` -- plot bundle adjustment sensitivities

This program should be used with the `generateSensitivityFunctions()` method in SSRLCV. This allows the programmer to analyze the practical objective functions. Hopefully, the programmer will notice these objective functions follow a specific patter or are differentable.

The nessesary CSV files are generated within the `generateSensitivityFunctions()` method, the `partialFilename` is sepcified there. 6 graphs are generated.

### USAGE

Run the program with:
```
python3 plot-sensitivity.py file/path/to/partialFilename xlabel ylabel
```
Where the arguments are:

* `partialFilename` -- a path with a PARTIAL filename, which does not inclde the _Delta######.csv part
* `xlabel         ` -- a string to label the x axis
* `ylabel         ` -- a string to label the y axis

---

## `plot-x-y.py` -- plot 2D CSV data

This method plots paired CSV encoded data. Each value in the CSV is encoded as `x,y\n` with a newline character after each entry.

### USAGE

Run the program with:
```
python3 plot-x-y.py file/path/to/file.csv xlabel ylabel
```
Where the arguments are:

* `file.csv` -- a path to a csv file that you want to graph
* `xlabel  ` -- a string to label the x axis
* `ylabel  ` -- a string to label the y axis

---

## `plotHistogram.py` -- plot CSV data as a histogram

This program will plot CSV data to be seen as a histogram. The program takes a set of CSV encoded values (all on the same line) and plots them as desired.

### USAGE

Run the program with:
```
python3 plotHistogram.py file/path/to/file.csv bin# xlabel ylabel
```
Where the arguements are:

`file.csv` -- a path to a csv file that you want to make a histogram of
`bin#    ` -- an integer representing the number of bars you want in the histogram
`xlabel  ` -- a string to label the x axis
`ylabel  ` -- a string to label the y axis
`xlimit  ` -- the x limit of the chart, if 0 there will be no limit







<!-- end -->
