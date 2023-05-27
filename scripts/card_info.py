import json
import logging
import sys

logging.getLogger().setLevel(logging.INFO)

class CardInfo:
    """
    Class that works with card data
    """
    def __init__(self, json_file:str)->None:
        """
        Constructor
        Args:
            json_file (str): file name of json settings file
        """
        self.__card_info = self.settings_deserialization(json_file)
        self.__last_numbers = self.__card_info["last_numbers"]
        self.__hash = self.__card_info["hash"]
        self.__bins = self.__card_info["bins"]

    def settings_deserialization(self, json_file)->dict:
        """
        Func that loads settings

        Args:
            json_file (_type_): file name of settings

        Returns:
            dict: values of settings
        """
        try:
            with open(json_file, "r") as file:
                settings = json.load(file)
        except OSError as error:
            logging.warning("Settings are not loaded")
            sys.exit(error)
        self.__path_to_card_number = settings["cardNumber"]
        card_info = {}
        try:
            path = settings["hash"]
            with open(path, "r") as file:
                card_info["hash"] = file.read()
        except OSError as error:
            logging.warning("Hash is not loaded")
            sys.exit(error)

        try:
            path = settings["bins"]
            with open(path, "r") as file:
                card_info["bins"] = tuple(map(int, file.readlines()))
        except OSError as error:
            logging.warning("Bins are not loaded")
            sys.exit(error)
        
        try:
            path = settings["lastNumbers"]
            with open(path, "r") as file:
                card_info["last_numbers"] = file.read()
        except OSError as error:
            logging.warning("Last numbers are not loaded")
            sys.exit(error)
        logging.info("Card's info is saved")
        return card_info

    

    @property
    def last_num(self)->str:
        """
        getter that return 4 last card's numbers 

        Returns:
            str: 4 last card's numbers
        """
        return self.__last_numbers

    @property
    def hash_card(self)->str:
        """
        getter that return card's hash 

        Returns:
            str: card's hash
        """
        return self.__hash

    @property
    def bins_card(self)->str:
        """
        getter that return card's bins 

        Returns:
            str: card's bins
        """
        return self.__bins
    

    def card_number_serealization(self, card_number:str)->None:
        """
        func that saves card number to file
        Args:
            file_name (str): card number file name
            card_number (str): card number

        """
        try:
            with open(self.__path_to_card_number, "w") as file:
                file.write(card_number)
            logging.info("Card number is written")
        except OSError as error:
            logging.warning("Card number is not written")
            sys.exit(error)

    def card_number_deserealization(self)->str:
        """
        func that loads card number from file
        Returns:
            str: card's number
        """
        try:
            with open(self.__path_to_card_number, "r") as file:
                number = file.read()
            logging.info("Card number is loaded")
            return number
        except OSError as error:
            logging.warning("Card number is not loaded")
            sys.exit(error)
