import project

word_tree = project.make_word_tree()
row = int(input("How many rows? "))
col = int(input("How many columns? "))
grid = project.make_squardle(row, col)

print(sorted(list(project.find_words(grid, word_tree))))