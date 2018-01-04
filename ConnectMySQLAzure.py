import mysql.connector

if __name__ == '__main__':
	try:
		database = mysql.connector.connect(user='libao%libao', password='baoli@bj123', database='libao', host="libao.mysqldb.chinacloudapi.cn")
		cursor = database.cursor()

	except mysql.connector.Error as err:
		print(err)
	else:
		print database.get_server_version()
		cursor.execute("SHOW VARIABLES LIKE '%have%ssl%'")
		print(cursor.fetchall())
		database.close	