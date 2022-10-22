import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)
    logger.addHandler(console)
    
    return logger

logger = setup_logger()
