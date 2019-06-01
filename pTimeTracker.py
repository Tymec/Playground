import psutil
import os
import pickle
import time
import ujson
import datetime
import argparse


parser = argparse.ArgumentParser(description='Process time tracker')
parser.add_argument('-p', '--print', help="Print a process time", dest="print", metavar="print")
args = vars(parser.parse_args())


class Tracker:
    @staticmethod
    def save_dict(dict_to_save, filename="pickle/pTimeTracker.p"):
        """Saves a dict"""
        with open(filename, 'wb') as f:
            pickle.dump(dict_to_save, f)

    @staticmethod
    def load_dict(filename="pickle/pTimeTracker.p"):
        """Loads a dict"""
        try:
            with open(filename, 'rb') as f:
                loaded_dict = pickle.load(f)
            return loaded_dict
        except FileNotFoundError:
            _processes = Tracker.get_all_processes()
            return _processes

    @staticmethod
    def get_all_processes():
        """Saves all running processes into a dict"""
        process_dict = {}
        for process in psutil.process_iter():
            process_name = os.path.splitext(process.name())[0]
            process_info = process.as_dict(attrs=['name', 'exe'])
            process_info['runtime'] = time.time() - process.create_time()
            process_info['datetime'] = str(datetime.timedelta(seconds=process_info['runtime']))
            process_dict[process_name] = process_info
        return process_dict

    @staticmethod
    def compare_processes(main_dict, process_dict):
        """Compares two dicts containing processes"""
        main_dict_keys = main_dict.keys()
        for process_name in [x for x in process_dict.keys()]:
            # if process is still running
            if process_name in main_dict_keys:
                main_dict[process_name]['runtime'] += process_dict[process_name]['runtime']
            # if a new process has been started
            elif process_name not in main_dict_keys:
                main_dict[process_name] = process_dict[process_name]
        return main_dict
    
    @staticmethod
    def print_process_time(processes, process_name):
        if not processes.get(process_name):
            print(f"No process with the name {process_name} was not found.")
            return
        print(f"This process has a tracked time of {processes[process_name]['runtime'] / 60:.2} hours.")

if __name__ == "__main__":
    processes = Tracker.load_dict()
    
    if args['print']:
        Tracker.print_process_time(processes, args['print'])
    else:
        try:
            while True:
                time.sleep(5)
                start = time.time()
                _processes = Tracker.get_all_processes()
                print(f"Took {time.time() - start:.2}s")
                processes = Tracker.compare_processes(processes, _processes)
        except KeyboardInterrupt:
            Tracker.save_dict(processes)
            with open('pickle/processes.json', 'w') as f:
                ujson.dump(processes, f, indent=4)
