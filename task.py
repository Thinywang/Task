# -*- coding:utf-8 -*-
# author:wangtingbo
import datetime
import time
import json
import os
import re
import signal
#读取json文件
def json_file():
    with open('task.json','r') as file:
        file_load=json.load(file)
        return file_load
run_time=json_file()['run_time']
kill_time=json_file()['kill_time']
run_process=json_file()['run_process']
run_process=re.split(",",run_process)
kill_process=json_file()['kill_process']
kill_process=re.split(",",kill_process)
#print(runtime,kill_process)
#定时任务
def timeFun(run_time,kill_time,run_process,kill_process):
    while True:
        time.sleep(1)
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now,run_time)
        k=str(run_time)
        t=str(kill_time)
        if now==k:
            taskkill(run_process)
            run_process = run_process + datetime.timedelta(days=1)
        elif now==t:
            taskkill(kill_process)
            kill_time = kill_time + datetime.timedelta(days=1)
        else:
            pass
#删除进程
def taskkill(kill_process):
    for i  in kill_process:
        os.system("taskkill /F /IM "+i)
        #os.kill(i, signal.SIGABRT)
def taskopen(run_process):
    for i in run_process:
        os.startfile(i)

if __name__=='__main__':
    timeFun(run_time,kill_time,run_process,kill_process)
    #taskkill(kill_process)
    #taskopen(run_process)