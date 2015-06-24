#Miami Herald graphics template

This is the Miami Herald's template for buidling interactive graphics online.

The template is an upgrade from a [previous version](https://github.com/chrisalcantara/herald-app-template) written in Python.

The new version, inspired by The Texas Tribune's [graphic template](https://github.com/texastribune/newsapps-graphic-kit), is written in JavaScript with task management handled by [Gulp](http://gulpjs.com/).

###What's in the box

CSS:

+ Bootstrap - Responsiveness
+ `_base.scss` - Miami Herald styles imported into `styles.scss`.

JS:

+ D3 - Data visualizations
+ jQuery – DOM manipulation
+ Bootsrap – Bootstrap components
+ Modernizr – Detection
+ Sinclair – Miami Herald's libaray
	

HTML:

+ `base.html` – Uniform page. This is where everything but the content is built, including SEO and footer.

+ `index.html` - Where the content lives, which includes headline, byline and text.


GULP:

+ BrowserSync - Live browser
+ SASS - SCSS/CSS compilling
+ JSHint - JavaScript linting
+ Nunjucks - JavaScript templating

More to come...

###How to start building

Before you begin, make sure you have [Node.js](https://nodejs.org/) installed on your computer.

If all systems go:

1. Clone repo.

2. Rename folder to project name.

3. In Terminal, `cd` into folder.

4. If there is no `node modules` folder, run `npm install`. All Node.js dependencies are in `package.json`.

5. `cd` into `app`. Then run `bower-installer -r` for all CSS and JS libraries. Settings are in `bower.json`.

6. To start working, go to command line and run `gulp`. Any tasks can be found in `gulpfile.js`.

6a. During development, run `jshint /path/to/file.js` for any JS files Gulp isn't watching.

7. Once finished. Run `gulp build` to create file. You're done!

###Working with Google Sheets

1. In Google Spreadsheets, copy from this [template](https://docs.google.com/spreadsheets/d/1EB0Xq0mt_MkszaBHeSpIWGdlSnt0errmxo7pQqTdvCw/edit#gid=0) and make a new document.

2. Using oAuth2, you need to make sure you're authorized to use the spreadsheet. At the project root, run `npm run authorize`. Any problems can be configured in `/bin/authorize.js`.

3. Next, go into `bin/fetch_spreadsheet.js` and change the `google_spreadsheet_key` to your spreadsheet's key.

4. If there's anything wrong. Check to make sure you have the following at the ~. `~/.mh_app_google_client_secrets.json
~/.mh_app_token.json`

5. Whenever you have to update text, run `npm run fetch/spreadsheet`. The spreadsheet is downloaded into `data.json`, which nunjucks will take and write into templates in the `index.html` and `base.html` files.

Questions or suggestions? Contact me at [calcantara@miamiherald.com](mailto:calcantara@miamiherald.com)