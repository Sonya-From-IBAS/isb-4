import sys
import json
import logging
import csv
import matplotlib.pyplot as plt

logging.getLogger().setLevel(logging.INFO)


class Stat:

    def  __init__(self, json_file:str)->None:
        """
        Constructor

        Args:
            json_file (str): settings file
        """
        self.__cores_to_time = {}
        try:
            with open(json_file, "r") as file:
                settings =  json.load(file)
            self.__cores_time_path = settings["coresTime"]
            self.__pyplot_bar_path = settings["pyplotBar"]
        except OSError as error:
            logging.warning("coresTime and pyplotBar file are not loaded")
            sys.exit(error)
    
    @property
    def stat_dict(self)->dict:
        """
        Getter

        Returns:
            dict: dict of cores-time
        """
        return self.__cores_to_time
    
    def time_serialization(self, cores:int, time:float)->None:
        """
        Func that saves the number of cores and their running time
        Args:
            cores (int): number of cores
            time (float): time
            json_file (str): settings file
        """
        try:
            with open(self.__cores_time_path, "a") as file:
                writer = csv.writer(file, delimiter=",", lineterminator="\n")
                writer.writerow([cores, time])
            logging.info("time info is written")
        except OSError as error:
            logging.warning("time info is not written")
            sys.exit(error)

    def time_deserialization(self)->None:
        """
        Func that loads the number of cores and their running time

        """
        try:
            with open(self.__cores_time_path, "r") as file:
                lines = file.readlines()
        except OSError as error:
            logging.warning("time info is not loaded")
            sys.exit(error)
        for line in lines:
            line = list(map(float, line.split(",")))
            self.__cores_to_time[line[0]]=line[1]
        logging.info("time info is loaded")
        

    def save_fig(self)->None:
        """
        Func saves bar to files
        """ 
        self.time_deserialization()
        plt.ylabel("time, sec")
        plt.xlabel("cores")
        plt.title("Statistic")
        cores, time = self.__cores_to_time.keys(), self.__cores_to_time.values()
        plt.bar(cores, time, color="blue", width=0.25)
        try:
            plt.savefig(self.__pyplot_bar_path)
            logging.info("bar is saved")
        except OSError as error:
            logging.warning("bar is not saved")
            sys.exit(error)