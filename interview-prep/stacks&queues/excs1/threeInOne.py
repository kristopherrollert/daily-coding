# Three in One: Describe how you could use a single array to implement three
# stacks

# Each stack i = (0, 1, 2) would push/pop onto 3m + i where m represents the
# number of elements in each stack.

# As a possible design feature, once stacks have used their 1/3 allotment,
# they could possibly start loop backwards on a previous stacks track. The
# downside is that there will always need to be a buffer between stacks

# I guess the solution is to shift stacks arround when they get too large
