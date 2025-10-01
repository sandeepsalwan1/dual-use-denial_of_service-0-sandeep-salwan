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
            return {}

async def concurrentReq(url,count,method='GET',payload=None, headers=None):
    coros = [request(url,method,payload,headers) for i in range(count)]
    return await asyncio.gather(*coros)


async def main():
    url = "https://xuandi.org"
    res = await request(url)
    res = await concurrentReq(url,6)

    # print( )
    print(res)
    #a
# p

if __name__ == "__main__":
    asyncio.run(main())