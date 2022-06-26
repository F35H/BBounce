import sys

sys.path.append("scripts")
sys.path.append("models")
sys.path.append("textures")

from hub import GInit

if __name__ == "__main__":
  __game = GInit()
  base.run()