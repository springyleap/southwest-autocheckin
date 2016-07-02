Southwest-Autocheckin
=====================

Yet another southwest checkin web-based system. Register your southwest/swa flights and the system will checkin for you _automatically 24hrs before departure_.

Go to [springyleap.com](http://springyleap.com) to try it out.

This system was inspired out of the original work by [Joe Beda's script](https://github.com/jbeda/southwest-checkin) and [Aaron Ortbals herokuapp](https://github.com/aortbals/southwest-checkin) southwest automatic checkin script and webapp respectively.

__The system is compatible with the latest changes done by the Southwest team in_May'16__ (API updates). This is a live project, and I keep updating it regularly to offer more functionality and/or fix issues find by its users. If you find any issues, please report them [here](mailto:flightautocheckin@sybleu.com) or raise an issue in this project.

__This system is for personal use only__.

***
New Features:
* fixed emailto field
* added new [python script](https://github.com/springyleap/southwest-autocheckin/tree/master/src/python/Southwest.Requests) with the basic functionality 

***

Existing Features
  * Domestic flights checkin.
  * Roundtrip and one way flights checkin
  * Multi-segment/stop flights checkin
  * Detects multiple travelers, but it only registers the name used to lookup the flight.

Missing Features
* Multiple traveler registration in a single ticket
* International flights
* SSL uses a different domain [springyleaf.com](https://www.springyleaf.com)
* Misc...
