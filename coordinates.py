from subprocess import Popen, PIPE
from typing import NamedTuple

#from exeptions import GantGetCoordinates


class Coordinates(NamedTuple):
    longitude: float
    latitude: float

def get_coordinates() -> Coordinates:
    """
    Get the coordinates from the user.
    """

    process = Popen(["whereami"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        print("Error:", err)
    output_lines = output.decode().strip().lower().split("\n")
    latitude = longitude = None
    for line in output_lines:
        if line.startswith("latitude"):
            latitude = float(line.split(":")[1])
        if line.startswith("longitude"):
            longitude = float(line.split(":")[1])
    return Coordinates(longitude=longitude, latitude=latitude)

if __name__ == "__main__":
    print(get_coordinates())