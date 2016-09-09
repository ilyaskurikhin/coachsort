coachsort
=========

This Python library aims to make managing groups of students at EPFL easier.
It also contains some demographic analysis tools.

With this tool, you can import xlsx files created by ISAcademia and based on
the data from <people.epfl.ch> into specialized python classes. This allows you
to handle the data in many different ways, from analysis to managment of 
smaller groups.

For further information, contact <mailto:ilya.skurikhin@epfl.ch>

## Requirements ##

All the python code in this library is in Python 3. All the package requirements
are therefore also in Python 3. If packages show as unavailable, try installing 
using `pip3 install {package}` or `python3 -m pip install {package}`.

This library uses a two popular excel read/write rools, `xlrd` and `xlwt`. I 
recomment that you install these via `pip install {package}`. 

In order to use the library, you can use the Jupyter Notebook(formerly iPython 
Notebook) environment. To install Jupyter, you can follow the instructions on
their website at <http://jupyter.org>.

## Get started ##

To get the EPFL people files, log into <http://isa.epfl.ch> and select 
'Reporting' in the top-right-hand menu. This will lead you to a page where you 
can select the lists that you would like to download. Choose the xls format and 
download the desired lists.

Convert the lists from xls to the XML based xlsx format by opening them with 
either a spreadsheet viewer (Google Docs if you have none installed). 

You could also implement importing xls files :P

Use the `import_check_headers()` function to import the files while selecting
which data to take. After you save them from the library, you can open them 
directly by using `import_safe_file(filename)`. 

## Build in tools ##

### Merge and update ###


The merge function allows you to merge your previous database with a newer one
from ISAcademia. It will add new students and update their info.

You can check what has been changed by calling `find_new_students()` and 
`find_updated_students()`. This was you can email all the students that have 
just joined a class, for example.

### Assign students to groups ###

The distribution functions will distribute students into a specified number of 
equally sized groups. You can choose to have the groups respect the sex ratio
of the larger group. You could also implement the same thing for nationality.


