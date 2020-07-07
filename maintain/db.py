def read_cursor(cursor):
    rows =[]
    for row in cursor:
        row_dc = {}
        for index, head in enumerate(cursor.description):
            row_dc[head[0]] = row[index]
        rows.append(row_dc)
    return rows

def write_cursor(src_cursor,dst_cursor,table):
    
    keys = [head[0] for head in src_cursor.description]
    sql_data = []
    for row in src_cursor:
        sql_data.append(row)
    print(len(sql_data))
    keys_str = ','.join(keys)
    keys_p = ','.join(['%s' for x in keys])
    sql = ''' INSERT INTO 
    %(table)s ( %(key_str)s )
    VALUES
    (%(keys_p)s)
    '''%{'table':table,'key_str':keys_str,'keys_p':keys_p}
    dst_cursor.executemany(sql,sql_data)