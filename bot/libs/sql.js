const mysql = require('mysql2/promise')

const pool = mysql.createPool({
	host: 'db',
	user: process.env.MYSQL_USER,
	password: process.env.MYSQL_PASSWORD,
	database: process.env.MYSQL_DATABASE,
	waitForConnections: true,
	connectionLimit: 10,
	queueLimit: 0
})
module.exports = pool