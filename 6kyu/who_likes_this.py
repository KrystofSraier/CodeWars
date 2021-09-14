You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.




def likes(names):
    c = ""
    b = len(names) - 2
    if len(names) > 0:
        if len(names) == 1:
            c =  "{} likes this".format(names[0])
        elif len(names) == 2:
            c =  "{} and {} like this".format(names[0], names[1])
        elif len(names) == 3:
            c = "{}, {} and {} like this".format(names[0], names[1], names[2])
        elif len(names) > 3:
            c = "{}, {} and {} others like this".format(names[0], names[1], b)
    else:
        c = "no one likes this"
    return c