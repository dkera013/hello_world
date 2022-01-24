import os


SCRIPT_PATH = 'C:/Users/ikerasiotis/Documents/Python Scripts/Silk'
FILE_NAME = 'test.config'
SVN_REPORT_PATH = 'C:\work\Reports\\'


def set_config_bat(new_id, previous_id, PSF_version, provider):

    config_file = os.path.join(SCRIPT_PATH, FILE_NAME)
    print(config_file)
    with open(config_file, "r") as file:
        data = file.readlines()
        #update the svn report path
        data[1] = 'svn_report_path = ' + SVN_REPORT_PATH + '\n'
        #update the auto run option
        data[7] = 'run=yes \n'
        #update the psf version
        data[11] = 'psf_version= ' + PSF_version + '\n'
        #update the provider
        data[12] = 'provider = ' + provider + '\n'
        #update the map ids
        data[15] = previous_id + ', ' + new_id

    with open(config_file, "w") as file:
        file.writelines(data)


set_config_bat('9999', '8888', '70', 'TA')
