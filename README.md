# Introduction to text analytics 2021

All meetings will take place online via Skype: [https://join.skype.com/ICLVQrErNSWj](https://join.skype.com/ICLVQrErNSWj)

## Schedule

- Saturday, November 20-th 2021, 10:00-13:00
- Saturday, November 20-th 2021, 14:00-16:00
- Sunday, November 21-th 2021, 10:00-13:00
- Sunday, November 21-th 2021, 14:00-16:00

## Details

TBA

## Environment setup

The workshop will be using `Python` as a computing environment. In order to be able to follow you will need
a working python installation and a text editor/IDE capable of running [jupyter notebooks](https://jupyter.org/).

- You need a working Python 3.7 installation. Newer version will probably also run fine, but it is recommended to follow the 
  instructions below.
- You can use your editor or IDE of choice. During the online meetings I'll be using [DataSpell](https://www.jetbrains.com/dataspell/)
  and [PyCharm](https://www.jetbrains.com/pycharm/). DataSpell is still in early preview but is usable and free to use.
  PyCharm is a commercial product with a free evaluation option and free student subscription. Note: the author is not affiliated with
  Jetbrains.

### Setup with Anaconda 3

1. Download and install [Anaconda 3](https://www.anaconda.com/products/individual) using
   the default installation options
2. Download and install [git](https://git-scm.com/download/win) for Windows. Leave the options to their defaults
3. To clone the workshop repository open the windows menu and type `cmd`. Open the command line window and paste the following
   command:
    ```
    git clone https://github.com/boyko/text-analytics-workshop-2021
    ```

   This will download the workshop files in a directory called `text-analytics-workshop-2021` located in your user
   directory.
4. Open Anaconda Navigator (Click on the Windows start button and start typing "anaconda"), find the environments section and click on the "Import" button (lower left part of the interface)
5. In the import environment dialog open the file browser (find the button next to specification file) and find the `environment.yml` file that is located in the
   workshop directory. Click "OK" and wait for the installation to complete (this can take a while depending on your machine and connection speed).
6. Find the `tawn` environment and click on its "play" button and then choose "Terminal". In the terminal,
   type

    ```
    pip install tensorflow==2.2.0
    ```

   to install tensorflow (this can also take some time).
7. Make sure that the `tawn` environment is activated and launch Jupyter Notebook. Open the test notebook
    called `01-Load-Packages.ipynb` and run the code block. If all required packages can be loaded successfully
    you should see the versions of the packages printed in the output area.


### Setup with DataSpell for Windows

1. Follow the anaconda setup steps outlined above to create the `tanw`
2. Download and install DataSpell EAP: [https://www.jetbrains.com/dataspell/](https://www.jetbrains.com/dataspell/)
3. Open DataSpell (requires Jetbrains login) and open the workshop directory.
   Find the `File` menu in DataSpell, click on it and select `Settings`. In the new window find the menu `Project` and
   then `Python interpreter`.
4. In the new dialog choose the `Conda environment` on the left. Click on the cog-wheel icon and choose "Add". Find the `tawn` environment created earlier and
    under the existing environments and select it. Click on "OK" and wait for the DataSpell indices to update.

[//]: # (5. When the environment creation is finished, click on the `Terminal` button at the bottom of the interface. )

[//]: # (   This will open a new command line interface. Copy and run the following command there to install )

[//]: # (   the python packages in the conda environment.)

[//]: # ()
[//]: # (    ```)

[//]: # (    conda install scikit-learn=1.0.* numpy=1.21.* seaborn=0.11.* scipy=1.7.* jupyter=1.0.* nltk=3.6.* matplotlib=3.4.* pandas=1.3.*)

[//]: # (    ```)

[//]: # ()

