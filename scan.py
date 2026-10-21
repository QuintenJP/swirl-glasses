"""Listen for Shining Glasses advertisements. Sends nothing to any device."""

import asyncio

from bleak import BleakScanner

COMPANY_ID = 0x5254       # manufacturer data "TR" ...
ADV_PREFIX = b"\x00\x41"  # ... followed by 00 41


async def main(seconds: float = 10.0) -> None:
    found = {}

    def on_advert(device, adv):
        data = adv.manufacturer_data.get(COMPANY_ID)
        if data is not None and data.startswith(ADV_PREFIX) and device.address not in found:
            found[device.address] = (device.name or adv.local_name, data.hex(" "))
            print(f"glasses: {device.name or adv.local_name!r}  id={device.address}  rssi={adv.rssi}  data={data.hex(' ')}")

    print(f"Scanning for {seconds:.0f} s...")
    async with BleakScanner(on_advert):
        await asyncio.sleep(seconds)
    if not found:
        print("No glasses found. Are they switched on, with the phone app closed?")


if __name__ == "__main__":
    asyncio.run(main())
