import logging
logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt="%d / %b / %Y %H:%M:%S")
my_logger = logging.getLogger("amine")
my_logger.warning("this is warning message") 