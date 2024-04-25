/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                pastelgreen: {
                    DEFAULT: '#21c55d',
                    100: '#072713',
                    200: '#0d4e25',
                    300: '#147638',
                    400: '#1b9d4a',
                    500: '#21c55d',
                    600: '#3fde7a',
                    700: '#6fe79b',
                    800: '#9fefbc',
                    900: '#cff7de'
                  },
                  platinum: {
                    DEFAULT: '#ebe9e9',
                    100: '#312d2d',
                    200: '#635959',
                    300: '#928787',
                    400: '#bfb8b8',
                    500: '#ebe9e9',
                    600: '#efeeee',
                    700: '#f3f2f2',
                    800: '#f7f6f6',
                    900: '#fbfbfb'
                  },
                  dimgray: {
                    DEFAULT: '#646165',
                    100: '#141314',
                    200: '#282729',
                    300: '#3c3a3d',
                    400: '#504e51',
                    500: '#646165',
                    600: '#848085',
                    700: '#a3a0a4',
                    800: '#c1c0c2',
                    900: '#e0dfe1'
                  },
                  celestialblue: {
                    DEFAULT: '#008dd5',
                    100: '#001d2b',
                    200: '#003956',
                    300: '#005681',
                    400: '#0072ab',
                    500: '#008dd5',
                    600: '#12b0ff',
                    700: '#4ec4ff',
                    800: '#89d8ff',
                    900: '#c4ebff'
                  },
                  pinkcrayola: {
                    DEFAULT: '#f56476',
                    100: '#41040b',
                    200: '#820817',
                    300: '#c40c22',
                    400: '#f1243c',
                    500: '#f56476',
                    600: '#f78492',
                    700: '#f9a3ad',
                    800: '#fbc2c8',
                    900: '#fde0e4'
                  }
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
}
