# coachsort
This Python library aims to make managing groups of students at EPFL easier.

With this tool, you can import xlsx files created by ISAcademia and based on
the data from people.epfl.ch into specialized python classes. This allows you
to handle the data in many different ways, from analysis to managment of 
smaller groups.

For further information, contact ilya.skurikhin@epfl.ch

Build in tools
==============

Merge and update
----------------

The merge function allows you to merge your previous database with a newer one
from ISAcademia. It will add new students and update their info.

You can check what has been changed by calling `find_new_students()` and 
`find_updated_students()`. This was you can email all the students that have 
just joined a class, for example.

Distribute
----------

The distribution functions will distribute students into a specified number of 
equally sized groups. You can choose to have the groups respect the sex ratio
of the larger group. You could also implement the same thing for nationality.


