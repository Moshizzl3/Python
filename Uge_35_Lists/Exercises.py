# Exercise 1

# #['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
# #['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
# ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are'] 'Hello World Huston we are here' -> 'World Huston we'

# #['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
strList1 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
result1 = strList1[1:5]
print(result1)
# #['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
result2 = strList1[0:2]
print(result2)
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
result3 = strList1[4:]
print(result3)

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
result4 = strList1[4:5]
print(result4)

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
result5 = strList1[::2]
print(result5)

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
result6 = strList1[::-1]
print(result6)

# ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are'] 'Hello World Huston we are here' -> 'World Huston we'
result7 = strList1[:],  " ".join(strList1), " ".join(strList1[1:4])
print(result7)


# ____________________

# Exercise 1.1
# The following data should be presented as either a list or a tuple.
# Your job is to choose the right one.
# Hint: A list is a collection of the same type of data, a tuple is a record (e.g. in a database a record is called a row):
# 1. Claus, 51, male, clbo@kea.dk, 31011970-1313 (Tuple, data should be mutable)
# 2. Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo (List, data should be mutable)
# 3. Claus, Henning, Torben, Carl, Tine (List, data should be mutable)
# 4. ‘Hello’, ‘World’, ‘Huston’, ‘we’, ‘are’, ‘here’ (List, data should be mutable, no idea what this is though??)
# 5. Rolling Stones, Goats Head Soup, 31 August 1973, 46:56 (Tuple, data should be immutable as this is a historic record)
# 6. 40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan; (Tuple, look like geo locations, but can the names not change)

# ____________________

# Exercise 2

# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
input = input("Give me a word, and i will give u a broken word back..: ")


def strippedWord(input):

    temp = ""
    for char in input:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            continue
        temp += char

    return temp


print(strippedWord(input))

# ____________________

# Exercise 3

# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])


# Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Ib', 'Per', 'Ali', 'Zaa']

# Sort this list by using the sorted() build in function.
l_sorted = sorted(l)
print(l_sorted)

# Sort the list in reversed order.
l_sorted = sorted(l, reverse=True)
print(l_sorted)

# Sort the list on the lenght of the name.
l_sorted = sorted(l, key=len)
print(l_sorted)

# Sort the list based on the last letter in the name.


l_sorted = sorted(l, key=lambda x: x[-1])
print(l_sorted)


# Sort the list with the names where the letter ‘a’ is in the name first.


l_sorted = sorted(l, key=lambda x: 'a' in x.lower(), reverse=True)
print(l_sorted)

# ____________________

# Excercise 4.1
s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

print(len(s))
print(len(s.replace(" ", "")))
print(len(s.split()))
# ______

# Exercise 4.2
lyric = open('lyrics.txt', 'w')
song = open('songs.docx', 'w')

song.write("hi, this is line one. \n")
song.write("hi, this is line two \n")
song.write("hi, this is line three \n")
song.close()

songOpen = open('songs.docx', 'r')
print(songOpen.read())
songOpen.close()

songOpen = open('songs.docx', 'r')
print(songOpen.readline())
songOpen.close()

songOpen = open('songs.docx', 'r')
print(songOpen.readlines())
songOpen.close()
# ____________________

# Exercise 5

list2 = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2),
         (1, 5), (10, 4), (10, 1), (3, 1)]

l_sorted_2 = sorted_by_second = sorted(
    list2, key=lambda tup: (tup[1], tup[0]))

print(l_sorted_2)
# ____________________

for index, i in enumerate(l):
    print(index)
