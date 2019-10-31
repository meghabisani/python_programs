import logging
import os

if os.path.exists('monitor.log'):
    os.remove('monitor.log')

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='monitor.log', level=logging.DEBUG)

test_case_files = (os.listdir(".\\Test_Cases"))
logging.info('List of input_file found with Test Cases:')

os.chdir("..\\source")
for input_file in test_case_files:
    logging.info(input_file)
    input_file_path = "..\\testing\\Test_Cases\\" + input_file
    print(input_file_path)
    logging.info('*********************************')
    with open(input_file_path, 'r') as fin:
        logging.info(fin.read())

    result = os.system("python toy_robot.py " + input_file_path)

    logging.info('*********************************')
    print('\n')
    logging.info('\n')

