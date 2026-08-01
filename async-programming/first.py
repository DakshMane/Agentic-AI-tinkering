
import asyncio
import time 

# def fetchWeather () :
#     print("Fetching weather")
#     time.sleep(4) 
#     print("Fetched weather details ")

# def fetchNews() :
#     print("Fetching news")
#     time.sleep(4)
#     print("Fetched news")

# def main () :
#     time_start = time.time() 

#     fetchWeather()
#     fetchNews()

#     time_end = time.time()

#     print(f"Time took : {time_end - time_start} seconds " )


# main()


async def fetchWeatherAsync() :
    print("Fetching weather")
    await asyncio.sleep(4) 
    print("Fetched weather details ")

async def fetchNewsAsync ()  :
    print("Fetching news")
    await asyncio.sleep(4)
    print("Fetched news")


async def mainFunc() :
    time_Start = time.time()
    await asyncio.gather(
        fetchWeatherAsync(),
        fetchNewsAsync()
    )
    time_end = time.time()
    print(f"Time taken : {time_end - time_Start}")


asyncio.run(mainFunc())