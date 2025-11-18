'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2025-10-29 15:30:35
LastEditTime: 2025-10-30 11:42:31
Description: 结合理论值的角度数据补全工具
'''
import sqlite3
import pandas as pd
import numpy as np
import os
from scipy.interpolate import interp1d

# ==================== 配置 ====================
DB_PATH = 'angle.db'              # 采集数据数据库
THEORY_DB_PATH = 'angle-theory.db'# 理论数据数据库（如果在同一个DB中）
TABLE_NAME = 'CalibrationAngle'   # 采集数据表名
THEORY_TABLE_NAME = 'Lens2Data'   # 理论数据表名
OUTPUT_DB = 'angle_out.db'        # 输出数据库

# ==================== 数据读取 ====================


def read_from_sqlite(db_path, table_name, columns=None):
  """从SQLite数据库读取数据"""
  try:
    conn = sqlite3.connect(db_path)
    if columns:
      cols_str = ', '.join([f'"{col}"' for col in columns])
      query = f'SELECT {cols_str} FROM "{table_name}"'
    else:
      query = f'SELECT * FROM "{table_name}"'
    df = pd.read_sql_query(query, conn)
    conn.close()
    print(f"成功读取 {table_name}: {len(df)} 行数据")
    return df
  except Exception as e:
    print(f"读取 {table_name} 失败: {e}")
    return None

# ==================== 数据补全策略 ====================


def calculate_offset_model(df_measured, df_theory):
  """
  计算测量值与理论值之间的偏移模型
  返回: 偏移量DataFrame (Uacc, WD, offset)
  """
  # 合并测量值和理论值
  merged = pd.merge(
    df_measured,
    df_theory,
    on=['Uacc', 'WD'],
    suffixes=('_measured', '_theory')
  )

  if merged.empty:
    print("警告: 测量数据与理论数据没有交集!")
    return None

  # 计算偏移量 (测量值 - 理论值)
  merged['offset'] = merged['Angle_measured'] - merged['Angle_theory']

  print(f"\n偏移量统计 (基于 {len(merged)} 个测量点):")
  print(f"  平均偏移: {merged['offset'].mean():.2f}°")
  print(f"  偏移标准差: {merged['offset'].std():.2f}°")
  print(f"  偏移范围: [{merged['offset'].min():.2f}°, {merged['offset'].max():.2f}°]")

  return merged[['Uacc', 'WD', 'offset']]


def interpolate_offset(offset_df, target_uacc, target_wd):
  """
  对给定的(Uacc, WD)点插值偏移量
  策略: 先按WD插值，再按Uacc插值
  """
  if offset_df is None or offset_df.empty:
    return 0.0

  # 策略1: 找到该WD下的所有偏移量，按Uacc插值
  wd_data = offset_df[offset_df['WD'] == target_wd]
  if len(wd_data) >= 2:
    try:
      f = interp1d(wd_data['Uacc'].values, wd_data['offset'].values, kind='linear', fill_value='extrapolate', bounds_error=False)
      return float(f(target_uacc))
    except:
      pass

  # 策略2: 找到该Uacc下的所有偏移量，按WD插值
  uacc_data = offset_df[offset_df['Uacc'] == target_uacc]
  if len(uacc_data) >= 2:
    try:
      f = interp1d(uacc_data['WD'].values, uacc_data['offset'].values, kind='linear', fill_value='extrapolate', bounds_error=False)
      return float(f(target_wd))
    except:
      pass

  # 策略3: 找最近的点
  if not offset_df.empty:
    offset_df['dist'] = np.sqrt(
      (offset_df['Uacc'] - target_uacc)**2 +
      (offset_df['WD'] - target_wd)**2
    )
    nearest = offset_df.loc[offset_df['dist'].idxmin()]
    return float(nearest['offset'])

  # 策略4: 使用平均偏移量
  return float(offset_df['offset'].mean())


def complete_missing_data_with_theory(df_measured, df_theory):
  """
  结合理论值补全缺失数据
  补全策略:
  1. 保留所有测量值
  2. 对于缺失的点，使用: 理论值 + 插值偏移量
  """
  print("\n原始测量数据范围:")
  print(f"  Uacc: {df_measured['Uacc'].min():.0f} - {df_measured['Uacc'].max():.0f}")
  print(f"  WD: {df_measured['WD'].min():.0f} - {df_measured['WD'].max():.0f}")
  print(f"  Angle: {df_measured['Angle'].min():.1f}° - {df_measured['Angle'].max():.1f}°")

  # 计算偏移模型
  offset_df = calculate_offset_model(df_measured, df_theory)

  # 目标范围 (根据理论数据范围)
  target_uacc = sorted(df_theory['Uacc'].unique())
  target_wd = sorted(df_theory['WD'].unique())

  print(f"\n目标补全范围:")
  print(f"  Uacc: {min(target_uacc):.0f} - {max(target_uacc):.0f} ({len(target_uacc)} 个值)")
  print(f"  WD: {min(target_wd):.0f} - {max(target_wd):.0f} ({len(target_wd)} 个值)")

  completed_rows = []
  补全计数 = 0

  # 创建测量数据的查找字典
  measured_dict = {}
  for _, row in df_measured.iterrows():
    key = (float(row['Uacc']), float(row['WD']))
    measured_dict[key] = float(row['Angle'])

  # 创建理论数据的查找字典
  theory_dict = {}
  for _, row in df_theory.iterrows():
    key = (float(row['Uacc']), float(row['WD']))
    theory_dict[key] = float(row['Angle'])

  # 遍历所有目标点
  for uacc in target_uacc:
    for wd in target_wd:
      key = (float(uacc), float(wd))

      # 如果有测量值，直接使用
      if key in measured_dict:
        completed_rows.append({
          'Uacc': uacc,
          'WD': wd,
          'Angle': measured_dict[key],
          'Source': 'Measured'
        })
      # 如果没有测量值但有理论值，使用理论值+偏移量
      elif key in theory_dict:
        theory_angle = theory_dict[key]
        offset = interpolate_offset(offset_df, uacc, wd)
        补全_angle = theory_angle + offset
        补全_angle = np.clip(补全_angle, 0, 180)

        completed_rows.append({
          'Uacc': uacc,
          'WD': wd,
          'Angle': round(float(补全_angle), 1),
          'Source': 'Theory+Offset'
        })
        补全计数 += 1
      else:
        print(f"警告: ({uacc}, {wd}) 在理论数据中也不存在")

  print(f"\n补全了 {补全计数} 个数据点")

  completed_df = pd.DataFrame(completed_rows)
  completed_df = completed_df.sort_values(['WD', 'Uacc']).reset_index(drop=True)

  return completed_df

# ==================== 数据保存 ====================


def save_to_sqlite(df, output_db, table_name='completed_data'):
  """保存补全后的数据到SQLite"""
  try:
    conn = sqlite3.connect(output_db)
    # 只保存需要的列
    df_save = df[['Uacc', 'WD', 'Angle']].copy()
    df_save.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"\n✓ 数据已保存到 {output_db} (表: {table_name})")
    return True
  except Exception as e:
    print(f"保存失败: {e}")
    return False


def save_to_csv(df, output_file='completed_data.csv'):
  """保存为CSV文件"""
  try:
    df.to_csv(output_file, index=False)
    print(f"✓ 数据已导出为 {output_file}")
    return True
  except Exception as e:
    print(f"导出CSV失败: {e}")
    return False


def save_to_excel(df, output_file='completed_data.xlsx'):
  """保存为Excel文件（含透视表）"""
  try:
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
      # 原始数据（含来源标记）
      df.to_excel(writer, sheet_name='完整数据', index=False)

      # 透视表 - Angle值
      pivot_angle = df.pivot_table(values='Angle', index='Uacc', columns='WD')
      pivot_angle.to_excel(writer, sheet_name='角度透视表')

      # 透视表 - 数据来源
      if 'Source' in df.columns:
        pivot_source = df.pivot_table(
            values='Source', index='Uacc', columns='WD', aggfunc='first')
        pivot_source.to_excel(writer, sheet_name='数据来源')

    print(f"✓ Excel文件已生成: {output_file}")
    return True
  except ImportError:
    print("⚠ 未安装openpyxl，跳过Excel导出")
    return False
  except Exception as e:
    print(f"导出Excel失败: {e}")
    return False

# ==================== 数据统计 ====================


def print_statistics(df_measured, df_completed):
  """打印数据统计信息"""
  print("\n" + "="*60)
  print("数据统计信息")
  print("="*60)
  print(f"测量数据行数: {len(df_measured)}")
  print(f"补全后数据行数: {len(df_completed)}")
  print(f"新增行数: {len(df_completed) - len(df_measured)}")

  if 'Source' in df_completed.columns:
    print("\n数据来源分布:")
    source_counts = df_completed['Source'].value_counts()
    for source, count in source_counts.items():
      print(f"  {source}: {count} ({count/len(df_completed)*100:.1f}%)")

  print("\n角度值范围:")
  print(f"  最小值: {df_completed['Angle'].min():.1f}°")
  print(f"  最大值: {df_completed['Angle'].max():.1f}°")
  print(f"  平均值: {df_completed['Angle'].mean():.1f}°")
  print(f"  中位数: {df_completed['Angle'].median():.1f}°")

  print("\n数据完整性检查:")
  uacc_count = df_completed['Uacc'].nunique()
  wd_count = df_completed['WD'].nunique()
  expected_total = uacc_count * wd_count
  print(f"  Uacc数量: {uacc_count}")
  print(f"  WD数量: {wd_count}")
  print(f"  预期总行数: {expected_total}")
  print(f"  实际总行数: {len(df_completed)}")
  print(f"  完整性: {len(df_completed)/expected_total*100:.1f}%")

# ==================== 主程序 ====================


def main():
  print("结合理论值的角度数据补全工具")
  print("="*60)

  # 检查数据库文件
  if not os.path.exists(DB_PATH):
    print(f"错误: 数据库文件 {DB_PATH} 不存在")
    return

  # 读取测量数据
  df_measured = read_from_sqlite(DB_PATH, TABLE_NAME, ['Uacc', 'WD', 'Angle'])
  if df_measured is None or df_measured.empty:
    print("无法读取测量数据，程序退出")
    return

  # 读取理论数据
  df_theory = read_from_sqlite(THEORY_DB_PATH, THEORY_TABLE_NAME, ['Uacc', 'WD', 'Angle'])
  if df_theory is None or df_theory.empty:
    print("无法读取理论数据，程序退出")
    return

  # 补全数据
  print("\n" + "="*60)
  print("开始补全数据...")
  print("="*60)
  df_completed = complete_missing_data_with_theory(df_measured, df_theory)

  # 打印统计信息
  print_statistics(df_measured, df_completed)

  # 保存数据
  print("\n" + "="*60)
  print("保存数据...")
  print("="*60)

  save_to_sqlite(df_completed, OUTPUT_DB)
  save_to_csv(df_completed)
  save_to_excel(df_completed)

  # 显示补全后的数据示例
  print("\n补全后的数据预览 (前3个WD和后2个WD):")
  unique_wd = sorted(df_completed['WD'].unique())
  for wd in unique_wd[:3]:
    print(f"\nWD={wd}:")
    subset = df_completed[df_completed['WD']
                          == wd][['Uacc', 'Angle', 'Source']]
    print(subset.to_string(index=False))

  print("\n...")
  for wd in unique_wd[-2:]:
    print(f"\nWD={wd}:")
    subset = df_completed[df_completed['WD']
                          == wd][['Uacc', 'Angle', 'Source']]
    print(subset.to_string(index=False))


if __name__ == '__main__':
  main()
