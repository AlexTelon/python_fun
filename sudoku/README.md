# Variations of a small part of Norvigs sudoku solver.

The initial part of Norvigs solution creates lists of squares and units that are possible.

I liked the elegance of his solution. But I wanted to explore the solution space in terms of things like:

 * easy vs hard to understand
 * simple vs complex solution

# Solutions and some comments:

 * [`extremly_simple.py`](extremly_simple.py)
   * This is as simple as it gets.
 * [`basic.py`](basic.py)
   * Using only basic python constructs that reads like psudo-code. You can read this without knowing python.
 * [`basic_with_functions.py`](basic_with_functions.py)
   * Same as basic.py but with functions for increased readability. basic is not a fair comparison to python_specific below without functions. Because one would surely use functions in this case right?
 * [`basic_with_functions_yield.py`](basic_with_functions_yield.py)
   * Variation of basic_with_functions that returns generators instead of lists.
 * [`python_specific.py`](python_specific.py)
   * Using list comprehensions to make things more concice. This allows us to create the units in a way where its easier to get an overview of what is combined and why.
 * [`close_to_norvig.py`](close_to_norvig.py)
   * My solution when i approach his solution from `python_specific.py` with the addition of his cross function.
 * [`norvig.py`](norvig.py)
   * This is a small sample of norvigs code from https://norvig.com/sudoku.html. 
   * Remember that the full context of his solution is very important here. The elegance of his choices are made clearer when we consider how then on the next two lines creates `units` and `peers`. Something that I have not done in any of the solutions here.
   * Note that solutions beyond here are moving beyond norvig in non-simplicity. Not that I am claiming they are better.
 * [`beyond_norvig.py`](beyond_norvig.py)
   * This takes the cross idea one step further and allows you to specify which function to apply to each pair.
 * [`beyond_norvig_2.py`](beyond_norvig_2.py)
   * Various alternatives using python itertools.
 * [`beyond_norvig_3.py`](beyond_norvig_3.py)
   * More itertools. Getting squares from unitlist gets us to two usages of rows and cols only, so i inlined them and made the code even more terse.
   * This is now very hard to read
 * [`generic_generator.py`](generic_generator.py)
   * It works, but is not done. An attempt to create a small DSL to create the type of selections in a grid of cols and rols that we want. Much more complex, needlessly so. But more generic and flexible.
   * Again in sudoku this is not necessary.

Finally there is is `compare.py`.

I used `$(python compare.py)` to sanity check my various solutions and changes. Its a quick and dirty way to ensure that the output is the same for all these solutions.


# Thoughs on the results
I am tempted to say that the [`extremly_simple.py`](extremly_simple.py) is the best. You want to write some other code to generate it, but for an application like sudoku these values are constant and hence could be hardcoded. I would want to hide it in a seperate file such that the main code just
imports squares and unitlist though since it is very long and you dont want to unecessarily use that 
much vertical space in your main code. :P 

