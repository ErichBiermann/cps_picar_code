from Pathfinder_class import Pathfinder
import picar_4wd as fc


pathfinder = Pathfinder()

def main():
    pathfinder.steer()


if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()