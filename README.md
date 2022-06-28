ProgSoc-Competition
=====

## Table of Contents

- [1. Hello World](https://github.com/AchillesReaper/ProgSoc-Competition#1.-Hello-World)
- [2. Console Frame](https://github.com/AchillesReaper/ProgSoc-Competition#2.-Console-Frame)
- [3. Startup Job](https://github.com/AchillesReaper/ProgSoc-Competition#3.-Startup-Job)
- [4. Expert Spy](https://github.com/AchillesReaper/ProgSoc-Competition#4.-Exper-Spy)
- [5. Seismic Peaks](https://github.com/AchillesReaper/ProgSoc-Competition#5.-Seismic-Peaks)
- [6. ASCII Cross Box](https://github.com/AchillesReaper/ProgSoc-Competition#6.-ASCII-Cross-Box)
- [7. Message Compression](https://github.com/AchillesReaper/ProgSoc-Competition#7.-Message-Compression)
- [8. Rouge Lock-on](https://github.com/AchillesReaper/ProgSoc-Competition#8.-Rogue-Lock-On)
- [9. Matching Brackets](https://github.com/AchillesReaper/ProgSoc-Competition#9.-Matching-Brackets
)
- [10. Train Game](https://github.com/AchillesReaper/ProgSoc-Competition#10.-Train-Game)
- [11. Persona Timetable](https://github.com/AchillesReaper/ProgSoc-Competition#11.-Persona-Timetable)
- [12. Ray Casting](https://github.com/AchillesReaper/ProgSoc-Competition#12.-Ray-Casting)


### 1. Hello World

Welcome to the programming competition! We assume that this is the first programming competition for many contestants here, so we’re starting off with a basic Hello World question.

You need to read a number from standard input (stdin) and print hello world that number of times.

Input
<br>A single number (1 <= N < 1000), representing the number of times hello world should be printed.

Output
<br>Print Hello World N times.

Sample “1”
<pre>
1
Hello World
</pre>

Sample “4”
<pre>4
Hello World
Hello World
Hello World
Hello World
</pre>


### 2. Console Frame
You’re working on a console user interface with some pretty visualizations of data. Part of the interface involves printing out words in a frame, so that they’re more easily visible.

So for example, if you want to display Hello World in a frame, it will print it as:
<pre>
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
</pre>



Input
<br>You’re given a string of words, separated by spaces.

Output
<br>Print the words in a frame, with one word on each line.

Sample “Frame”
<pre>
Text in a box
********
* Text *
* in   *
* a    *
* box  *
********
</pre>

Sample “Hello”
<pre>
Hello World in a frame
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
</pre>

Sample “Test”
<pre>
Test
********
* Test *
********
</pre>


### 3. Startup Job
You’ve been hired by an accounting startup after the previous developer quit, and they want you to clean up their records. After briefly looking over their database, you realized how many duplicate records they have of transactions. Each transaction has an ID, and their database wasn’t configured to prevent duplicates.

Each ID is an 8 digit hex code, and before configuring the database to prevent future duplicates, you need to remove all duplicate records.

Input
<br>There is a single line of IDs separated by spaces, in random order with duplicates.

Output
<br>Print the unique IDs, separated by spaces, in the order they first appeared, without duplicates.

Sample “Example”
<pre>
901ec343 d2111f4a a391c135 c66d1385 c66d1385 c66d1385 c66d1385 c9cb4635 c66d1385 5acc6017 ceb83be1 d2111f4a ceb83be1 d2111f4a a30db74f ceb83be1 4aa0b3fe c66d1385 901ec343 d2111f4a

901ec343 d2111f4a a391c135 c66d1385 c9cb4635 5acc6017 ceb83be1 a30db74f 4aa0b3fe
</pre>

Sample “Small”
<pre>
c66d1385 901ec343 d2111f4a c66d1385 d2111f4a

c66d1385 901ec343 d2111f4a
</pre>


### 4. Expert Spy
A spy of the name James Bond has found the jackpot. Steam is the most popular online Video Game distributor, and Bond has just found his way into the Valve Headquarters and has located the CEO’s secret stash of Steam gift card codes. He needs your help to decrypt them so MI6 can buy a bunch of games during the next Steam Sale.

Each code is encrypted as a sequence of numbers and you need to create an advanced algorithm to decrypt them. Each number in the sequence is two digits long and matches an associated letter of the alphabet, alternating between lowercase and uppercase. For example, the code 0001 decrypts to “ab”, and 232425262728 decrypts to “xyzABC”.

Input
<br>A single line of digit pairs

Output
<br>The decrypted code

Sample “1”
<pre>
000102030405060708
abcdefghi
</pre>

Sample “2”
<pre>
232425262728
xyzABC
</pre>

Sample “3”
<pre>
9075143201754932
MxoGbxXG
</pre>

Sample “wrap”
<pre>
505152535455
YZabcd
</pre>


### 5. Seismic Peaks
You’re analyzing seismic activity values, and you have many graphs with two activity peaks each from different sensors. You need to find out the time between the two peaks in order to triangulate the underground source of the activity.

A peak is a value where both neighbouring values are smaller, so for example in 1 1 2 3 1 1, the 4th value is the peak.

Input
You will receive a list of numbers (at least 5 numbers), the numbers will always contain 2 peaks, and the peaks are never the first or last element of the list.

Output
Print the number of elements between the peaks. For example for `1 2 3 2 3 2 1`, the output should be `1`.

Sample “Example1”
<pre>
1 1 2 4 2 1 3 5 4 3 2 1 1
3
</pre>

Sample “Example2”
<pre>
1 2 3 2 3 2 1
1
</pre>


### 6. ASCII Cross Box
You are in a programming interview, and you are asked to print a cross box using ASCII, given the size of the box.

Input
A single number (1 <= N < 100) representing the size of the box.

Output
An ascii cross box made with hashtags (`#`) of size N. See the samples for example outputs.

Sample “1”
<pre>
1
#
</pre>

Sample “10”
<pre>
10
##########
##      ##
# #    # #
#  #  #  #
#   ##   #
#   ##   #
#  #  #  #
# #    # #
##      ##
##########
</pre>

Sample “5”
<pre>
5
#####
## ##
# # #
## ##
#####
</pre>


### 7. Message Compression
Forrest lives a country where mobile plans have very strict and expensive SMS limits. He wants to save characters while texting people, and he noticed that when he sends text messages, they have many repeating characters, and has devised a simple compression algorithm based on repeating information.

The compression scheme is rather simple. When encoding a text string, repeated consecutive characters are replaced by a single instance of that character and the number of occurrences of that character (the character’s run length), unless there’s only 1 instance in which case the 1 is skipped. Decoding the encoded string results in the original string by repeating each character the number of times encoded by the run length. Forrest calls this encoding scheme run-length encoding. (We don’t think he was actually the first person to invent it, but we haven’t mentioned that to him.)

For example, the string `HHHellloo` is encoded as `H3el3o2`. Decoding `H3el3o2` results in the original string. Encoding something like `compression` results in `compres2ion`. Forrest has hired you to write an implementation for his run-length encoding algorithm.

Input
<br>Input consists of a single line of text. The line starts with a single letter: `E` for encode or `D` for decode. This letter is followed by a single space and then a message. The message consists of `1` to `100` characters.

Each string to `encode` contains only upper- and lowercase English letters, underscores, periods, and exclamation points. There are no numbers in the input. No consecutive sequence of characters exceeds 9 repetitions.

Each string to `decode` has even length. Its characters alternate between the same characters as strings to encode and a single digit between `1` and `9`, indicating the run length for the preceding character.

Output
<br>On an input of `E` output the run-length encoding of the provided message. On an input of `D` output the original string corresponding to the given run-length encoding.

Sample “Compress”
<pre>
E HHHeellloWooorrrrlld!!
H3e2l3oWo3r4l2d!2
</pre>

Sample “Decompress”
<pre>
D H3e2l3oWo3r4l2d!2
HHHeellloWooorrrrlld!!
</pre>


### 8. Rogue-Lock-On
Hrrrrnngh, this is Solid Snake. I’m being attacked by an insane man in an Attack Helicopter and my homing missiles aren’t working. There’s too much interference and they can’t lock onto him, so I can’t get a good shot. I need you to come up with an algorithm to fix this damn thing, and fast!

There should be several sequences of numbers. Each number in each sequence should represent the heat signature that the tracker sees. 0 means completely cold, and 9 means hot. To guarantee locking on, the tracker should be able to see the same heat value at least once in each sequence. If the tracker can’t see a pattern in each sequence, then it’s not locked on and you should return “No lock on”. If there are multiple matches, then the hottest match should be the target. If you do find a match in all sequences, return the number and the position in the sequence!

Then I can finally get a good shot on that Helicopter!

Input
A single digit representing the number of sequences (N>1).

Then, the sequences of numbers, with a potential match betwen them. For example:

18700
88330
68710
68876
18153
98507

Where the index is 1 and the number is 8.

There will never be multiple matches with the same digit on different indexes.

Output
Output 2 numbers, first one is the index, second one is the number. If there are multiple matches, return the one with the highest number.

Sample “Match”
<pre>
6
18700
88330
68710
68876
18153
98507
1 8
</pre>

Sample “Multiple Matches”
<pre>
4
0059503
0369653
0899983
0129853
3 9
</pre>

Sample “No Match”
<pre>
5
6709609
7509240
9054612
6485153
5230189
No lock on
</pre>


### 9. Matching Brackets
You are making a syntax parser for your own programming language, and the language uses various brackets for different scopes and expressions (similar to other C-style languages). Before parsing any fancy syntax, you want to make sure that the number of brackets matches, as most of the syntax around it would depend on it.

You take input text for language and remove all characters other than the brackets. Then you write a script that makes sure that all the brackets match.

Input
<br>You are given a string of nested brackets of different types, specifically `{}`, `()` and `[]`

Output
<br>Print `yes` if the brackets match, `no` otherwise.

Sample “Backwards”
<pre>
}}{{
no
</pre>

Sample “Longer Fail”
<pre>
[({})(){[(){}]]
no
</pre>

Sample “Longer Success”
<pre>
[({})()[(){}]]
yes
</pre>

Sample “Simple Fail”
<pre>
{(}
no
</pre>

Sample “Simple Success”
<pre>
{}
yes
</pre>


### 10. Train Game


### 11. Persona Timetable
You have been given a list of Friends with their timetables of availability in High School in a specific order of priority. You’ve made it your mission to hang out with each friend exactly once throughout the week as early as possible.

Each timetable (including your own) ranges from Monday to Friday, with time slots for the Morning and Afternoon for each day. Your script should output the optimal schedule for your friends, which in your case, is the earliest available slot in the week for each friend. If there is a conflict which causes a friend to not have an available slot, then try to move conflicting friends in order to the next available slot until you have an available slot.

Input
<br>You will receive a single digit representing the number of friends with timetables (N>1). You will then receive each friend’s timetable with their name and time slots available seperated by commas. For example:
<pre>
2
Name 1,Monday Morning,Tuesday Afternoon,Friday Morning
Name 2,Monday Afternoon,Wednesday Afternoon,Thursday Morning
</pre>


There will be no inputs where creating a timetable will be impossible.

Output
<br>Output the final timetable with each friend assigned to a time slot. If there is no friend assigned to a time slot, write “None”.

For example:
<pre>
Monday Morning: Ryuji
Monday Afternoon: Ann
Tuesday Morning: None
Tuesday Afternoon: Yusuke
Wednesday Morning: Makoto
Wednesday Afternoon: None
Thursday Morning: Futaba
Thursday Afternoon: None
Friday Morning: Haru
Friday Afternoon: Akechi
</pre>


Sample “1 - Simple”
<pre>
4
Ryuji,Monday Morning,Tuesday Morning,Wednesday Morning
Ann,Monday Afternoon,Tuesday Afternoon,Wednesday Afternoon
Yusuke,Thursday Morning,Friday Morning
Makoto,Monday Morning,Tuesday Morning
Monday Morning: Ryuji
Monday Afternoon: Ann
Tuesday Morning: Makoto
Tuesday Afternoon: None
Wednesday Morning: None
Wednesday Afternoon: None
Thursday Morning: Yusuke
Thursday Afternoon: None
Friday Morning: None
Friday Afternoon: None
</pre>

Sample “2 - Conflict”
<pre>
4
Ryuji,Monday Morning,Tuesday Morning
Ann,Tuesday Afternoon
Yusuke,Monday Morning,Tuesday Afternoon
Makoto,Tuesday Morning,Wednesday Afternoon
Monday Morning: Yusuke
Monday Afternoon: None
Tuesday Morning: Ryuji
Tuesday Afternoon: Ann
Wednesday Morning: None
Wednesday Afternoon: Makoto
Thursday Morning: None
Thursday Afternoon: None
Friday Morning: None
Friday Afternoon: None
</pre>

Sample “3 - Complex”
<pre>
7
Ryuji,Monday Afternoon,Wednesday Afternoon,Friday Afternoon
Ann,Tuesday Morning,Thursday Morning
Yusuke,Monday Morning,Tuesday Morning
Makoto,Tuesday Morning,Thursday Morning,Friday Morning
Futaba,Monday Morning,Monday Afternoon,Tuesday Morning,Tuesday Afternoon,Wednesday Morning,Wednesday Afternoon,Thursday Morning,Thursday Afternoon,Friday Morning,Friday Afternoon
Haru,Thursday Morning,Friday Afternoon
Akechi,Wednesday Afternoon,Friday Afternoon
Monday Morning: Yusuke
Monday Afternoon: Ryuji
Tuesday Morning: Ann
Tuesday Afternoon: Futaba
Wednesday Morning: None
Wednesday Afternoon: Akechi
Thursday Morning: Makoto
Thursday Afternoon: None
Friday Morning: None
Friday Afternoon: Haru
</pre>


### 12. Ray Casting 
