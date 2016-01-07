def get_config(config_path):
    config = dict()

    for line in open(config_path, 'r').read().split('\n'):
        if '=' in line:
            key = line.split('=')[0]
            value = line.split('=')[1]
            config[key] = value
    return config
