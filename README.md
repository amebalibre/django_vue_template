# Instalation guide

1.  Start project `django-admin startproject my_project`
2.  Navigate to project folder
3.  Create a virtualenv `virtualenv .env`
4.  Use virtual environment `source .env/bin/activate`
5.  Install django `pip install django`
5.  Install postgres connector `pip install psycopg2-binary`
6.  Execute first migration `./manage.py  migrate`
7.  You can run server now! `./manage.py runserver`
8.  Install vue-cli `su -c "npm install -g vue-cli"`
9.  Download the vue webpack template `vue init webpack src` [More info](https://github.com/vuejs-templates/webpack)
10. The previous point initialize a assistant. Follow this steps:

    ```
    ? Project name src
    ? Project description Vue.js src
    ? Author ****
    ? Vue build standalone
    ? Install vue-router? Yes
    ? Use ESLint to lint your code? Yes
    ? Pick an ESLint preset Standard
    ? Set up unit tests Yes
    ? Pick a test runner jest
    ? Setup e2e tests with Nightwatch? Yes
    ? Should we run `npm install` for you after the project has been created? (recom
    mended) npm
    ```


# django_vue_template

> A Django + Vue.js project template

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).



# REFERENCE GUIDE

*  [Routing](https://medium.freecodecamp.org/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9)
