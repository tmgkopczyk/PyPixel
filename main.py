import utilities
import json
skyblock_profiles = utilities.get_skyblock_profiles("PickaxeTubeHD")
with open("skyblock_player_data.json","w") as file:
  json.dump(skyblock_profiles,file)