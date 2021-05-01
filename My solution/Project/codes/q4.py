import numpy as np
from configuration import Configuration

class Hessian:
    pass

if __name__=="__main__":
    config_instance = Configuration()
    new_config = np.array(config_instance.read_config("./outputs/final_conf.xyz"))
    config_instance.assign_configuration(new_config)
    config_instance.convert_to_bohr()
    hessian = Hessian(config_instance, 0.00001)