# PytorchFramework

This is a pytorch framework for my research.

## Import

you can make whole file as a package and put data file outside. You should call from outside.

Here I just don't treat this whole folder as package. I treat each subfolder as module. So I put data here.

The disadvange is some py files(like process_data.py, util.py) should be in the module (but I put them here with the main file and data folder)

If you want to release the whole project as a package. You should ignore the data folder and pay attention to the data path

Ths advantage is the path of data is relevant.
