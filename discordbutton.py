from pypresence import Presence
import time

client_id = "your client id"
RPC = Presence(client_id=client_id)
RPC.connect()


RPC.update(large_image="IMAGE_NAME",
           large_text="TEXT",
           small_image="image_name",
           small_text="text",
           buttons=[{"label": "URL_NAME", "url": "URL"},
            {"label": "URL_NAME", "url": "URL"}])

while 1:
    time.sleep(15)