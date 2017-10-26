# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:54:44 2017
@author: ZhianLin
统计源代码的行数（含注释行）同时合并源代码到txt中，用来方便软件著作权申请用。
Python 3.4.3.4
"""
import os
import time

# filelists = []
#
def getFile(basedir,whitelist=['py'],openLib=[]):
    '''
     递归遍历文件夹，返回符合类型的文件清单
    
    :basedir:软件项目的根目录。
    :whitelist:文件类型的白名单。
    :openLib:需要排除的库文件，一般是去除掉开源公共库。
    '''

    filelists = []
    for parent,dirnames,filenames in os.walk(basedir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            #去掉开源公共库
            if  ext in whitelist and filename.split('\\')[-1] not in openLib:
                filelists.append(os.path.join(parent,filename))
    print('文件数量：',len(filelists))        
    return filelists
 
#
def countLine(fname,detail=0):
    '''
    统计一个文件的行数
    :fname:文件的全路径
    :detail:是否输出每个文件的行数，默认不输出，detail=1时输出。
    '''
    count = 0
    #    print('fname',fname)
    for file_line in open(fname,'r',encoding='utf-8'):
        if file_line != '' and file_line != '\n': #过滤掉空行
            count += 1
    if detail==1:
        print (fname + '----' , count)
    return count
#
def projectLinesCount(path,fileType,openLib):    
    startTime = time.clock()
    print('==========')
    folderName=path.split("/")[-1]
    filename=path+'/'+folderName+'.products.txt'
    r=open(filename,'wb')
    filelists=getFile(path,fileType,openLib)        
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
        t=open(filelist,'r',encoding='utf-8')
        for file_line in t:        
            if file_line!='' and file_line !='\n':
    #            print('line:',line)
                r.write(file_line.encode())
    #把统计结果追加到源代码文件末尾。
    r.write(('\n 当前正在进行的目录'+path).encode())
    r.write(('\n 项目：'+folderName+' 总行数是:'+str(totalline)).encode())
    r.write(('\n 源码合并后的文件名：'+filename).encode())
    r.write(('\n Done! Cost Time: %0.2f second' % (time.clock() - startTime)).encode())
    #命令行输出统计结果
    print('当前正在进行的目录',path)
    print('源码合并后的文件名：',filename,'\n')
    print ('项目：',folderName,' 总行数是:',totalline)
    print ('Project:',folderName,' TotalLines:',totalline)
    print ('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
    r.close()
        
if __name__ == '__main__' :
    '''
    统计源代码的行数（含注释行）同时合并源代码到根目录的txt中。
    '''
    #目录组，只有一个软件项目时只填写一个。
    folders=[r'D:/项目/NongTaiProject/19本地测试环境/新建文件夹/场内驻守V1.1/garrison-APP-v1.1']
    #要排除的公共库文件    
    openLib=('vue.js','vue.min.js','mui.js','mui.min.js','bootstrap.js','bootstrap.min.js',
    'browser.min.js','jquery.validate.min.js','jquery-1.12.3.min.js','vue-router.js','vue-router.min.js',
    'bootstrap.css','bootstrap.min.css','bootstrap-datetimepicker.min.css','mui.css','mui.min.css',
    'moment-with-locales.min.js','moment.min.js','moment.js','moment-timezone.min.js','moment-timezone-with-data.js','moment-timezone-with-data.min.js',
    'vue-components.css','vue-components.js')
    # 统计的文件类型
    fileType = ['html', 'css', 'js','py']
    for i in folders:
        projectLinesCount(i,fileType,openLib)