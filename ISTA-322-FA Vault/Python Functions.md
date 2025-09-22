## SQL:
#### `get_conn_cur()`:
> Returns connector and cursor instance for database access
```Python
mysql_address  = '131.193.32.85'
mysql_username='de_student'
mysql_password='DE_Student_PaSS'
#We are going to use a single database for all databases in this course.

#To avoid confusion, we use databasename_tablename naming convention.
mysql_database = 'my_dataengineering_dbs'

def get_conn_cur():
    cnx = mysql.connector.connect(user=mysql_username, password=mysql_password,
          host=mysql_address,
          database=mysql_database, port='3306');
    return (cnx, cnx.cursor())
```
#### `get_table_names()`:
>Returns all table names of current database
```Python
def get_table_names():
    conn, cur = get_conn_cur() # get connection and cursor
    
    # query to get table names from my_data_engineering_dbs schema
    table_name_query = """ 
    SELECT table_name FROM information_schema.tables
    WHERE table_schema = 'my_dataengineering_dbs'; """

    # df = pd.read_sql(table_name_query, conn)
    cur.execute(table_name_query) # execute
    my_data = cur.fetchall() # fetch results
    
    # create a dataframe from the return data
    result_df = pd.DataFrame(my_data, columns=cur.column_names)

    cur.close() #close cursor
    conn.close() # close connection
    
    return  result_df
```
#### `get_column_names()`:
>Returns all column names from specified "table_name" parameter
```Python
def get_column_names(table_name): # arguement of table_name
  conn, cur = get_conn_cur() # get connection and cursor

  # Now select column names while inserting the table name into the WERE
  column_name_query =  """SELECT column_name FROM information_schema.columns
       WHERE table_name = '%s' """ %table_name

  cur.execute(column_name_query) # exectue
  my_data = cur.fetchall() # store
  result_df = pd.DataFrame(my_data, columns=cur.column_names)

  cur.close() # close
  conn.close() # close
  
  return result_df # return
```
#### `run_query()`:
>Returns tuple of list of column names and list of tuples of requested data
```Python
def run_query(query_string):
  conn, cur = get_conn_cur() # get connection and cursor

  cur.execute(query_string) # executing string as before
  
  my_data = cur.fetchall() # fetch query data as before
  result_df = pd.DataFrame(my_data, columns=cur.column_names)
  
  cur.close() # close
  conn.close() # close
  
  return result_df
```
