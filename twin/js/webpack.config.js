var path = require( 'path' );

var webpack = require('D:/coblan/webcode/node_modules/webpack')

//const VueLoaderPlugin = require('D:/coblan/webcode/node_modules/vue-loader/lib/plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports =
{
    //context:__dirname,
    mode: 'development', // 'production', //
    entry: {
        twin:'./main.js',
    },
    output: {
        path:path.resolve(__dirname, '../static/js'),
        filename: '[name].pack.js'
    },

    watch: true,
    resolve:{
        alias: {
            //jb_admin: path.resolve(__dirname,"../../case/jb_admin/js")
            twin:"D:/coblan/py3/fastdog/twin/js",
        },
        modules:["D:/coblan/webcode/node_modules"],
    },
    resolveLoader: {
        //moduleExtensions:["D:/coblan/webcode/node_modules"],
        modules: ["D:/coblan/webcode/node_modules"],
        //resolver:["D:/coblan/webcode/node_modules"],
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets:[
                            require.resolve('@babel/preset-env')
                        ]

                    }
                },
            },
            {
                test: /\.scss$/,
                use: [{
                    loader: "style-loader" // creates style nodes from JS strings
                }, {
                    loader: "css-loader" // translates CSS into CommonJS
                }, {
                    loader: "sass-loader" // compiles Sass to CSS
                }]
            },
            {
                test: /\.styl$/,
                use: [
                    {
                        loader: "style-loader" // creates style nodes from JS strings
                    },
                    {
                        loader: "css-loader" // translates CSS into CommonJS
                    },
                    {
                        loader: "stylus-loader" // compiles Stylus to CSS
                    }
                ]
            },
            {
                test: /\.less$/,
                use: [{
                    loader: 'style-loader' // creates style nodes from JS strings
                }, {
                    loader: 'css-loader' // translates CSS into CommonJS
                }, {
                    loader: 'less-loader' // compiles Less to CSS
                }]
            }
        ]

    },
    plugins: [
        new VueLoaderPlugin(),


        //new UglifyJSPlugin()
        //new webpack.DefinePlugin({
            //'process.env.NODE_ENV': JSON.stringify('production'),
        //}),
    ]
}



