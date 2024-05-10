import bz2
import lzma
import gzip
import pickle


class CompressPickle:
    def compress_pickle(self, filename: str, object, compression_mode: str = "none"):
        self.object = object
        if "." in filename:
            filename = filename.split(".")[0]
        if compression_mode == "gzip":
            filename = f"{filename}.gz"
            with gzip.open(filename=filename, mode="wb") as gzfile:
                pickle.dump(obj=self.object, file=gzfile)
        elif compression_mode == "bzip2":
            filename = f"{filename}.bz2"
            with bz2.open(filename=filename, mode="wb") as bz2file:
                pickle.dump(obj=self.object, file=bz2file)
        elif compression_mode == "lzma":
            filename = f"{filename}.xz"
            with lzma.open(filename=filename, mode="wb") as lzfile:
                pickle.dump(obj=self.object, file=lzfile)
        elif compression_mode == "none":
            filename = f"{filename}.pickle"
            with open(filename, mode="wb") as picklefile:
                pickle.dump(obj=self.object, file=picklefile)
        else:
            print("Incorrect Format")
            

    def decompress_pickle(self,filename: str):
        if "gz" in filename:
            with gzip.open(filename=filename, mode="rb") as gzfile:
                self.object = pickle.load(file=gzfile)
            return self.object
        elif "bz2" in filename:
            with bz2.open(filename=filename, mode="rb") as bz2file:
                self.object = pickle.load(file=bz2file)
            return self.object
        elif "xz" in filename:
            with lzma.open(filename=filename, mode="rb") as lzfile:
                self.object = pickle.load(file=lzfile)
                return self.object
        elif "pickle" in filename:
            with open(filename, mode="rb") as picklefile:
                self.object = pickle.load(file=picklefile)
            return self.object
        else:
            print("Incorrect Format")


# Main Code Here
def main():
    a: str = "Test"

    compressor = CompressPickle()
    # Compress to each mode 'gzip', 'bzip2', and 'lzma'
    compressor.compress_pickle(filename="a", object=a, compression_mode="gzip")
    compressor.compress_pickle(filename="a", object=a, compression_mode="bzip2")
    compressor.compress_pickle(filename="a", object=a, compression_mode="lzma")
    compressor.compress_pickle(filename="a", object=a)

    # Decompress
    b = compressor.decompress_pickle(filename="a.gz")
    c = compressor.decompress_pickle(filename="a.bz2")
    d = compressor.decompress_pickle(filename="a.xz")
    e = compressor.decompress_pickle(filename="a.pickle")

    print(a, b, c, d, e)

if __name__ == "__main__":
    main()
