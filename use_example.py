from reader_manometer import get_angles_volum, get_crops_names
import asyncio

async def example_vol():
    angles, volum = await get_angles_volum('./crops/image4_0.jpg')
    print("valor final:", volum)

async def example_crop():
    names = await get_crops_names('image4.jpg', 0)
    print('nomes', names)

if __name__ == '__main__':
    asyncio.run(example_crop())
    asyncio.run(example_vol())