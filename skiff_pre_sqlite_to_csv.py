#coding=utf-8

import sqlite3
import csv
import codecs

import sys

def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='a+', encoding='utf-8-sig') as f:
        taitou=(u'hostname', u'SSH免密', u'CPU核数', u'内存(M)', u'内核', u'Linux发行版', u'系统型号', u'VIP正常', u'默认路由', u'互联网连通性', u'性能测试结果', u'DNS', u'NTP')
        write = csv.writer(f, dialect='excel')
        conn = sqlite3.connect('/tmp/skiff_pre_tools.db')
        cur = conn.cursor()
        sql = 'select * from skiff_pre_table'
        results = cur.execute(sql)
        write.writerow(taitou)
        for result in results:
            print(result)
            write.writerow(result)
        conn.close()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    read_mysql_to_csv('/tmp/skiff_pre_tools.csv')
