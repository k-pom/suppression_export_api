module.exports = function(grunt) {
  // Show elapsed time after tasks run to visualize performance
  require('time-grunt')(grunt);

  // Load all Grunt tasks that are listed in package.json automagically
  require('load-grunt-tasks')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // clean up the static directories
    clean: ['<%= pkg.name %>/static'],

    // browserify stuff
    browserify: {
      dist: {
        options: {
          transform: [
            ["babelify", {
              loose: "all",
              optional: ["es7.decorators"]
            }]
          ]
        },
        files: {
          "<%= pkg.name %>/static/application.js": "<%= pkg.name %>/js/application.js"
        }
      }
    },

    // sass config
    sass: {
      options: {
        relativeAssets: false,
        outputStyle: 'expanded',
        sassDir: '<%= pkg.name>/sass'
      },
      build: {
        files: [{
          expand: true,
          cwd: '<%= pkg.name>/sass',
          src: ['**/*.{scss,sass}'],
          dest: '<%= pkg.name>/static',
          ext: '.css'
        }]
      },
      dist: {
        files: {
          "<%= pkg.name %>/static/application.css": "<%= pkg.name %>/sass/application.scss"
        }
      }
    },

    // uglify the things
    uglify: {
      build: {
        src: '<%= pkg.name %>/static/application.js',
        dest: '<%= pkg.name %>/static/application.js'
      }
    },

    // add cache busting to the assets
    filerev: {
      options: {
        algorithm: 'md5',
        length: 16,
        move: true,
        mapping: true
      },
      build: {
        src: '<%= pkg.name %>/static/**/*'
      }
    },

    // concurrent
    concurrent: {
      target: {
        tasks: ['build-watch', 'shell'],
        options: {
          logConcurrentOutput: true
        }
      }
    },

    // run the flask app in development mode
    shell: {
      target: {
        command: 'exporter/application.py'
      }
    },

    // build the static files on change
    watch: {
      build: {
        files: [
          '<%= pkg.name %>/js/**/*',
          '<%= pkg.name %>/sass/**/*'
        ],
        tasks: ['build']
      }
    }
  });

  // build the static assets
  grunt.registerTask('build', ['clean', 'sass', 'browserify', 'filerev']);

  // build and minify the assets
  grunt.registerTask('build-prod', ['clean', 'sass', 'browserify', 'uglify', 'filerev']);

  // build and watch
  grunt.registerTask('build-watch', ['build', 'watch']);

  // by default, build
  grunt.registerTask('default', ['concurrent:target']);
};
