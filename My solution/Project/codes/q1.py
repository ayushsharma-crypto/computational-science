from configuration import Configuration

def initial_configuration():
    random_configuration = Configuration()
    random_configuration.create_random_configuration()
    f = open("outputs/init_conf.xyz", "w")
    f.write(f"{random_configuration.total_atoms}\n")
    for line in random_configuration.config:
        f.write(f"C {line[0]} {line[1]} {line[2]}\n")
    f.close()
    return random_configuration


if __name__=="__main__":
    print("Generating A Random Initial Configuration...")
    random_conf = initial_configuration()
    # print("Checking corrctness...")
    # random_conf.check_pbc()
    print("Conf. generated and saved at location ./outputs/init_conf.xyz")