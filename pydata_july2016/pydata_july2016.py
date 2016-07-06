import sys
import os
import logging.config
import yaml

logger = logging.getLogger(__name__)

def get_path(fname):
    """
        Get the path of a filename in the same
        directory as this script.
    """
    return os.path.join(os.path.dirname(__file__), fname)

def logmaker(**kwargs):
    """
        Create a custom log handler that is stored
        in a specifically created logs directory.
    """
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(path, 'logs')
    path = os.path.join(path, 'info.log')
    return logging.handlers.RotatingFileHandler(path, **kwargs)

def setup_logging(
        default_path = get_path('logging.yaml'),
        default_level = logging.INFO,
        env_key='LOG_CFG'
    ):
        """
        Setup logging configuration"
        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

def python_path():
    logger.info('Getting python path.')
    return '\n'.join(sys.path)

def system_path():
    logger.info('Getting system path.')
    return '\n'.join(os.environ['PATH'].split(':'))

def run():
    setup_logging()
    main()

def main():
    logger.info('Logging from main() function.')
    print('This is my Python path:\n\n')
    print(python_path())
    print('\n\nThis is my system path:\n\n')
    print(system_path())

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    main()
