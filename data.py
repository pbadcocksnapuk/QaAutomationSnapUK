import sqlite3
# commit
# Connect to the database
conn = sqlite3.connect("snap_analytics")
cursor = conn.cursor()

# Execute a SELECT query to fetch the column names
cursor.execute("PRAGMA table_info(auto_test_20230615)")
columns = [column[1] for column in cursor.fetchall()]

# Execute a SELECT query to fetch the table data
cursor.execute("SELECT * FROM snapanalytics.auto_test_20230615")
rows = cursor.fetchall()
#
# def postgres(database: str, minconn=1, maxconn=20, connect_timeout=1000, name=None):
#     """
#
#     :param database: Name of database
#     :param minconn: minimum connection you need
#     :param maxconn: max connection you need
#     :param connect_timeout: timeout
#     :param name: name if you are trying to use more than one pool with same database, default None
#     :return:
#     """
#     my_pool: AsyncConnectionPool
#     my_pool = _get_pool(database, minconn, maxconn, connect_timeout, name)
#     with my_pool.connection() as conn:
#         yield conn
#
# with postgres("snap_analytics") as con:  # greates connection or gives you connection
#     cursor.execute(
#         f'''select * FROM snapanalytics.auto_test_20230615
#         ''', con)
# rows = cursor.fetchall()

# Create the nested list representation of the table
table_data = [columns]
table_data.extend(rows)

# Close the database connection
conn.close()

# Print the nested list
for row in table_data:
    print(row)

#     git config --global --add safe.directory C:/Users/pbadcock/PycharmProjects/seliniumStarter