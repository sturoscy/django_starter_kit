'use strict';

require('es6-promise').polyfill();

// Load required files that aren't auto-loaded by
// gulp-load-plugins (see below)
var argv            = require('yargs').argv,
    fs              = require('fs'),
    gulp            = require('gulp'),
    mainBowerFiles  = require('main-bower-files'),
    merge           = require('merge-stream'),
    minifyCss       = require('gulp-minify-css'),
    path            = require('path'),
    taskListing     = require('gulp-task-listing');

// Browserify specific
var babelify = require('babelify'),
    browserify = require('browserify'),
    source = require('vinyl-source-stream');

// This will load any gulp plugins automatically that
// have this format ('gulp-pluginName' [can only have one dash])
// The plugin can used as $.pluginName 
var $ = require('gulp-load-plugins')();

// Browser Sync
var browserSync = require('browser-sync'),
    reload      = browserSync.reload;
 
// Add a task to render the output
// Used for $-> gulp help
gulp.task('help', taskListing);

// Paths
var cssPath         = 'static_dev/css',
    javascriptsPath = 'static_dev/javascripts',
    imagesPath      = 'static_dev/images',
    sassPath        = 'static_dev/sass';

// Get Folder Function (from paths)
function getFolders(dir) {
    return fs.readdirSync(dir)
        .filter(function(file) {
            return fs.statSync(path.join(dir, file)).isDirectory();
        });
}

// Main serve task
// Watches coffee, js, and scss files for changes. Will restart
// apache and reload browser automatically
gulp.task('serve', function() {
    gulp.watch([
        'static_dev/javascripts/**/app.js',
        'static_dev/javascripts/**/**/*.js'
    ], ['scripts-browserify', 'shell-apache']);
    gulp.watch('static_dev/css/**/*.css', ['styles-css', 'shell-apache']);
    gulp.watch('static_dev/sass/**/*.scss', ['styles-sass', 'shell-apache']);
});

/* Shell tasks */

// Quick ways of running python and client related tasks
gulp.task('shell-apache', $.shell.task(['sudo service httpd restart']))

/* Main bower tasks */
gulp.task('bower', ['bower-scripts', 'bower-styles']);

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
        // Minify CSS
        .pipe(minifyCss({ compatibility: 'ie9', rebase: false }))
        // Post CSS processor
        .pipe($.postcss([
            require('autoprefixer')({ browsers: ['last 1 version'] })
        ]))
        // Copy to static folder
        .pipe(gulp.dest('static/stylesheets'))
});

/* Main scripts tasks */
gulp.task('scripts', ['scripts-browserify'])

// Browserify task
gulp.task('scripts-browserify', function() {
    var folders = getFolders(javascriptsPath);

    var tasks = folders.map(function(folder) {
        return browserify({
            entries: ['./static_dev/javascripts/' + folder + '/app.js'],
            debug: true
        })
            .transform(babelify,  { presets: ['es2015', 'react'] })
            .bundle()
                .pipe(source(folder + '.js'))
                //.pipe($.uglify())
                .pipe($.rename(folder + '.min.js'))
                .pipe(gulp.dest('./static/javascripts/'));
    });

    return merge(tasks);
});

/* Main styles tasks */
gulp.task('styles', ['styles-sass']);

// CSS Task
// Concats and minifies css files
gulp.task('styles-css', function() {
    var folders  = getFolders(cssPath);
    var tasks   = folders.map(function(folder) {
        return gulp.src('static_dev/css/' + folder + '/*.css',
            { base: 'static_dev/css/' + folder }
        )
            // Concat files
            .pipe($.concat(folder + '.css'))
            // Minify CSS
            .pipe(minifyCss({ compatibility: 'ie9', rebase: false }))
            // Post CSS processor
            .pipe($.postcss([
                require('autoprefixer')({ browsers: ['last 1 version'] })
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
gulp.task('styles-sass', function() {
    var folders = getFolders(sassPath);
    var tasks   = folders.map(function(folder) {
        return gulp.src(['static_dev/sass/' + folder + '/*.scss'], 
            { base: 'static_dev/sass/' + folder }
        )
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
            //.pipe(minifyCss({ compatibility: 'ie9', rebase: false }))
            // Post CSS processor
            .pipe($.postcss([
                require('autoprefixer')({ browsers: ['last 1 version'] })
            ]))
            // Rename the file
            .pipe($.rename(folder + '.min.css'))
            // Copy it to static folder
            .pipe(gulp.dest('static/stylesheets'))
    });

    return merge(tasks);
});

/* Main image tasks */
gulp.task('media', ['images']);

/*  Images Task
    Optimizes images and places copies in static/app_name/*.{jpg|png}

    This task needs to be run manually. It is not triggered by anything
    other than 'build' */
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

gulp.task('build', ['bower', 'scripts', 'styles'])
