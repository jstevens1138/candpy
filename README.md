# candpy
Simple examples for C/Python interoperability 

Thanks to the hard work of many and its ever-expanding ecosystem, Python has available to it a number of mechanisms with 
which interfaces with or even compilation to C code are not only possible, but easy. The needs of such interfaces generally 
involve a requirement to integrate with a library written in C, or a need for increased performance. When the need is the 
former, the solution often involves simply loading an SO and executing the necessary functions. When the need is the latter, 
the work involved can become much more complex, requiring a degree of fine-tuning.

With the diverse array of needs for interfaces, the various options available to us are generally built around specific needs 
and use cases. With this in mind, there isn’t a catch-all library or utility available that one can always be sure to rely on 
for all possible uses. At the same time, there exist several mature solutions that deal in different approaches and uses, and 
one can be certain that at least one of these will be the right tool for the job-- it’s simply important to understand how 
each of these solutions work and how they fit into the current business need. Three of the best solutions are ctypes, cffi, 
and Cython.

ctypes is an older solution that is part of the Python standard library. It’s ubiquitous and well-understood, and is 
commonly used for calling existing shared object library functions. Though it is easy to work with, it is not magic-- 
memory leaks are easy to introduce, and intermediary wrapping functions must be employed to, for example, deal in floats. 
Performance can be much slower than other options. ctypes is perhaps best to use if the specific need involves lightweight 
usage (where the ability to quickly adapt stackoverflow snippets is preferable, for instance) or the need is to maintain 
some sort of legacy project where ctypes is already employed.

cffi is a modern option that in many way feels like a natural successor to ctypes. One can even employ ctypes-esque ABI 
functionality to essentially work with shared objects in a surprisingly similar fashion to the aforementioned library. 
However, the real power in cffi comes from its API mode, which grants speed, flexibility, and performance. Additionally, 
cffi is far less tedious than ctypes as a result of its ability to consume actual C (no more painful conversion functions 
for simple actions). The hurdle one faces when employing the API mode is the need for an additional compilation step-- 
but this is a small price to pay. For when vanilla Python is a must and development is greenfield, cffi might be the best
possible Python/C interface.

Cython is a superset of the Python specification that supports (almost) all Python syntax while also allowing for static 
typing and other spiffy features. Built primarily for developing performant Python modules, Cython can also be used to build
compiled executables. Its secret is that it compiles Cython files (pyx) to C, then either to object or executable code. 
This allows for a huge degree of low-level optimization, including even bypassing the GIL in certain cases. Furthermore,
the feature-set and tooling around development are both rich. One incredibly useful feature is the code annotation, which 
allows for generation of an HTML file which displays points at which fast C code and slow Python code will run as the result
of a given .pyx file. The challenges associated with using Cython are largely organizational: teaching developers how to 
use this new language and integrating the new build steps, such as compilation, into the development workflow. Once these 
are overcome, Cython can be used with great efficacy for a wide variety of tasks.

To conclude, the options for Python/C interoperability that exist for the developer are both sufficiently mature and 
feature-rich; the specific option that is most viable depends on the needs of the project at hand. No matter the chosen 
option, there is support and documentation to make the project enjoyable and fruitful.

 

Works Cited
https://www.infoworld.com/article/3250299/python/what-is-cython-python-at-the-speed-of-c.html

https://docs.python.org/3/library/ctypes.html

https://cython.org/#documentation

https://cffi.readthedocs.io/en/latest/

https://www.paypal-engineering.com/2016/09/22/python-by-the-c-side/

https://docs.scipy.org/doc/numpy-1.15.0/user/c-info.html

http://masnun.rocks/2016/10/01/creating-an-executable-file-using-cython/
