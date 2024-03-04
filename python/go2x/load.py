import os
import tarfile
import mysql.connector
import platform

# clean install -DskipTests=true -f pom.xml
# clean install -Dmaven.javadoc.skip=true -Dgpg.skip=true -Dmaven.source.skip=true -DskipTests=true -f pom.xml
# NACOS_DISCOVERY_IP=127.0.0.1

def extract_tar_gz():
    try:
        directory = os.getcwd()
        print(directory)
        for file_name in os.listdir(directory):
            # 如果文件是以.tar.gz结尾的文件
            if file_name.endswith(".tar.gz"):
                tar_gz_file = os.path.join(directory, file_name)
                fileBaseName = os.path.basename(tar_gz_file).replace('.tar.gz', '')
                fileName = f'{directory}/load-{fileBaseName}.sh'
                if os.path.exists(fileName):
                    print(f"文件 '{fileName}' 已存在。")
                    # break
                # 解压tar.gz文件
                with tarfile.open(tar_gz_file, "r:gz") as tar:
                    tar.extractall()
                    # 遍历解压后的文件和目录
                    for member in tar.getmembers():
                        # 将解压后的目录加入列表
                        if member.isdir():
                            generate_sql_code(member.name, fileBaseName)
                            print("成功解压文件:", tar_gz_file)
                            break
    except Exception as e:
        print("解压文件时出现错误:", str(e))

def execSql(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        if cursor.rowcount > 0:
            print(f'{sql}执行成功')
        else:
            print(f'{sql}执行失败! -> 影响行数为0')
        cursor.close()
    except Exception as e:
        print(f'{sql}执行失败: {e.__str__}')

def generate_sql_code(directory, fileName):
    pwdPath = os.getcwd()
    if not os.path.isdir(directory):
        print("目录不存在:", directory)
        return
    # 建立MySQL连接
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="yuri",
        database="mysql" 
    )
    # 获取目录下的所有 .sql 文件
    sql_files = [file for file in os.listdir(directory) if file.endswith('.sql')]

    # 生成 SQL 代码
    sql_code = ''
    for sql_file in sql_files:
        base_name = os.path.splitext(sql_file)[0]
        execSql(connection, f"DROP DATABASE IF EXISTS {base_name};")
        execSql(connection, f"create database {base_name};")
        sql_code += f'mysql -uroot -pyuri -D{base_name} < {pwdPath}/{directory}/{base_name}.sql\n'
    with open(f'load-{fileName}.{'sh' if platform.system() == 'Linux' else 'bat'}', 'w', encoding='utf-8') as file:
        file.write(sql_code)

extract_tar_gz()



