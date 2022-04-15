from flask import Flask, request, jsonify
from my_sql import mysql_util

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_one_mysql():
    values = request.json
    table_name = values["table_name"]
    record = values["record"]
    values_string=''
    for k,v in record.items():
        values_string=values_string+repr(v)+','
    values_string='('+values_string[:-1]+')'
    result = my_sql_obj.execute_query(f"INSERT INTO {table_name} VALUES{values_string}")
    return jsonify(result)

@app.route('/get-all', methods=['POST'])
def get_all_mysql():
    values = request.json
    table_name = values["table_name"]
    result = my_sql_obj.execute_query_read(f"SELECT * FROM {table_name}")
    return jsonify(result)

@app.route('/get-selected', methods=['POST'])
def get_selected_mysql():
    values = request.json
    table_name = values["table_name"]
    record = values["where"]
    filter_string=''
    for k,v in record.items():
        filter_string=filter_string+str(k)+' = '+repr(v)+' AND '
    filter_string='('+filter_string[:-5]+')'
    result = my_sql_obj.execute_query_read(f"SELECT * FROM {table_name} WHERE{filter_string}")
    return jsonify(result)

@app.route('/update-selected', methods=['POST'])
def update_selected_mysql():
    values = request.json
    table_name = values["table_name"]
    record_update = values["update"]
    record_where = values["where"]

    # generate the update string
    update_string=''
    for k,v in record_update.items():
        update_string=update_string+str(k)+' = '+repr(v)+','
    update_string=update_string[:-1]

    # generate the where string
    where_string=''
    for k,v in record_where.items():
        where_string=where_string+str(k)+' = '+repr(v)+' AND '
    where_string='('+where_string[:-5]+')'

    result = my_sql_obj.execute_query(f"UPDATE {table_name} SET {update_string} WHERE{where_string}")
    return jsonify(result)

@app.route('/delete-all', methods=['POST'])
def delete_all_mysql():
    values = request.json
    table_name = values["table_name"]
    result = my_sql_obj.execute_query(f"DELETE FROM {table_name}")
    return jsonify(result)

@app.route('/delete-selected', methods=['POST'])
def delete_selected_mysql():
    values = request.json
    table_name = values["table_name"]
    where = values["where"]
    filter_string=''
    for k,v in where.items():
        filter_string=filter_string+str(k)+' = '+repr(v)+' AND '
    filter_string='('+filter_string[:-5]+')'
    result = my_sql_obj.execute_query(f"DELETE FROM {table_name} WHERE{filter_string}")
    return jsonify(result)


if __name__ == '__main__':
    global my_sql_obj
    host='bjnqjjyrdwceenpesae2-mysql.services.clever-cloud.com'
    user='ulbbyxidrojqjova'
    password= 'ZH9q5Hd0m9gBPhAZM7hy'
    database = 'bjnqjjyrdwceenpesae2'
    my_sql_obj = mysql_util(host,user,password,database)

    app.run(debug=True)