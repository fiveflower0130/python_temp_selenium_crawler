import sys, os

# current_dir = os.path.dirname(os.path.realpath(__file__))
# parent_dir = os.path.dirname(current_dir)
# print('current_dir: ',current_dir)
# print('parent_dir: ', parent_dir)

# args: list = [parent_dir]
# for _ in range(1):
#     args.append('..')   
# rel_path = os.path.join(*args)
# print('rel_path: ',rel_path)
# sys.path.append(rel_path)

# import lib_function
# set relative path
testdir = os.path.dirname(__file__)
srcdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from library.lib_function import Read_INI_File_Info

def config_test():
    config = Read_INI_File_Info()
    # config = lib_function.Read_INI_File_Info()
    browser_name = config.get('Driver', 'browser_driver')
    ase_id = config.get('LoginInfo', 'ase_id') #your ase id
    ase_password = config.get('LoginInfo', 'ase_password') # your ase password

    print(browser_name, ase_id, ase_password)
    print('this is config test')

if __name__ == "__main__":
    config_test()