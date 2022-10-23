from yarl import URL

from cyberdrop_dl.base_functions.base_functions import log, logger
from ..client.client import Session


class DirectCrawler:
    async def fetch(self, session: Session, url: URL):
        try:
            for ext in [".jpg", ".png", ".gif"]:
                if url.path.endswith(ext):
                    return url

        except Exception as e:
            logger.debug("Error encountered while handling %s", str(url), exc_info=True)
            await log("Error scraping " + str(url))
            logger.debug(e)
