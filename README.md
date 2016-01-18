## Mailgun Suppression API
This creates and manages exports of suppression data from Mailgun.
These suppression lists are a csv file of all suppressions of a given
type, grouped by domain, at the time of the file creation.

Libraries
 - Flask (for server side code / API)
 - Mongo DB (for storage of export metadata)
 - Boto.s3 (for remote file storage)
 - Swagger (for api documentation)
 - React/Redux (frontend UI)
 - Bootstrap (css/templating)

### Example
View demo here: http://suppression-export.herokuapp.com/  
(Could be slow at first if the heroku dino is sleeping)

### Installation

First step, clone the repo onto your development machine
```
    git clone git@github.com:k-pom/suppression_export_api.git
    cd suppression_export_api
```

Set up the python side of things using virtualenvwrapper (https://virtualenvwrapper.readthedocs.org/en/latest/)
```
     mkvirtualenv suppression_export_api
     pip -r requirements.txt
```

Set up the tool necessary for the frontend/js
```     
    npm install -g grunt-cli
    npm install -g sass
    npm install
```

Last step, configure your env variables and start the server
```
    cp .env.example .env
    vi .env
    source .env
    grunt
```

### Additional Feature List
- Tooltip / UI features helpers
- Paginate the number of exports
- Spinning Icons to indicate loading
- Validate create (right now it will queue anything)
- Limit to 1 file generated per TIMEFRAME (10 minutes?)
- Socket.io for push notifications, ie, file is ready for download
