import pandas as pd

# 测试Excel文件读取
def test_excel_reading():
    try:
        # 读取Excel文件
        df = pd.read_excel('Yamazumi Process Modeling Tool Templates.xls', sheet_name='Yamazumi Data', header=None)
        print("Excel文件读取成功！")
        print(f"数据形状: {df.shape}")
        
        # 查找数据开始行
        data_start_row = -1
        for i in range(len(df)):
            row = df.iloc[i].dropna()
            if len(row) > 0 and row.iloc[0] == 'Task' and row.iloc[1] == 'Work Type':
                data_start_row = i
                break
        
        if data_start_row == -1:
            print("错误: 找不到数据表开始行")
            return False
        
        print(f"数据开始行: {data_start_row}")
        
        # 获取工作站列表
        station_row = df.iloc[data_start_row].dropna()
        stations = station_row[2:].tolist()
        stations = [s for s in stations if s and s != '<fill in>']
        print(f"工作站列表: {stations}")
        
        # 处理数据行
        tasks = []
        for i in range(data_start_row + 1, len(df)):
            row = df.iloc[i].dropna()
            if len(row) < 3 or pd.isna(row.iloc[0]):
                continue
                
            task_name = row.iloc[0]
            work_type_desc = row.iloc[1]
            work_type = row.iloc[2]
            
            print(f"\n任务: {task_name}")
            print(f"工作类型描述: {work_type_desc}")
            print(f"工作类型: {work_type}")
            
            # 处理每个工作站的时间
            for j, station in enumerate(stations):
                if j + 2 < len(row):
                    time = row.iloc[j + 2]
                    # 确保time是数值类型
                    if pd.notna(time):
                        try:
                            time_val = float(time)
                            if time_val > 0:
                                print(f"  {station}: {time_val}秒")
                                tasks.append({
                                    'task_name': task_name,
                                    'work_type': work_type,
                                    'station': station,
                                    'time': time_val
                                })
                        except (ValueError, TypeError):
                            # 如果无法转换为数字，跳过
                            pass
        
        print(f"\n总共找到 {len(tasks)} 个任务")
        return True
        
    except Exception as e:
        print(f"错误: {e}")
        return False

# 测试CSV文件读取
def test_csv_reading():
    try:
        # 读取CSV示例文件
        df = pd.read_csv('Factory A_Process Section 1_data.csv')
        print("\nCSV文件读取成功！")
        print(f"数据形状: {df.shape}")
        print("列名:", df.columns.tolist())
        print("\n前5行数据:")
        print(df.head())
        return True
        
    except Exception as e:
        print(f"CSV读取错误: {e}")
        return False

if __name__ == "__main__":
    print("=== 测试Excel文件读取 ===")
    excel_success = test_excel_reading()
    
    print("\n=== 测试CSV文件读取 ===")
    csv_success = test_csv_reading()
    
    print(f"\n=== 测试结果 ===")
    print(f"Excel文件测试: {'成功' if excel_success else '失败'}")
    print(f"CSV文件测试: {'成功' if csv_success else '失败'}")
    
    if excel_success and csv_success:
        print("\n✅ 导入功能应该可以正常工作！")
    else:
        print("\n❌ 导入功能可能存在问题，请检查文件格式。")