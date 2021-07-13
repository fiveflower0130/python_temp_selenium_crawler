#coding=utf-8
import os
import configparser

# print(type(__name__), __name__) # 執行程式的名字
# print(type(__package__), __package__) # 屬於哪個 package

def Read_INI_File_Info():
    
    current_dir = os.path.dirname(os.path.realpath(__file__)) # 取得目前檔案位置
    working_directory_path = os.path.dirname(current_dir) # 取得root相對位置
    # working_directory_path1 = os.path.abspath(".") # 取得目前執行位置
    # print('working_directory_path1: ', working_directory_path1)
    # print('current_dir: ', current_dir)
    # print('working_directory_path: ', working_directory_path)
    ini_file_path = f'{working_directory_path}\crawler.ini'
    config = configparser.ConfigParser()
    config.read(ini_file_path)
    
    return config