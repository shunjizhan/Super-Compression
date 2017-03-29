To Run:
"python compress.py" <br>

--> random_generated_file --> modify() <br>
--> modified_file --> compress() <br>
--> super_compressed_file --> decompress() <br> 
--> decoded_file <br>

# Introduction
This is a Python program that implement a new algorithm to compress certain English texts. The estimated compression ratio is 4:1, which is even higher than Hoffman Encoding. Right now it can only be applied to a fixed format of English texts, but it has high potential to apply to more generic texts with further improvement on the algorithm.

# Run
    cd GoBang/
    ant run

or

    cd GoBang/
    ant compile
    ./Gobang

# Options
`-l`if this is specified, computer will be the dark player.     
`-n [size]`size of the board, can be 5-26, default is 11.     
`-d [depth]` depth of the Minimax tree, default is 2.     

# Sample 
![](https://raw.githubusercontent.com/shunjizhan/GoBang/master/Gobang_demo.gif?raw=true)

# Referee
To make this program compete with itself or with other program: 

    python referee.py [board_size] ./Gobang ./Gobang

or

    python referee.py [board_size] ./other_program ./Gobang

# Resources
referee.py is provided by TA.

# Specification
A report containing more details can be found [here](https://github.com/shunjizhan/GoBang/blob/master/cs165A_mp2_report.pdf)

# Author
Shunji Zhan & Yueyang Li