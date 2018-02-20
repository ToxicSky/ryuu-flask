'use strict';

const gulp      = require('gulp'),
      minifyCSS = require('gulp-csso'),
      rename    = require('gulp-rename'),
      sass      = require('gulp-sass'),
      uglify    = require('gulp-uglify'),
      ts        = require('gulp-typescript'),
      babel     = require('gulp-babel');

var tsProject = ts.createProject('tsconfig.json');

gulp.task('styles', ['styles:vendor'], function () {
  return gulp.src(['./src/sass/**/*.scss', '!./src/sass/vendor/**/*.scss'])
    .pipe(sass().on('error', sass.logError))
    .pipe(minifyCSS())
    .pipe(rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest('./static/css'));
});

gulp.task('scripts', function () {
    return gulp.src('./src/scripts/**/*.ts')
      .pipe(tsProject())
        .js
        .pipe(babel({
            presets: ['env']
        })).pipe(uglify())
        .pipe(rename({
            suffix: '.min'
        }))
        .pipe(gulp.dest('./static/js'));
});

gulp.task('styles:vendor', ['styles:vendor:bootstrap', 'styles:vendor:font-awesome']);

gulp.task('styles:vendor:bootstrap', function() {
    return gulp.src('./node_modules/bootstrap/scss/**/*').pipe(gulp.dest('./styles/vendor/bootstrap'));
});

gulp.task('styles:vendor:font-awesome', function() {
    return gulp.src('./node_modules/font-awesome/scss/**/*').pipe(gulp.dest('./styles/vendor/font-awesome'));
});

gulp.task('build', ['styles', 'scripts']);