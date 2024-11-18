import asyncio
import time
from typing import Any

from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService


async def connect(thing: Any, service: Any) -> str:
    thing_id = await service.register_device(thing)
    return thing_id


async def main() -> None:
    # create an IOT service
    service = IOTService()

    # create and register a few devices
    # hue_light = HueLightDevice()
    # speaker = SmartSpeakerDevice()
    # toilet = SmartToiletDevice()
    devices = [HueLightDevice(), SmartSpeakerDevice(), SmartToiletDevice()]
    connections = await asyncio.gather(*[connect(device, service) for device in devices])
    print(connections)

    # hue_light_id = service.register_device(hue_light)
    # speaker_id = service.register_device(speaker)
    # toilet_id = service.register_device(toilet)

    # create a few programs
    # wake_up_program = [
    #     Message(hue_light_id, MessageType.SWITCH_ON),
    #     Message(speaker_id, MessageType.SWITCH_ON),
    #     Message(speaker_id, MessageType.PLAY_SONG, "Rick Astley - Never Gonna Give You Up"),
    # ]
    #
    # sleep_program = [
    #     Message(hue_light_id, MessageType.SWITCH_OFF),
    #     Message(speaker_id, MessageType.SWITCH_OFF),
    #     Message(toilet_id, MessageType.FLUSH),
    #     Message(toilet_id, MessageType.CLEAN),
    # ]
    #
    # # run the programs
    # service.run_program(wake_up_program)
    # service.run_program(sleep_program)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()

    print("Elapsed:", end - start)
