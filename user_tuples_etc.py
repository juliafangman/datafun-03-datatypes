"""
Modify this docstring.

"""

#tuples
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

def tuple_illustrated():
#Double faults by Roger Federer from 2001-2006
    tuple_1 = (203, 194, 269, 156, 152, 118)
#matches played by Roger Federer from 2001-2006
    tuple_2 = (70, 80, 95, 80, 85, 97)

    logger.info(f"tuple_1 = {tuple_1}")
    logger.info(f"tuple_2 = {tuple_2}")

    double_faults_per_match = tuple(a / b for a, b in zip(tuple_2, tuple_1))
    print(double_faults_per_match)

    logger.info(f"{tuple_1 = }")
    logger.info(f"{tuple_2 = }")
    logger.info(f"{double_faults_per_match = }")

#sets
def illustrate_sets():
    set_A = {"A", "C", "G", "W", "R", "P", "V"}
    set_B = {"B", "F", "C", "P", "O", "G", "Y"}

#union of sets A and B
    union_set = set_A | set_B
    print(union_set)

#intersection of sets A and B
    intersection_set = set_A & set_B
    print(intersection_set)

def illustrate_dict():
#Dictionary
    TennisPlayerA_dict = {'name': 'Djokovic', 'age': 36, 'weight_lbs': 170}
    TennisPlayerB_dict = {'name': 'Nadal', 'age': 37, 'weight_lbs': 187}

    logger.info(f"TennisPlayerA_dict = {TennisPlayerA_dict}")
    logger.info(f"TennisPlayerB_dict = {TennisPlayerB_dict}")

    with open ("text_names_in.txt") as file_object:
        word_list = file_object.read().split()

    word_count_dict = {word: word_list.count(word) for word in word_list}

    logger.info(f"Given text_names_in.txt, the word_count_dict = {word_count_dict}")

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    tuple_illustrated()

    def tuple_illustrated():
        logger.info("Illustrating Tuples")

    illustrate_sets()
    
    def illustrate_sets():
        logger.info("Illustrating Sets")

    illustrate_dict()

    def illustrate_dict():
        logger.info("Illustrating Dictionaries")
    

