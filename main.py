import project

word_tree = project.make_word_tree()
row = int(input("How many rows? "))
col = int(input("How many columns? "))
grid = project.make_squardle(row, col)

near_misses = sorted(list(project.find_near_misses(grid, word_tree)))
near_misses.sort(key=len, reverse=True)
print(near_misses)