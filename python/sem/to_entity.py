'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2025-11-13 15:34:55
LastEditTime: 2025-11-17 15:08:52
Description: 
'''
import re


def sql_to_csharp_entity(sql_statement):
  """
  将SQL的CREATE TABLE语句转换为C#实体类
  """

  # 提取表名
  # 提取字段定义
  fields_section = re.search(r'\((.*)$$', sql_statement, re.DOTALL)
  table_match = re.search(r'CREATE TABLE\s+"(\w+)"', sql_statement)
  if not table_match:
    raise ValueError("无法解析表名")
  table_name = table_match.group(1)
  if not fields_section:
    raise ValueError("无法解析字段定义")

  field_lines = fields_section.group(1).strip().split(',')

  csharp_code = []

  # 添加命名空间和类声明
  csharp_code.append('using GrpcSqlite.Core.Attribute;\n')
  csharp_code.append('namespace GrpcSqlite.Entity.Eo;\n')
  csharp_code.append(
      f'[TableInfo(KnownDatabaseInfo.Eo, KnownTableInfo.{table_name})]')
  csharp_code.append(f'public class {table_name} {{')

  for line in field_lines:
    line = line.strip()
    if not line or 'PRIMARY KEY' in line or 'FOREIGN KEY' in line or 'UNIQUE' in line:
      continue

    # 匹配字段定义：列名 数据类型 [约束]
    field_match = re.match(
        r'"(\w+)"\s+([A-Z]+)(?:\s+(NOT NULL|NULL))?', line.strip())

    if field_match:
      column_name = field_match.group(1)
      data_type = field_match.group(2)
      is_nullable = field_match.group(3)

      # SQL数据类型到C#数据类型的映射
      type_mapping = {
          'INTEGER': 'int',
          'REAL': 'double',
          'TEXT': 'string',
          'BLOB': 'byte[]',
          'NUMERIC': 'decimal'
      }

      csharp_type = type_mapping.get(data_type.upper(), 'string')

      # 如果是可为空的类型且不是字符串，使用可空类型
      if is_nullable == 'NULL' and csharp_type not in ['string', 'byte[]']:
        csharp_type += '?'

      property_line = f'    public {csharp_type} {column_name} {{ get; set; }}'
      csharp_code.append(property_line)

  csharp_code.append('}')

  return '\n'.join(csharp_code)


def main():
  # 示例SQL语句
  sql_example = '''
CREATE TABLE "FisheyeAlign" (
	"GunAlignXLsv"	INTEGER,
	"GunAlignYLsv"	INTEGER,
	"ApAlignXLsv"	INTEGER,
	"ApAlignYLsv"	INTEGER,
	"Lens1Lsv"	INTEGER,
	"Lens2Lsv"	INTEGER,
	"StigX13Lsv"	INTEGER,
	"StigX2Lsv"	INTEGER,
	"StigX4Lsv"	INTEGER,
	"StigY13Lsv"	INTEGER,
	"StigY2Lsv"	INTEGER,
	"StigY4Lsv"	INTEGER,
	"ScanRLsv"	REAL,
	"ScanGain"	REAL,
	"Skew"	REAL,
	"Tilt"	REAL
);
    '''

  try:
    result = sql_to_csharp_entity(sql_example)
    print(result)

  except Exception as e:
    print(f"错误: {e}")


if __name__ == "__main__":
  main()
