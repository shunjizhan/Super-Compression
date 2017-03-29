# Introduction
This is a Python program that implement a new algorithm to compress certain English texts. The estimated compression ratio is 4:1, which is even higher than Hoffman Encoding! Right now it can only be applied to a fixed format of English texts, but it has high potential to apply to more generic texts, with future improvement on the algorithm.

# Run
    cd Super-Compression/
    python compress.py

# Sample Output
![](https://raw.githubusercontent.com/shunjizhan/Super-Compression/master/compression%20demo.png?raw=true)

# Specification
The whole program will go through the following process:    
--- run() ---> random_generated_file <br> 
--- modify() ---> modified_file <br> 
--- compress() ---> super_compressed_file <br>
--- decompress() ---> decoded_file <br>

A report containing more details can be found [here](https://github.com/shunjizhan/Super-Compression/blob/master/New%20Compression%20Algorithm.pdf)

# Author
Shunji Zhan & Yueyang Li