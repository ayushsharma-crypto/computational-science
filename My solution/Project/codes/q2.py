import numpy as np
from configuration import Configuration


if __name__=="__main__":
    config_instance = Configuration()
    new_config = np.array(config_instance.read_config())
    config_instance.assign_configuration(new_config)
    potential = config_instance.calculate_potential()
    print("Lenard Jones Potential of the configuration = ",potential)