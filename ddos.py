import time
import asyncio
import aiohttp
import argparse
import json
import random
# Step 1: Make a single non-blocking HTTP request
async def request(url,method='GET',payload=None, headers=None):
    star = time.time()
    async with aiohttp.ClientSession() as session:
        try:
            kwargs = {'headers': headers} if headers else {}
            if method =='POST' and payload:
                kwargs['json'] = payload
            async with session.request(method, url, **kwargs) as resp:
                return {"stat":resp.status, 'success':resp.status < 400, 'time':time.time()-star}

        except Exception as e:
            return 


async def main():
    url = "https://xuandi.org"
    res = await request(url)
    # print( )
    print(res)
    #a
# p

if __name__ == "__main__":
    asyncio.run(main())