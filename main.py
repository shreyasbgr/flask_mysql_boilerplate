from flask import Flask, request, jsonify
from my_sql import mysql_util

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_one_mysql():
    record = request.json
    print(record)
    values_string=''
    for k,v in record.items():
        values_string=values_string+repr(v)+','
    values_string='('+values_string[:-1]+')'
    result = my_sql_obj.execute_query(f"INSERT INTO testtable VALUES{values_string}")
    return jsonify(result)

if __name__ == '__main__':
    global my_sql_obj
    host='bjnqjjyrdwceenpesae2-mysql.services.clever-cloud.com'
    user='ulbbyxidrojqjova'
    password= 'ZH9q5Hd0m9gBPhAZM7hy'
    database = 'bjnqjjyrdwceenpesae2'
    my_sql_obj = mysql_util(host,user,password,database)

    app.run(debug=True)