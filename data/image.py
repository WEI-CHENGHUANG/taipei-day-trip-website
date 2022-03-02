from encodings import utf_8
import json


# with open("taipei-attractions.json") as result:
#     data = json.load(result)

# result_list = data["result"]["results"]
# totalImage = []
# for i in result_list:
#     image = i["file"].split('https://')
#     image.pop(0)
#     eachIdImage = []
#     for g in image:

#         prefix = "https://"
#         eachIdImage.append(prefix+g)
#     totalImage.append(eachIdImage)
#     # print(f'image: {image}')
#     # print("***************")
#     # print(f'each image: {eachIdImage}')
#     print("==============")
    
# print(totalImage)
testList = ["https://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C1/D68/E883/F368/ff34f438-0a5d-4840-9829-ba6a47d9bc2f.jpg",
                    "https://www.travel.taipei/streams/scenery_file_audio/c16.mp3"]
print(testList[-1][-3:])