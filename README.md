## Random walk
It draws continuous random walks using [matplotlib](https://matplotlib.org/). It uses Python's standard library [random](https://docs.python.org/2.7/library/random.html) to generate random numbers

### To Setup
Install [matplotlib](https://matplotlib.org/) library using ```pip```  tool
```bash
pip install matplotlib
python -m matplotlib.install
```
Alternatively, if you are using Linux, install it as a package  
on Fedora/Centos/RHL  
```bash
sudo dnf install python-matplotlib
```  
on Ubuntu/Debian 
```bash
sudo apt-get install python-matplotlib
```
### To Run  
Clone the project,
```bash
git clone git@github.com:ubbn/random-walk-matplotlib.git
```

Switch to working directory
```bash
cd random-walk-matplotlib
```
To draw each step of the walk is as a connected line
```bash
python scr/visual_plot.py
```

To draw each step of the walk scattered points
```bash
python scr/visual_scatter.py
```

