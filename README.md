#Miami Herald graphics template

This is a Python/Google Doc-powered static page generator for building interactive graphics on the Miami Herald's website. 

This was inspired by [NPR visual team's app template](https://github.com/nprapps/app-template) and is a work in progress. More updates to come.


###How to start building

1. Clone repo.

2. Rename folder to project name.

3. In Terminal, `cd` into folder.

4. Active LiveReload and place folder into app.

5. Run `python app.py` to start app. 

6. In Google Spreadsheets, copy from [template](https://docs.google.com/spreadsheets/d/1EB0Xq0mt_MkszaBHeSpIWGdlSnt0errmxo7pQqTdvCw/edit#gid=0) and make a new document. Add key and value headers to first two columns. 

7. Find Doc's special key and replace it in `app_config.py`.

8. Whenver you want to update text, `cd` into project folder and run `fab text`.

Note: Make sure tab in Doc is named `content` and include that in template tags in `index.html` and `base.html`. 