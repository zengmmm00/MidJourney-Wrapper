import Globals
import requests

def PassPromptToSelfBot(prompt: str):
    payload = {"type": 2, "application_id": "936929561302675456", "guild_id": Globals.SERVER_ID,
               "channel_id": Globals.CHANNEL_ID, "session_id": "8e6f2dceeb2852c6cd444d7a00ab6357",
               "data": {"version": "1118961510123847772", "id": "938956540159881230", "name": "imagine", "type": 1,
                        "options": [{"type": 3, "name": "prompt", "value": prompt}],
                        "application_command": {"id": "938956540159881230", "application_id": "936929561302675456",
                                                "version": "1118961510123847772", "default_member_permissions": None,
                                                "type": 1, "nsfw": False, "name": "imagine",
                                                "description": "Create images with Midjourney", "dm_permission": True,
                                                "contexts": [0, 1, 2], "options": [
                                {"type": 3, "name": "prompt", "description": "The prompt to imagine",
                                 "required": True}]}, "attachments": []}}

    header = {
        'authorization' : Globals.SALAI_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
    json = payload, headers = header)
    return response

def Upscale(index : int, messageId : str, messageHash : str):
    payload = {"type":3,
    "guild_id":Globals.SERVER_ID,
    "channel_id":Globals.CHANNEL_ID,
    "message_flags":0,
    "message_id": messageId,
    "application_id":"936929561302675456",
    "session_id":"45bc04dd4da37141a5f73dfbfaf5bdcf",
    "data":{"component_type":2,
            "custom_id":"MJ::JOB::upsample::{}::{}".format(index, messageHash)}
        }  
    header = {
        'authorization' : Globals.SALAI_TOKEN
    }
    response = requests.post("https://discord.com/api/v9/interactions",
    json = payload, headers = header)
    return response




def MaxUpscale(messageId : str, messageHash : str):
  payload = {"type":3,
          "guild_id":Globals.SERVER_ID,
          "channel_id":Globals.CHANNEL_ID,
             "message_flags":0,
             "message_id": messageId,
             "application_id":"936929561302675456",
             "session_id":"1f3dbdf09efdf93d81a3a6420882c92c","data": 
       {"component_type":2,"custom_id":"MJ::JOB::upsample_max::1::{}::SOLO".format(messageHash)}}
  header = {
        'authorization' : Globals.SALAI_TOKEN
    }
  response = requests.post("https://discord.com/api/v9/interactions",
  json = payload, headers = header)
  return response


def Variation(index : int,messageId : str, messageHash : str):
  payload = {"type":3, "guild_id":Globals.SERVER_ID,
            "channel_id": Globals.CHANNEL_ID,
            "message_flags":0,
            "message_id": messageId,
            "application_id": "936929561302675456",
            "session_id":"1f3dbdf09efdf93d81a3a6420882c92c",
            "data":{"component_type":2,"custom_id":"MJ::JOB::variation::{}::{}".format(index, messageHash)}}
  header = {
        'authorization' : Globals.SALAI_TOKEN
    }
  response = requests.post("https://discord.com/api/v9/interactions",
  json = payload, headers = header)
  return response
