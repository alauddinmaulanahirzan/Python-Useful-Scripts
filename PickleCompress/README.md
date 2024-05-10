# Compress Pickle Class

This file contains **Variable Dumping** with **Compression** feature.

## Avaiable Methods
* compress_pickle(filename, object, compression_mode) : Dump and Compress on-the-fly Variable using avaiable compression algorithm
* decompress_pickle(filename) : Load dumped variables from a file

## Avaiable Algorithm
* **gz** as **gzip** in script
* **bz2** as **bzip2** in script
* **lzma** as **lzma** in script
* DEFAULT **none** to dump as normal pickle
