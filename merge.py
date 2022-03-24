import pandas as pd
import glob

#只是合并文件
def marge(csv_list, outputfile):
    for inputfile in csv_list:
        f = open(inputfile, 'r', encoding="utf-8")
        data = pd.read_csv(f)
        data.to_csv(outputfile, mode='a', index=False)
    print('完成合并')

#去重保留一个表头
def distinct(file):
    df = pd.read_csv(file, header=None)
    datalist = df.drop_duplicates()
    datalist.to_csv('result_new.csv', index=False, header=False)
    print('完成去重')

if __name__ == '__main__':
    # path = "/home/T1/Twitter"
    # interesting_files = glob.glob(os.path.join(path, "*.csv"))
    
    csv_list = glob.glob('address\*.csv')
    output_csv_path = 'result.csv'
    print(csv_list)
    marge(csv_list, output_csv_path)
    distinct(output_csv_path)
