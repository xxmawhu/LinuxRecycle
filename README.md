# LinuxRecycle
A recycle system for linux
## How to install?
```bash
python setup.py install [--user]
```
or
```bash
pip install LinuxRecycle [--user]
```

## Usage

*  Delete a file or folder
```
del [options] filename
```
> * -f remove the file or dictory forcely

* Show all files which have been deleted
```
del.printDB [options] [num]
```
For example, only show the last 10 file
```
del.printDB -n 5
```
you will see 
```
1220 Tue Dec 29 13:46:50 2020 xxxxxxxxx
1221 Tue Dec 29 13:46:50 2020 xxxxxxxxx
1222 Tue Dec 29 13:46:50 2020 xxxxxxxxx
1223 Tue Dec 29 13:46:56 2020 xxxxxxxxx
1224 Tue Dec 29 13:46:56 2020 xxxxxxxxx
1225 Tue Dec 29 13:53:16 2020 oh-my-god
```

* Recovery the file that deleted
```
del.recover [num] # i.e 1225
```


## setup your crontab
```
14 4 * * * python /pathto/auto_clear.py
```
```sh
git clone https://github.com/xxmawhu/LinuxRecycle.git
cd LinuxRecycle/core
python3 setCrontab.py
```
