# What The Flexbox?!

![](http://flexbox.io/images/share.png)

Exercises for the "What The Flexbox?!" video course. Videos available at <http://flexbox.io>


autoprefixer.github.io  Used to build your css so that it will work for other browsers.

Install Gulp
	go in to directory with files.
	npm init
	npm install gulp -g  // install globally
	copy con gulpfile.js
	npm install gulp --save-dev
	npm install gulp-autoprefixer --save-dev
	code for gulpfile.js:
		var gulp = require('gulp');
		var autoprefixer = require('gulp-autoprefixer');

		gulp.task('styles', function() {
			gulp.src('style.css')
				.pipe(autoprefixer())
				.pipe(gulp.dest('build'))
		});

		gulp.task('watch', function() {
			gulp.watch('styles.css', ['styles'])
		});

	in command line, type 'gulp styles' to run that task.
	type 'gulp watch' to constantly compile the css.