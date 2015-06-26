'use strict';

// Load required files that aren't auto-loaded by
// gulp-load-plugins (see below)
var argv          = require('yargs').argv,
  fs              = require('fs'),
  gulp            = require('gulp'),
  mainBowerFiles  = require('main-bower-files'),
  merge           = require('merge-stream'),
  minifyCss       = require('gulp-minify-css'),
  path            = require('path');

// This will load any gulp plugins automatically that
// have this format ('gulp-pluginName' [can only have one dash])
// The plugin can used as $.pluginName 
var $ = require('gulp-load-plugins')();

// Browser Sync
var browserSync = require('browser-sync'),
    reload      = browserSync.reload;

// Paths
var bowerPath           = 'static_dev/bower_components',
    coffeescriptsPath   = 'static_dev/coffeescripts',
    cssPath             = 'static_dev/css',
    javascriptsPath     = 'static_dev/javascripts',
    imagesPath          = 'static_dev/images',
    sassPath            = 'static_dev/scss',
    templatesPath       = 'static_dev/coffeescripts';

// Get Folder Function (from paths)
function getFolders(dir) {
  return fs.readdirSync(dir)
    .filter(function(file) {
      return fs.statSync(path.join(dir, file)).isDirectory();
    });
}

// Main serve task
// Watches coffee, js, and scss files for changes
gulp.task('serve', ['javascript'], function() {
  browserSync({
    proxy: 'localhost:5000',
    port: '8000'
  });
  gulp.watch([
    'static_dev/coffeescripts/**/*.coffee',
    'static_dev/coffeescripts/**/models/*', 
    'static_dev/coffeescripts/**/collections/*', 
    'static_dev/coffeescripts/**/views/*',
    'static_dev/coffeescripts/**/routers/*',
  ], ['coffee']);
  gulp.watch([
    'static_dev/javascripts/**/*.js',
    'static_dev/javascripts/**/models/*', 
    'static_dev/javascripts/**/collections/*', 
    'static_dev/javascripts/**/views/*',
    'static_dev/javascripts/**/routers/*',
  ], ['javascript']);
  gulp.watch('static_dev/coffeescripts/**/templates/*.eco', ['eco']);
  gulp.watch('static_dev/scss/**/*.scss', ['sass']);
  gulp.watch(['static/javascripts/*.js', 'static/stylesheets/*.css']).on('change', reload);
});

/* Shell tasks */

// Quick ways of running python and client related tasks
gulp.task('apache', $.shell.task(['sudo service httpd restart']))
gulp.task('backbonescaffold', $.shell.task([
  'mkdir static_dev/coffeescripts/' + argv.appname + '/models/',
  'mkdir static_dev/coffeescripts/' + argv.appname + '/collections/',
  'mkdir static_dev/coffeescripts/' + argv.appname + '/views/',
  'mkdir static_dev/coffeescripts/' + argv.appname + '/routers/',
  'mkdir static_dev/coffeescripts/' + argv.appname + '/templates/',
]))
gulp.task('collectstatic', $.shell.task([
  'echo "yes" | ./manage.py collectstatic',
  'sudo service httpd restart',
]))
gulp.task('startapp', $.shell.task([
  'django-admin.py startapp ' + argv.appname,
  'mkdir static_dev/coffeescripts/' + argv.appname,
  'mkdir static_dev/javascripts/' + argv.appname,
  'mkdir static_dev/sass/' + argv.appname,
  'mkdir templates/' + argv.appname,
]))

/* Main bower tasks */

/*  mainBowerFiles looks in an npm package's bower.json file
    for the 'main' entry - http://bower.io/docs/creating-packages/#main
    - and loops through the files listed there */

// Uglify's all bower/vendor scripts into single file
gulp.task('bower-scripts', function() {
  return gulp.src(mainBowerFiles())
    // Filter javascript files
    .pipe($.filter('*.js'))
    // Concat to single file
    .pipe($.concat('vendor.js'))
    // Remove whitespace and uglify
    .pipe($.uglify())
    // Restore filtered files
    .pipe($.filter('*.js').restore())
    // Rename the file
    .pipe($.rename('vendor.min.js'))
    // Copy to static folder
    .pipe(gulp.dest('static/javascripts'))
});

// Concats all bower/vendor styles into single file
gulp.task('bower-styles', function() {
  return gulp.src(mainBowerFiles())
    // Filter CSS files
    .pipe($.filter('*.css'))
    // Concat to single file
    .pipe($.concat('vendor.css'))
    // Restore filtered files
    .pipe($.filter('*.css').restore())
    // Copy to static folder
    .pipe(gulp.dest('static/stylesheets'))
});

/* Main scripts tasks */

// Coffeescript task
// If coding in coffee, this will compile and copy files to the 
// static javascript directory
gulp.task('coffee', function() {
  var folders = getFolders(coffeescriptsPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src(
    [
      'static_dev/coffeescripts/' + folder + '/*.coffee', 
      'static_dev/coffeescripts/' + folder + '/models/*', 
      'static_dev/coffeescripts/' + folder + '/collections/*', 
      'static_dev/coffeescripts/' + folder + '/views/*', 
      'static_dev/coffeescripts/' + folder + '/routers/*'
    ],  { base: 'static_dev/coffeescripts/' + folder })
      // Compile to JS
      .pipe($.coffee())
      // Concat files
      .pipe($.concat(folder + '.js'))
      // Check integrity
      .pipe($.jshint())
      // Remove whitespace and uglify
      .pipe($.uglify())
      // Rename the file
      .pipe($.rename(folder + '.min.js'))
      // Copy it to static folder
      .pipe(gulp.dest('static/javascripts'))
  });

  // Combines the streams and ends only when all streams emitted end
  return merge(tasks);

});

// ECO Template Task
// Compiles and concats html.eco files used in Backbone
gulp.task('eco', function() {
  var folders = getFolders(templatesPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src('static_dev/coffeescripts/' + folder + '/templates/*.eco', 
      { base: 'static_dev/coffeescripts/' + folder + '/templates'})
      // Compile eco to JS
      .pipe($.eco())
      // Concat files
      .pipe($.concat(folder + '.templates.js'))
      // Remove whitespace and uglify
      .pipe($.uglify())
      // Rename the file
      .pipe($.rename(folder + '.templates.min.js'))
      // Copy it to static folder
      .pipe(gulp.dest('static/javascripts'))
  });

  return merge(tasks);
});

// Javascript task
// If coding in Javascript, this will concat, jshint, and uglify
// Also converts to coffee and copies to coffeescripts directory
// to keep folders in sync
gulp.task('javascript', function() {
  var folders = getFolders(javascriptsPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src(
    [
      'static_dev/javascripts/' + folder + '/*',
      'static_dev/javascripts/' + folder + '/models/*', 
      'static_dev/javascripts/' + folder + '/collections/*', 
      'static_dev/javascripts/' + folder + '/views/*',
      'static_dev/javascripts/' + folder + '/routers/*',
    ], { base: 'static_dev/javascripts/' + folder })
      // concat files
      .pipe($.concat(folder + '.js'))
      // Check integrity
      .pipe($.jshint())
      // Remove whitespace and uglify
      .pipe($.uglify())
      // Rename the file
      .pipe($.rename(folder + '.min.js'))
      // Copy it to static folder
      .pipe(gulp.dest('static/javascripts'))
  });

  return merge(tasks);
});

/* Main styles tasks */

// CSS Task
// Concats and minifies css files
gulp.task('css', function() {
  var folders  = getFolders(cssPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src('static_dev/css/' + folder + '/*.css',
      { base: 'static_dev/css/' + folder })
      // Concat files
      .pipe($.concat(folder + '.css'))
      // Minify CSS
      .pipe(minifyCss({ compatibility: 'ie8' }))
      // Post CSS processor
      .pipe($.postcss([
        require('autoprefixer-core')({ browsers: ['last 1 version'] })
      ]))
      // Rename the file
      .pipe($.rename(folder + '.min.css'))
      // Copy it to static folder
      .pipe(gulp.dest('static/stylesheets'))
  });

  return merge(tasks);
});

// SASS Task
// Compiles, concats, minifies, and versions scss files
gulp.task('sass', function() {
  var folders = getFolders(sassPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src('static_dev/scss/' + folder + '/*.scss',
      { base: 'static_dev/scss/' + folder })
      // Compile to CSS
      .pipe($.sass({
        outputStyle: 'nested',
        precision: 10,
        includePaths: ['.'],
        onError: console.error.bind(console, 'Sass error:')
      }))
      // Concat files
      .pipe($.concat(folder + '.css'))
      // Minify CSS
      .pipe(minifyCss({ compatibility: 'ie8' }))
      // Post CSS processor
      .pipe($.postcss([
        require('autoprefixer-core')({ browsers: ['last 1 version'] })
      ]))
      // Rename the file
      .pipe($.rename(folder + '.min.css'))
      // Copy it to static folder
      .pipe(gulp.dest('static/stylesheets'))
  });

  return merge(tasks);
});

/* Main image tasks */

/*  Images Task
    Optimizes images and places copies in static/app_name/*.{jpg|png}
 
    This task needs to be run manually. It is not triggered by anything
    other than 'build' */

/* Needs a bit of work/research
   it works fine, but could be further
   optimized */
gulp.task('images', function() {
  var folders = getFolders(imagesPath);
  var tasks   = folders.map(function(folder) {
    return gulp.src('static_dev/images/' + folder  + '/*', 
      { base: 'static_dev/images/' })
      .pipe($.imagemin({
        progressive: true,
        interlaced: true,
        svgoPlugins: [{cleanupIDs: false}]
      }))
      .pipe(gulp.dest('static/images'));
  });

  return merge(tasks);
});

// Define the tasks
gulp.task('default',  ['serve']);
gulp.task('bower',    ['bower-scripts', 'bower-styles']);
gulp.task('scripts',  ['coffee', 'eco', 'javascript'])
gulp.task('styles',   ['css', 'sass']);
gulp.task('build',    ['bower', 'scripts', 'styles', 'images'])
