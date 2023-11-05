import logging

logging.basicConfig(level=logging.INFO, filename="testeLog.log", format="%(asctime)s - %(message)s" )

teste0 = 0
logging.info(f"Status da teste0 = {teste0}")

teste1 = 2
logging.info(f"Status da teste2 = {teste1}")

teste2 = 4
logging.info(f"Status da teste2 = {teste2}")

teste3 = 6
logging.info(f"Status da teste3 = {teste3}")