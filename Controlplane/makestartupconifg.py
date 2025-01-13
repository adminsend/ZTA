
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:30:05 2025

@author: Andreas Huemmer [andreas.huemmer@adminsend.de]

Version: 0.0

Changelist: 
    
ToDoList:

"""

import configparser
import os

def create_config_file(file_path):
    """
    Creates a config file with default values.
    """
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'ControlplaneID': '0',
        'DebugLevel': '0',
        #'nonsens': 'None',
        #'blubb': 'None'
    }

    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"\nConfig file created at: {file_path}")

def read_config_file(file_path):
    """
    Reads and prints the content of the config file.
    """
    if not os.path.exists(file_path):
        print(f"Config file does not exist: {file_path}")
        return None

    config = configparser.ConfigParser()
    config.read(file_path)

    print("\nReading configuration:")
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config[section].items():
            print(f"{key} = {value}")

    if 'DEFAULT' in config:
        print("\n[DEFAULT]")
        for key, value in config['DEFAULT'].items():
            print(f"{key} = {value}")

    return config

def update_config_file(file_path, section, key, value):
    """
    Updates a specific value in the config file.
    """
    if not os.path.exists(file_path):
        print(f"Config file does not exist: {file_path}")
        return

    config = configparser.ConfigParser()
    config.read(file_path)

    if section not in config:
        config[section] = {}

    config[section][key] = value

    with open(file_path, 'w') as configfile:
        config.write(configfile)
    print(f"\nUpdated {key} in section {section} to {value}")

def main():
    file_path = "config.zta"

    # Create the config file if it doesn't exist
    if not os.path.exists(file_path):
        create_config_file(file_path)

    # Read the config file
    config = read_config_file(file_path)

    # Update the config file
    update_config_file(file_path, 'DEFAULT', 'ControlplaneID', '1')
    update_config_file(file_path, 'DEFAULT', 'DebugLevel', '1')
    #update_config_file(file_path, 'DEFAULT', 'nonsens', 'UpdatedValue')
    #update_config_file(file_path, 'DEFAULT', 'blubb', 'UpdatedBlubb')

    # Read the updated config file
    read_config_file(file_path)

if __name__ == "__main__":
    main()
