import configparser

class ConfigReader:
    @staticmethod
    def read_config(section, key):
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        return config.get(section, key)

# Example Usage
if __name__ == "__main__":
    print(ConfigReader.read_config("settings", "base_url"))
