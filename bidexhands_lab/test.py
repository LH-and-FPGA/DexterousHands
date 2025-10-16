#launch Isaac Sim before any other imports
#default first two lines in any standalone application
from isaacsim import SimulationApp # type: ignore
simulation_app = SimulationApp({"headless": False}) # we can also run as headless.
print("Isaac Sim launched")

from isaacsim.core.api import World # type: ignore
world = World()
task = TODO
world.add_task(task) # 在此处不会执行任何除了注册task以外的操作
world.scene.add_default_ground_plane()

world.reset()