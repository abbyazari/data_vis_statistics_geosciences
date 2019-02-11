# Frequently Asked Questions Section
This file contains groupings of commonly asked questions with regards to Python, visualization, and statistics. 

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
  I'm here to learn Python but code in space science / climate science. Where do I begin?
 </summary>
 
 - Lab 1 has a lot of what you need to get started. Begin there then pick and choose what labs you would like after that but make sure to start with Lab 1 as it has a lot of the basics of Python oddities in there. 
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
   </details>
   
    <details>
     <summary> 
      More advanced courses:
     </summary>

    - EECS 545 Machine Learning 
    - EECS 598 Computational Data Science
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
 
- NCAR has moved toward Python for future development. Go check out their roadmap and report [here](http://www.ncl.ucar.edu/Document/Pivot_to_Python/NCL_Pivot_to_Python_Report_and_Roadmap.pdf). I reccomend seeing the NCAR supported transition documentations providing NCL to Python comparisons at the following links:

- [Transition Guide](http://www.ncl.ucar.edu/Document/Manuals/NCL_to_Python/Transition_Guide_NCL_PyNGL.pdf)
- [Quick Look Applications](http://www.ncl.ucar.edu/Applications/NCL_to_Python/)
</details>

# Lab 1 Questions
<details>
  <summary> I'm feeling overwhelmed writing my own code. How do I start this? 
  </summary>
 
  - Coding is not a profession that runs on natural talent. Most of coding is an iterative process where you try, receive an error, and try again. Errors are a natural part of programming. You should expect to have your notebooks throw errors at you and to then figure out how to fix them. As you code you will need to use resources such as the help() function, resources you find in books and online including these notebooks here! I wanted to share with you an outline to get started writing your own code that I've found particularly useful: 

- **Step 1: Make an outline.** Before starting coding, make an outline (pencil and paper) of what you want to accomplish. You should know where you want to go before you begin coding. 

- **Step 2: Build Up.** Don't try to code everything in one Jupyter cell at once. Build up to your goals by picking pieces of your code to implement. It's a lot easier to deal with 1 error than 10 errors. 

- **Step 3: Analyze the errors.** When an error is thrown, read it. The last part of the error message is the type of error that Python found, the beginning of the message tells you where in your code itself the error happened. 

- **Step 4: Get help.** If you can't figure out from the error message or your own code what's going wrong, don't be afraid to ask the internet! Most of the time with Python the errors are explained online either by other coders or by looking up the help() function or through the Python documentation online.

- **Step 5: Clean and curate.** Make sure your code makes sense, is logical, is professional (I reccomend following the [Python style guide](https://www.python.org/dev/peps/pep-0008/)), and has clearly defined variables etc. 

You can do this! If you start getting overwhelmed take a step back and make sure that you know where you are headed with your code. 
</details>

<details>
  <summary> What does the % character do in the labs? Specically in the %matplotlib inline? 
  </summary>
 
 - This is a 'magic' command which enables the plots to be shows within the Jupyter notebook itself. 
</details>

# Lab 2 Questions
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


# Lab 3 Questions

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

<details>
 <summary> 
  What if I have NaN values and want to take some summary statistics?
 </summary>
 
- Within Python generally NaNs in objects result in unexpected behaivor. There are several ways to get around this in Python. Some functions have a nan version like np.mean() vs np.nanmean(). Pandas has some nice inbuilt behavior to handle this through the isnull() method which generates a Boolean array. A good summary with examples can be found [here](https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html).
</details>

# Lab 4 Questions

# Visualizations 
<details>
 <summary> 
  I just want a quick way to tell if my figure is understandable by many people?
 </summary>
 
- Go check out the [visualization lectures](https://github.com/astro-abby/data_vis_statistics_geosciences/tree/master/VisualizationBasics). This is a quick tool that you can install to see if your figures are readable for the various types of colors that people see - [Color Oracle](https://colororacle.org/)
</details>



