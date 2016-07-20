import logging


def setup_logging(level=logging.DEBUG):  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger('boto3').setLevel(logging.CRITICAL)
    logging.getLogger('botocore').setLevel(logging.CRITICAL)
    logging.getLogger('dbus.proxies').setLevel(logging.CRITICAL)
    spacel_logger = logging.getLogger('spacel')
    spacel_logger.setLevel(level)
    return spacel_logger
