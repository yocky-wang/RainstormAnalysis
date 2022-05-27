import pandas as pd
import os
import matplotlib.pyplot as plt
import json

def raintime(df):
    month_list = [0]*12
    year_list = [0] * 13  # 2010-2022
    time_set = set()
    print(len(df['暴雨内涝开始时间']))
    try:
        for item in df['暴雨内涝开始时间']:
            item = item.translate(str.maketrans({'-': '/', '.': '/'}))
            time_set.add(item.split(' ')[0])
        for time_set_item in time_set:
            if '/' in time_set_item:
                # print(time_set_item)
                month = int(time_set_item.split('/')[1])
                month_list[month - 1] += 1
                year = int(time_set_item.split('/')[0])
                year_list[year - 2010] += 1
    except Exception as e:
        print('error:', e)
    return month_list, year_list
def rainfenxi(dfs):
    json1 = {"data": []}
    city_month_list = []
    city_year_list = []
    city_count_dic = {}
    dfyear = [0] * 13  # 2010-2022
    for cities in [cities1, cities2, cities3]:
        dfmonth = [0] * 12
        year = [0] * 13
        for city in cities:
            print(city)
            df_item = dfs[dfs['所在城市'] == city]
            df_item_month, df_item_year = raintime(df_item)
            dic = {"cityName": city, "month": df_item_month, "year": df_item_year, "count": sum(df_item_month)}
            json1['data'].append(dic)
            print(df_item_month)
            print(df_item_year)
            for i in range(0, 12):
                dfmonth[i] += df_item_month[i]
            for i in range(0,13):
                dfyear[i] += df_item_year[i]
                year[i] += df_item_year[i]
            city_count_dic[city] = sum(df_item_month)
        # print(dfmonth)

        city_month_list.append(dfmonth)
        city_year_list.append(year)
    json_dict_2 = json.dumps(json1, ensure_ascii=False)
    print(json_dict_2)
    return city_month_list, city_count_dic, dfyear, city_year_list
def draw_renwu1(citiesname, month_list):
    month_label = [str(i) + '月' for i in range(1, 13)]
    x = month_label
    y = month_list
    plt.bar(x, y)
    for a, b, i in zip(x, y, range(len(x))):  # zip 函数
        plt.text(a, b + 0.01, "%.2f" % y[i], ha='center', fontsize=12)  # plt.text 函数
    plt.ylabel('次数')
    plt.title(citiesname+"--下雨统计")
    plt.show()
def draw_renwu2(race_list):
    month_label = [str(i) + '月' for i in range(1, 13)]
    x = month_label
    y = [float(i.split('%')[0]) for i in race_list]
    plt.bar(x, y)
    for a, b, i in zip(x, y, range(len(x))):  # zip 函数
        plt.text(a, b + 0.01, "%.2f" % y[i], ha='center', fontsize=12)  # plt.text 函数
    plt.ylabel('次数')
    plt.title("暴雨内涝次数比例")
    plt.show()
def draw_renwu4(list):
    x = [i for i, j in list]
    y = [j for i, j in list]
    plt.barh(x, y)
    plt.title("各个城市暴雨统计")
    plt.show()
def draw_renwu5(year_list):
    x = [2010 + i for i in range(0, 13)]
    y = year_list
    plt.plot(x, y)
    for a, b, i in zip(x, y, range(len(x))):  # zip 函数
        plt.text(a, b + 0.01, y[i], ha='center', fontsize=12)  # plt.text 函数
    plt.title('2010年--2022年')
    plt.show()
def draw_renwu6(list):
    x = [i for i, j in list]
    y = [j for i, j in list]
    plt.barh(x, y)
    plt.title("暴雨影响统计")
    plt.show()

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    cities1 = ['北京', '天津', '石家庄', '唐山']
    cities2 = ['广州', '深圳', '东莞', '香港', '佛山', '珠海']
    cities3 = ['合肥', '南京', '宁波', '上海', '苏州', '温州', '舟山', '安庆']
    citiesall = cities1+cities2+cities3
    cities_name = ['京津冀城市群', '粤港澳城市群', '长三角城市群']
    src_path = './数据分析所用的excel'
    dirs = os.listdir(src_path)
    dflist = []
    for dirr in dirs:
        excel_path = src_path+'/'+dirr
        df = pd.read_excel(excel_path)
        dflist.append(df)
    dfs = pd.concat([i for i in dflist])
    dfs['暴雨内涝开始时间'] = dfs['暴雨内涝开始时间'].astype(str)
    renwu1_month, renwu4_city, renwu5_year, year = rainfenxi(dfs)
    # 任务1
    print('任务1：')
    for i in range(0,3):
        print(cities_name[i], '：', renwu1_month[i])
        print(cities_name[i], '：', year[i])
        draw_renwu1(cities_name[i], renwu1_month[i])
    # 任务2
    renwu2_list = [0]*12
    for i in range(0,12):
        renwu2_list[i] = renwu1_month[0][i]+renwu1_month[1][i]+renwu1_month[2][i]
    month_sum = sum(renwu2_list)
    month_race = [str(round(item * 100 / month_sum, 2)) + '%' for item in renwu2_list]
    print('任务2：')
    print(renwu2_list)
    print(month_race)
    draw_renwu2(month_race)
    # 任务4
    print('任务4：')
    renwu4_sort = sorted(renwu4_city.items(), key=lambda d: d[1], reverse=True)
    print(renwu4_sort)
    draw_renwu4(renwu4_sort)
    # 任务5
    print('任务5：')
    print(renwu5_year)
    draw_renwu5(renwu5_year)
    # print(month_sum) #210
    # print(sum(renwu5_year)) #210
    # 6  10-26 col
    print('任务6：')
    col_name = [column for column in dfs]
    col_dic = {}
    for i in range(10, 27):
        col_dic[col_name[i]] = int(dfs.iloc[:, [i]].notnull().sum())
    col_sort = sorted(col_dic.items(), key=lambda d: d[1], reverse=True)
    print(col_sort)
    draw_renwu6(col_sort)