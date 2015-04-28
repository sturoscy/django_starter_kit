'use strict';

// Load required files
var gulp            = require('gulp'),
    mainBowerFiles  = require('main-bower-files'),
    $               = require('gulp-load-plugins')();

var browserSync = require('browser-sync');
var reload      = browserSync.reload;

// Main serve task
// Watches coffee, js, and scss files for changes
gulp.task('serve', function() {
    browserSync({ proxy: 'http://localhost:8001' });

    gulp.watch([
        'static_dev/coffeescripts/*.coffee',
        'static_dev/coffeescripts/**/*.coffee',
        'static_dev/coffeescripts/**/models/*', 
        'static_dev/coffeescripts/**/collections/*', 
        'static_dev/coffeescripts/**/views/*',
        'static_dev/coffeescripts/**/routers/*',
    ], ['coffee']);
    gulp.watch('static_dev/coffeescripts/**/templates/*.eco', ['eco']);
    gulp.watch('static_dev/scss/**/*.scss', ['sass']);
    gulp.watch(['static/javascripts/*.js', 'static/stylesheets/*.css']).on('change', reload);
});

// Main bower task
// Uglify's all bower/vendor scripts into single file
gulp.task('bower', function() {
    return gulp.src(mainBowerFiles())
        .pipe($.filter('*.js'))
        .pipe($.concat('vendor.js'))
        .pipe($.uglify())
        .pipe(gulp.dest('static/javascripts'))
        .pipe($.filter('*.js').restore())
        .pipe($.filter('*.css'))
        .pipe($.concat('vendor.css'))
        .pipe(gulp.dest('static/stylesheets'))
        .pipe($.filter('*.css').restore())
});

// Coffeescript task
// If coding in coffee, this will compile, concat, and uglify
// Also moves compiled scripts to the javascript directory for reference
gulp.task('coffee', function() {
    return gulp.src(
        [
            'static_dev/coffeescripts/*.coffee',
            'static_dev/coffeescripts/**/*.coffee',
            'static_dev/coffeescripts/**/models/*', 
            'static_dev/coffeescripts/**/collections/*', 
            'static_dev/coffeescripts/**/views/*',
            'static_dev/coffeescripts/**/routers/*',
        ])
        .pipe($.coffee())
        .pipe(gulp.dest('static_dev/javascripts'))
        .pipe($.concat('app.js'))
        .pipe($.jshint())
        .pipe($.uglify())
        .pipe(gulp.dest('static/javascripts'))
});

// Javascript task
// If coding in Javascript, this will concat, jshint, and uglify
gulp.task('javascripts', function() {
    return gulp.src(
        [
            'static_dev/javascripts/*.js',
            'static_dev/javascripts/**/*.js'
            'static_dev/javascripts/**/models/*', 
            'static_dev/javascripts/**/collections/*', 
            'static_dev/javascripts/**/views/*',
            'static_dev/javascripts/**/routers/*',
        ]
    )
    .pipe($.concat('app.js'))
    .pipe($.jshint()) 
    .pipe($.uglify())
    .pipe(gulp.dest('static/javascripts'))    
});

// ECO Template Task
// Compiles and concats JST files used in Backbone
gulp.task('eco', function() {
    return gulp.src('static_dev/coffeescripts/**/templates/*.eco')
        .pipe($.eco())
        .pipe($.concat('templates.js'))
        .pipe(gulp.dest('static/javascripts'))
});

// SASS Task
// Compiles, concats, minifies, and versions scss files
gulp.task('sass', function() {
    return gulp.src([
        'static_dev/scss/*.scss',
        'static_dev/scss/**/*.scss'
    ])
        .pipe($.sass({
            outputStyle: 'nested',
            precision: 10,
            includePaths: ['.'],
            onError: console.error.bind(console, 'Sass error:')
        }))
        .pipe($.concat('custom.css'))
        .pipe($.postcss([
            require('autoprefixer-core')({ browsers: ['last 1 version'] })
        ]))
        .pipe(gulp.dest('static/stylesheets/'))
});

// Images Task
// Optimizes images
gulp.task('images', function() {
    return gulp.src(['static_dev/img/**/*'])
        .pipe($.cache($.imagemin({
            progressive: true,
            interlaced: true,
            svgoPlugins: [{cleanupIDs: false}]
        })))
        .pipe(gulp.dest('static/img'));
});

// Define the tasks
gulp.task('default', ['serve']);
gulp.task('build', ['bower', 'coffee', 'javascripts', 'eco', 'images', 'sass']);
