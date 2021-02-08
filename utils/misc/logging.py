import logging

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    handlers=[
                            logging.FileHandler("debug.log"),
                            logging.StreamHandler()
                        ]
                    )
