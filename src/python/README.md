Southwest-Autocheckin Python script
===================================

This is a stand alone python script using [Python v3.5.2](https://www.python.org/downloads/release/python-352/) to query and checkin southwest flight reservations.

__This system is for personal use only__.


_usage:_
_'SwaClient.py -c <confirmation #> -l <lastName> -f <firstName> -e <email>'_
_'SwaClient.py --confirmationNumber=<confirmation #> --lastName=<lastName> --firstName=<firstName> --email <email>'_

If you want to try the full system, go to [springyleap.com](http://springyleap.com)


The script is compatible with the latest changes done by the Southwest team in Late May'16 (REST API changes). This is a live project, and I keep updating it regularly to offer more functionality and/or fix issues find by its users. If you find any issues, please report them [here](mailto:flightautocheckin@sybleu.com) or raise an issue in this project.

***

__Development setup__

* Download [Python v3.5.2](https://www.python.org/downloads/release/python-352/) or above
* install [pip](https://pip.pypa.io/en/stable/installing/) if not installed yet
* install requests module (pip install requests)
* install latest azure sdk (pip install --pre azure)
* You can work with the script in any ide/text editor of your choice
* For [visual studio](http://www.visualstudio.com) users, I've added the .pyproj file

***

__Contributing__

* Fork it
* Create your feature branch (git checkout -b my-new-feature)
* Commit your changes (git commit -am 'Add some feature')
* Write rspec tests
* Push to the branch (git push origin my-new-feature)
* Create new Pull Request