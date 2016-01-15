## Mailgun Suppression API
This creates and manages exports of suppression data from Mailgun.
These suppression lists are a csv file of all suppressions of a given
type, grouped by domain, at the time of the file creation.

Libraries
 - Flask (for server side code / API)
 - Mongo DB (for storage of export metadata)
 - Cloud Files (for raw file storage and serving)
 - Swagger (for api documentation)
 - React/Redux (frontend UI)
 - Bootstrap (css/templating)

### Example
View demo here (todo: Make this a real link)

### Installation
TODO: Provide installation instructions

### To Do
- JS: Download Export
- Python/Cron: Generate export data (cloud files integration)
- Misc: Mongo connection after fork
- Setup on heroku
- Tool tips on status/type

### Feature List
- Paginate the number of exports
- Spinning Icons to indicate loading
- Validate create (right now it will queue anything)
- Limit to 1 file generated per TIMEFRAME (10 minutes?)
- Socket.io for push notifications, ie, file is ready for download
