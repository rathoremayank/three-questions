'use strict';

const mysql = require('mysql');

// local mysql db connection

const dbConn = mysql.createConnection({
    host : 'database-container',
    user : 'dev',
    password : 'GodMode@94',
    database : 'todo-database',
    port: '3306'
});

dbConn.connect(function(err) {
    if (err) throw err;
    console.log("Database Connected!");
});

module.exports = dbConn;
