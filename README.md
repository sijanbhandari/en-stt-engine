## To deploy to heroku

Clone this repository and navigte into the stt-api directory

Run the command below to loginto heroku within your terminal

`heroku login `

Create a heroku app within the heroku gui

Add the remote app you just created from the heroku through the terminal like below

`heroku git:remote -a lg-stt-engine `

Add the ` .buildpacks file` using the command below

`heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`


This will show

```
Buildpack added. Next release on lg-stt-engine will use:
  1. heroku/python
  2. https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
```

Then you should be able to deploy your app like below

```bash
git push heroku main:master  
```

To use the api,

use in postman with the body sending a file as a .wav file with the file keyword

Example below here

![postman demo](stt.png)