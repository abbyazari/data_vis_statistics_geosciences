# Frequently Asked Questions 
This file contains groupings of commonly asked questions and resources with regards to Python, visualization, and statistics. 

# Getting Started 

<details>
 <summary> 
  I'm new! Where do I begin?
 </summary>

 - If you are new to programming or new to Python: I reccomend going through each lab in the order it is presented. Lab 1 and beyond. Each one builds off the other. 
 - Go ahead and download the whole repository and work through it at the pace that feels right. I reccomend weekly lab time just so that it stays fresh! You can get Python for FREE through either through the Canopy or the Anaconda distribution. The labs were made and tested with the Anaconda distribution. 
- This is a course at the University of Michigan. If you are currently at UM, check out the course number Climate and Space 405 - 002 (To Be Updated as of 2018 to finalized course number)
</details>

<details>
 <summary> 
  I'm here to learn Python code in space science / climate science. Where do I begin?
 </summary>
 
 - Lab 1 has a lot of what you need to get started. Begin there then pick and choose what labs you would like after that but make sure to start with Lab 1 as it has a lot of the basics of Python oddities in there. 
 
 - Prof. Dan Welling also has posted an extensive introduction to Python and SpacePy on http://www-personal.umich.edu/~dwelling/python/. 
 
 - Prof. Karen Shell teaches a 300 level Climate Data Analysis class at Oregon State University which can be found at https://github.com/karenshell/climate-data-class.
 
 - Prof. S.-H. Dan Shim has posted several notebooks on getting started in different areas at https://www.danshimlab.info/resources/studying-jupyter-python.
</details>

<details>
 <summary> 
  I'm at the University of Michigan and want to see what other classes there are around?
 </summary>
 
 - This class is a good place to start at the upper level undergrad / graduate level on statistics and data analysis in Python. Below I list similar level classes with a different focus as well as follow on classes that are at more advanced levels. I also reccomend checking out the MIDAS certificate approved courses [here](https://midas.umich.edu/certificate/approved-courses/).

   <details>
    <summary> 
      Similar level courses with a different flavor: 
    </summary>
 
    - STATS 412 Introduction to Probability & Statistics -- More theory based and introductory stats
    - STATS 451 Bayesian Data Analysis -- Less visualization, more theory, more Bayesian
    - EAS 538 Natural Resource Statistics -- In R rather than Python, Earth focused
    - [Ross Big Data Summer Camp](https://icosbigdatacamp.github.io/) -- This is not for credit but is a 1 week crash course.
    - ALA 470 [Introduction to Data Visualization](https://www.lib.umich.edu/instruction-and-workshops/library-courses)
    - IOE 410 Advanced Optimization Methods -- More optimization, less statistics.  
    </details>
    <details>
     <summary> 
      More advanced courses:
     </summary>

    - EECS 505 Computational Data Science
    - EECS 545 Machine Learning 
    - TO 640 Big Data Management: Tools and Techniques
    - EECS 402 Programming for Scientists and Engineers
     </details>

</details>
 
<details>
  <summary> I'm here from space science and I've heard talk about SpacePy, astroPy, SunPy etc?
  </summary>
 
- Go check out the Python in Heliophysics community pages and projects at https://heliopython.org/projects/.
</details>

<details>
  <summary> I'm here from climate science and am most familiar with NCL. Where should I look?
  </summary>
 
- NCAR has moved toward Python for future development. Go check out their roadmap and report [here](http://www.ncl.ucar.edu/Document/Pivot_to_Python/NCL_Pivot_to_Python_Report_and_Roadmap.pdf). If you are ready to dive in start with [Lab 6](https://github.com/astro-abby/data_vis_statistics_geosciences/blob/master/Lab6/Lab6_MappingSeaIce.ipynb) which covers netCDF files and geolocated data. I also reccomend seeing the NCAR supported transition documentations providing NCL to Python comparisons at the following links:

- [Transition Guide](http://www.ncl.ucar.edu/Document/Manuals/NCL_to_Python/Transition_Guide_NCL_PyNGL.pdf)
- [Quick Look Applications](http://www.ncl.ucar.edu/Applications/NCL_to_Python/)
</details>


<details>
  <summary> I'm here from social sciences. Where should I start?
  </summary>
 
- Make sure you check out the [ICOS Big Data Camp](https://icosbigdatacamp.github.io/2018-summer-camp/) resources from the most recent camp in 2018. They include note only a subset of this course but also a full week long series of seminars and workshops. It will be held again in the spring of 2019 at University of Michigan. 
</details>

<details>
  <summary> I'm here from using ArcGIS. What types of things can Python do for me?
  </summary>
 
- Make sure you check out the ArcPY package. As stated in their [documentation](https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm) "ArcPy is a Python site package that provides a useful and productive way to perform geographic data analysis, data conversion, data management, and map automation with Python".

</details>

# General Programming

<details>
  <summary> I'm feeling overwhelmed writing my own code. How do I start this? 
  </summary>
 
  - Coding is not a profession that runs on natural talent - it's all about learning, making mistakes, and learning more. You iterate constantly. Most of coding is an iterative process where you try, receive an error, and try again. Errors are a natural part of programming. You should expect to have your notebooks throw errors at you and to then figure out how to fix them. As you code you will need to use resources such as the help() function, resources you find in books and online including these notebooks here! I wanted to share with you an outline to get started writing your own code that I've found particularly useful: 

- **Step 1: Make an outline.** Before starting coding, make an outline (pencil and paper) of what you want to accomplish. You should know where you want to go before you begin coding. 

- **Step 2: Build Up.** Don't try to code everything in one Jupyter cell at once. Build up to your goals by picking pieces of your code to implement. It's a lot easier to deal with 1 error than 10 errors. 

- **Step 3: Analyze the errors.** When an error is thrown, read it. The last part of the error message is the type of error that Python found, the beginning of the message tells you where in your code itself the error happened. 

- **Step 4: Get help.** If you can't figure out from the error message or your own code what's going wrong, don't be afraid to ask the internet! Most of the time with Python the errors are explained online either by other coders or by looking up the help() function or through the Python documentation online.

- **Step 5: Clean and curate.** Make sure your code makes sense, is logical, is professional (I reccomend following the [Python style guide](https://www.python.org/dev/peps/pep-0008/)), and has clearly defined variables etc. 

You can do this! If you start getting overwhelmed take a step back and make sure that you know where you are headed with your code. 
</details>

<details>
  <summary> How do I know what syntax to use?
  </summary>
 
 - Python is extensively documented. You can use the help() function most simply or you can find most if not all of the documentation online as well. There are some general rules which we will be seeing in action in the labs for setting up for loops, functions, etc. 
</details>

# Lab 1 

<details>
  <summary> What does the % character do in the labs? Specically in the %matplotlib inline? 
  </summary>
 
 - This is a 'magic' command which enables the plots to be shows within the Jupyter notebook itself. 
</details>

<details>
  <summary> How do you end a for loop?
  </summary>
 
 - Python syntax runs on indentation. To end a for loop, you simply move back your indentation level. You can see this in Part 4. A. 
</details>

# Lab 2 
<details>
  <summary> What must I set the limits for subplots which share an axis? 
  </summary>
 
 - If you are merging two subplots so that you can no longer see an axis (for example in Lab 2) then it can appear that they are set on the same limits when in fact they are not restrained. You can have one plot go from 1900 - 2000 for example and the other go from 1920 to 2020 but they look the same. This is incredibly misleading and a downfall of the way we see subplots in Lab 2. For this reason you should use the set_xlim() to avoid misleading both yourself and others. 
 
</details>

<details>
  <summary> Should I use a datetime index for everything? 
  </summary>
 
 - Most certainly not! There are some advantages that we see later in the labs, but if you have a datetime index for example that has extreme accuracy to the millisecond, this can be quite annoying as an index! It's up to your discretion if it's more or less useful to have a datetime index. I do reccomend always keeping your original datetime data in your dataframe just in case you corrupt your index upon conversion or other manipulations. 
 
</details>

<details>
  <summary> I'm having trouble understanding the syntax on subplots. How is fig, gridspec, etc different from each other?
  </summary>
 
 - Python is object oriented, that means it's easiest for some people to think of plotting in a similar vein. You are creating multiple instances of different classes of objects that when plotted interact with each other to make the final graphic. Or put more understandably, you create the fig, then the gridspec, then the ax and all of these things in the code interact with each other to make the final graphic. Each of these things (instances of the class of object) have different qualities (attributes/methods) that you can manipulate to make your final graphic. This is why you have so much flexibility in graphics in Python (and possibly frustration).
 
</details>

# Lab 3 

<details>
 <summary> 
  How do vmin, vmax, and set_under() work together?
 </summary>
 
- vmin and vmax set the scale of the colorbar, whereas set_under() sets all the values under the scale to the color that you specify. If vmin is set to the lowest value in the data you are plotting, then set_under() has no effect. 
</details>

<details>
 <summary> 
  What if I have NaN values as well as a value I want to use to set_under?
 </summary>
 
- This isn't shows in Lab 3 but is a very common issue when dealing with plots with both low values and NaN values. The functionality you want is the set_under() AND the set_bad() options. There are several good examples in the official [Matplotlib documentation](https://matplotlib.org/examples/pylab_examples/image_masked.html).
</details>




# Lab 4 
<details>
 <summary> 
  What if I have NaN values and want to take some summary statistics?
 </summary>
 
- Within Python generally NaNs in objects result in unexpected behaivor. There are several ways to get around this in Python. Some functions have a nan version like np.mean() vs np.nanmean(). Pandas has some nice inbuilt behavior to handle this through the isnull() method which generates a Boolean array. A good summary with examples can be found [here](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html).
</details>

<details>
 <summary> 
  What is this .format() syntax for printing things?
 </summary>
 
- Within Python (and other languages!) you can print out values nicely through string formatting. In Python this works as '{}'.format(value) where within the {} it will print the value as a string. You can format the value to be printed using different format codes. I personally like the guide located [here](https://pyformat.info/) on the different ways to format strings.
</details>

<details>
 <summary> 
  I'm having trouble orienting my understanding of the error propagation section in part 6 - how did you know what rule to use?
 </summary>
 
- Within our course textbook, An Introduction to Error Analysis: The Study of Uncertainties in Physical Measurements chapter three covers various cases of the error propagation rules. You can derive them from the general form (equation 3.47). When in doubt you can always use the full form. In fact in this case, it does simplify resulting in the constant error we observe in the final plot in Part 6. 
</details>

<details>
 <summary> 
 What are the stripes in Part 6 the final plot?
 </summary>
 
- Because of the way we plotted the final figure, the NaN values in the array end up stopping the plotting envelope. When starting and stopping repeatedly over the x-axis this has the effect of shading the gap regions darker. Go ahead and try to change the axis limits to see a closer view of what it looks like. 
</details>



# Lab 5 
<details>
 <summary> 
  Why did plotting the anomaly values rather than the t-values (Part 2. C.) change the look of the plot?
 </summary>
 
- We normalized (calculated the t-values) for each month seperately. That means that we calculated the t-values for June only compared the the June distribution, July only to July etc. Each normalization comparison month has a seperate standard deviation. So when you move from anomaly value to the t-values the distribution changes.
</details>

<details>
 <summary> 
  It looks like the plots in Part 2. D. onwards sum up to a probability of greater than 100%? What is going on here?
 </summary>
 
- If you notice in the documentation of [ax.hist()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html) if you set density = True then the area under the curve is set to normalize to one. This can actually be quite confusing because if you have bins of < 1 width, it appears that the y-axis will add up to greater than one. This is something to keep in mind when using the density = True command.
</details>

# Lab 6  

<details>
 <summary> 
 I want to learn more about reading in netCDF files.
 </summary>
 
- Beyond just the lab there are several examples on the web, including the documentation of the netCDF package. I reccomend the netCDF package [documentation and examples](http://unidata.github.io/netcdf4-python/).
</details>

<details>
 <summary> 
 What is this [var for var in dataset.variables] syntax?
 </summary>
 
- This is something in Python called list comprehension. It's best to think of this like a nested for loop that outputs a list. What we did in lab was make a list of the netCDF file variables. The line loops through dataset.variables and populates a list with each one. A similar list comprehension example would be [v for v in np.arange(1, 10)] which would output [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
</details>

# Lab 7  

<details>
 <summary> 
 How can I interpret the ROC curve?
 </summary>
 
- We cover more details in lecture but there is additional description within [Fawcett, 2006](https://www.sciencedirect.com/science/article/pii/S016786550500303X) and usage for classification analysis within space physics check out [Azari et al., 2018](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018JA025391).
</details>

# Lab 8  

<details>
 <summary> 
 Where can I find more information about styles in matplotlib?
 </summary>
 
- I reccomend the matplotlib documentation for more information [here](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html).
</details>

# Visualizations 
<details>
 <summary> 
  I just want a quick way to tell if my figure is understandable by many people?
 </summary>
 
- Go check out the [visualization lectures](https://github.com/astro-abby/data_vis_statistics_geosciences/tree/master/VisualizationBasics). This is a quick tool that you can install to see if your figures are readable for the various types of colors that people see - [Color Oracle](https://colororacle.org/)
</details>

<details>
<summary> 
  Where are some places I can go for inspiration?
 </summary>
 
- Go check out the [From Data to Vis](https://www.data-to-viz.com/) for some high level ideas. If you are in Python I also reccomend seeing the package documentation of [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/). 
</details>

# Useful Resources

<details>
 <summary> 
  Regular expression testing and writing
 </summary>
 
- A useful tester and explanation can be found at https://regex101.com/.
</details>

<details>
 <summary> 
  Matplotlib documentation and examples for basic plotting
 </summary>
 
- For basic plots in Python you can refer to the Matplotlib documentation https://matplotlib.org/.
</details>

<details>
 <summary> 
  NASA CDF files - resources and information
 </summary>
 
* NASA will often use a specific type of file called common data format or CDF to supply and store its data. You can find more about this at the descriptive page at [NASA Goddard](https://cdf.gsfc.nasa.gov/). There are several ways to obtain read and write access to CDF files in Python. What follows is a list to be best of my current knowledge of where to look.
  * Through **SpacePy (pycdf)**, more information at: https://pythonhosted.org/SpacePy/pycdf.html
  * Through **cdflib**, more information at the MAVEN SDC: https://github.com/MAVENSDC/cdflib
  * Through **pysatCDF**, more information is at: https://github.com/rstoneback/pysatCDF

</details>

