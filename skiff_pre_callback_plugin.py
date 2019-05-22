'''
describe: ansible callback skiff_pre plugin
author: mamingxing
date: 2019.05.22
'''


import sqlite3
import json

from ansible.plugins.callback import CallbackBase

def skiff_pre_str_intercept(str_intercept):
    return str_intercept.split(":")[1]


class CallbackModule(CallbackBase):
    
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'skiff'
    CALLBACK_NAME = 'skiff_pre'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):

        super(CallbackModule, self).__init__()

    def skiff_conn(self):
        conn = sqlite3.connect('/tmp/skiff_pre_tools.db')
        return conn
     
    def skiff_pre_ssh_check_ok(self, host, mmx_dict):
        conn = self.skiff_conn()
        c = conn.cursor()
        c.execute('''create table if not  exists skiff_pre_table
             (skiff_pre_hostname  text, skiff_pre_ssh_check_ok test, skiff_pre_cpu text, skiff_pre_mem text, skiff_pre_kernel text, skiff_pre_linux_versoin text, skiff_pre_system_versoin text, skiff_pre_vip text, skiff_pre_default_route text, skiff_pre_internet text, skiff_pre_machine_performance text, skiff_pre_dns_ns text, skiff_pre_ntp_ping)''')
        
        t = (host,)
        c.execute('select * from skiff_pre_table where skiff_pre_hostname=?', t)
        if not c.fetchone():
            c.execute("insert into skiff_pre_table values ('%s', 'OK', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null')" % host)
            conn.commit()
        conn.close()
 
    def skiff_pre_cpu(self, host, mmx_dict):
        skiff_pre_cpu = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_cpu='%s' where skiff_pre_hostname='%s'" % (skiff_pre_cpu, host)
        c.execute(sql)
        conn.commit()
        conn.close()
    
    def skiff_pre_mem(self, host, mmx_dict):
        skiff_pre_mem = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_mem='%s' where skiff_pre_hostname='%s'" % (skiff_pre_mem, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_kernel(self, host, mmx_dict):
        skiff_pre_kernel = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_kernel='%s' where skiff_pre_hostname='%s'" % (skiff_pre_kernel, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_linux_versoin(self, host, mmx_dict):
        skiff_pre_linux_versoin = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_linux_versoin='%s' where skiff_pre_hostname='%s'" % (skiff_pre_linux_versoin, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_system_versoin(self, host, mmx_dict):
        skiff_pre_system_versoin = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_system_versoin='%s' where skiff_pre_hostname='%s'" % (skiff_pre_system_versoin, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_vip(self, host, mmx_dict):
        skiff_pre_vip = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_vip='%s' where skiff_pre_hostname='%s'" % (skiff_pre_vip, host)
        c.execute(sql)
        conn.commit()
        conn.close()
    
    def skiff_pre_default_route(self, host, mmx_dict):
        skiff_pre_default_route = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_default_route='%s' where skiff_pre_hostname='%s'" % (skiff_pre_default_route, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_internet(self, host, mmx_dict):
        skiff_pre_internet = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_internet='%s' where skiff_pre_hostname='%s'" % (skiff_pre_internet, host)
        c.execute(sql)
        conn.commit()
        conn.close()

    def skiff_pre_dns_ns(self, host, mmx_dict):
        skiff_pre_dns_ns = skiff_pre_str_intercept(mmx_dict.values()[0])
        conn = self.skiff_conn()
        c = conn.cursor()
        sql = "update skiff_pre_table set skiff_pre_dns_ns=\"%s\" where skiff_pre_hostname='%s'" % (skiff_pre_dns_ns, host)
        c.execute(sql)
        #print(sql)
        conn.commit()
        conn.close()
    

    def runner_on_ok(self, host, res):
        mmx_dict = json.loads(self._dump_results(res))
        
        if "ansible_facts" not in mmx_dict:
            #05_pre_check_ssh
            if mmx_dict.has_key('msg') and 'skiff_pre_ssh_check_ok' in mmx_dict.values():
                self.skiff_pre_ssh_check_ok(host, mmx_dict)         
            #10_pre_sysinfo skiff_pre_cpu
            if mmx_dict.has_key('msg') and 'skiff_pre_cpu' in mmx_dict.values()[0]:
                self.skiff_pre_cpu(host, mmx_dict)
            #10_pre_sysinfo skiff_pre_mem
            if mmx_dict.has_key('msg') and 'skiff_pre_mem' in mmx_dict.values()[0]:
                self.skiff_pre_mem(host, mmx_dict)
            #10_pre_sysinfo skiff_pre_kernel
            if mmx_dict.has_key('msg') and 'skiff_pre_kernel' in mmx_dict.values()[0]:
                self.skiff_pre_kernel(host, mmx_dict)
            #10_pre_sysinfo skiff_pre_linux_versoin
            if mmx_dict.has_key('msg') and 'skiff_pre_linux_versoin' in mmx_dict.values()[0]:
                self.skiff_pre_linux_versoin(host, mmx_dict)
            #10_pre_sysinfo skiff_pre_system_versoin
            if mmx_dict.has_key('msg') and 'skiff_pre_system_versoin' in mmx_dict.values()[0]:
                self.skiff_pre_system_versoin(host, mmx_dict)
            #15_pre_testvip skiff_pre_vip
            if mmx_dict.has_key('msg') and 'skiff_pre_vip' in mmx_dict.values()[0]:
                self.skiff_pre_vip(host, mmx_dict)
            #20_pre_default_route
            if mmx_dict.has_key('msg') and 'skiff_pre_default_route' in mmx_dict.values()[0]:
                self.skiff_pre_default_route(host, mmx_dict)            
            #25_pre_internet_test
            if mmx_dict.has_key('msg') and 'skiff_pre_internet' in mmx_dict.values()[0]:
                self.skiff_pre_internet(host, mmx_dict)
            #30_pre_dns_ns
            if mmx_dict.has_key('msg') and 'skiff_pre_dns_ns' in mmx_dict.values()[0]:
                self.skiff_pre_dns_ns(host, mmx_dict)
            #print ('ansible-command: task execution OK; host: %s; message: %s' % (host, mmx_dict))
        
    
